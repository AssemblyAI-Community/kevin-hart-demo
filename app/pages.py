from flask import Blueprint, render_template, current_app, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import assemblyai as aai
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired

bp = Blueprint("pages", __name__)

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

def replace_extension_txt(filename):
    base, _ = os.path.splitext(filename)
    return f"{base}.txt"

@bp.route('/transcripts', methods=['GET', 'POST'])
def transcripts():
    prompt = "Provide a brief summary of the transcript."
    upload_status = ""
    transcript_text = None
    lemur_response = None
    audio_files = []
    uploads_dir = os.path.join(current_app.root_path, 'static', 'uploads')


    form=UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        audio_file_save = os.path.join(os.path.abspath(os.path.dirname(__file__)),current_app.config['UPLOAD_FOLDER'],secure_filename(file.filename))
        file.save(audio_file_save)
        audio_url = audio_file_save
        upload_status = "File is processing!"

        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(audio_url)
        base_filename, _ = os.path.splitext(audio_file_save)
        text_file_save = f"{base_filename}.txt"

        transcript_text = transcript.get_paragraphs()

        with open(text_file_save, 'w') as txt_file:
            for paragraph in transcript_text:
                txt_file.write(paragraph.text)
                txt_file.write('\n\n')
        upload_status = "File has been uploaded!"

    for filename in os.listdir(uploads_dir):
        if filename.endswith('.wav') or filename.endswith('.mp3') or filename.endswith('.m4a'):
            audio_files.append(filename)

    return render_template('pages/transcripts.html', upload_status=upload_status, transcript_text=transcript_text, prompt = prompt, lemur_response = lemur_response, form=form, audio_files=audio_files)

@bp.route('/file_content/<filename>')
def get_file_content(filename):
    uploads_dir = os.path.join(current_app.root_path, 'static', 'uploads')
    txt_filename = replace_extension_txt(filename)
    txt_file_path = os.path.join(uploads_dir, txt_filename)

    text_content = None

    if os.path.exists(txt_file_path):
        try:
            with open(txt_file_path, 'r') as file:
                text_content = file.read()
        except FileNotFoundError:
            pass  # Ignore if the text file is not found
    return jsonify({'content': text_content})

@bp.route('/serve_audio/<filename>')
def serve_audio(filename):
    uploads_dir = os.path.join(current_app.root_path, 'static', 'uploads')
    return send_from_directory(uploads_dir, filename)

@bp.route('/static/<path:filename>')
def serve_static(filename):
    print(f"Serving static file: {filename}")
    return send_from_directory('static', filename)

@bp.route("/")
def home():
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")