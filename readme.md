# Memory Leak Detector

## Introduction
This utility tool processes your code with python and uses OpenAI to search for memory leak.

## tl;dr
Run the code by using:
```sh
python src/main.py -s <CODE_DIR> -l c# -e cs -m "As a code reviewer, examine the below code inside the <code> tag, which is from a web app written in C# for memory leak. Respond with only a json object with a key 'has_leak' boolean and a key 'explanation' explaining your reasoning if there is memory leak. Do not return anything else."
```
Replace `<CODE_DIR>` with the directory of your code.


## Installation

1. Clone the repo.
1. (Optional) create a python virtual env `python -m venv venv`.
1. Install requirements `pip install -r requirements.txt`.
1. Create a `.env` file with the following:
    - `OPENAI_API_KEY`: Your OpenAI/Azure OpenAI API Key
    - `OPENAI_ENDPOINT`: Your OpenAI/Azure OpenAI endpoint
    - `OPENAI_DEPLOYMENT`: Your model name (deployment name)
    - `OPENAI_API_VERSION`: API version

## Usage

1. Run `python src/main.py` with the following flags:
    - `-s` or `--source`: address of the folder containing code
    - `-l` or `--lang`: language of the code (e.g., `cs`, `c#`, `cpp`, `c++`)
    - `-e` or `--ext`: file extensions to read (e.g., `cs`, `json`) 
    - `-m` or `--system_msg`: the message (system prompt) that will be included before each code is sent to the API.


## Notes
- The code is wrapped with `<code>...</code>` tag, in case you'd like to refer to it in the `system_msg`.
- Currently, only `c#` is supported.
- The prompt can be anything. You are not limited to memory leak detection. It can be, for instance, "find code smells...", or anything else.
- Eventhough we asked the model to return `json`, a lot of times it does not return a parseable json string, i.e., parsing will throw an error. Be mindful of this fact. 
- Feel free to write support for other languages and submit a pull request.