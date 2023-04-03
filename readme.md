# Memory Leak Detector

## Introduction
This utility tool processes your code with python and uses OpenAI to search for memory leak.

Run the code by using:
```sh
python src/main.py -s test_dir/web -l c# -e cs -m "As a code reviewer, examine the below code inside the <code> tag, which is from a web app written in C# for memory leak. Respond with only a json object with a key 'has_leak' boolean and a key 'explanation' explaining your reasoning if there is memory leak. Do not return anything else."
```