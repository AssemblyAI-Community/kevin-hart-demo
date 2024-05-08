# Kevin Hart Demo App

Companion repo for the YouTube Short - Transcribe your ideas like Kevin Hart Using AssemblyAI

You can run the application without changes, just add your AssemblyAI API key.

## Prerequisites
You must have:
1. [Python](https://www.python.org/) installed
2. [pip](https://pip.pypa.io/en/stable/installation/) installed
3. An [AssemblyAI](https://www.assemblyai.com/dashboard/signup) account

## Setup

1. Clone this repository and cd into it
    ```bash
    git clone https://github.com/AssemblyAI-Examples/kevin-hart-demo.git
    cd kevin-hart-demo
    ```

2. Create and activate a virtual environment (optional)

    MacOS/Linux:
    ```bash
    python -m venv venv  # you may need to use `python3` instead
    source ./venv/bin/activate
    ```

    Windows:
    ```bash
    python -m venv venv  # you may need to use `python3` instead
    .\venv\Scripts\activate.bat
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Set your AssemblyAI API key as an environment variable (you can get a key [here](https://www.assemblyai.com/dashboard/signup))
```shell
# Mac/Linux:
export ASSEMBLYAI_API_KEY=<YOUR_KEY>

# Windows:
set ASSEMBLYAI_API_KEY=<YOUR_KEY>
```
5. Run `python run.py` to locally run the Kevin Hart Demo App
