import openai
import requests
import os
import json


class BaseParser:
    def __init__(self, lang: str):
        self.lang = lang
        self.system_msg = os.getenv('SYSTEM_MSG')

        if self.system_msg is None:
            raise ValueError('system_msg cannot be empty')
        if lang is None:
            raise ValueError('lang  cannot be empty')
        # self.file_path = file_path
        # self.blocks = []

    def parse(self, file_path: str):
        raise NotImplementedError('Must be implemented in child classx')

    def call_api(self, chunk: str):
        prompt = f'{self.system_msg}\n\n<code>\n{chunk}\n</code>'
        openai.api_key = os.environ['OPENAI_API_KEY']
        openai.api_base = os.environ['OPENAI_ENDPOINT']
        openai.api_version = os.environ['OPENAI_API_VERSION']
        deployment = os.environ['OPENAI_DEPLOYMENT']
        payload = {"prompt": prompt, "max_tokens": 100, "temperature": 0.75, }

        try:
            response = requests.post(
                f"{openai.api_base}openai/deployments/{deployment}/completions?api-version={openai.api_version}",
                json.dumps(payload),
                headers={"api-key": openai.api_key}
            ).json()
            res = response['choices'][0]['text']
            try:
                res_json = json.loads(res)
                return f'OPENAI (json): {json.dumps(res_json)}'
            except:
                return 'OPENAI: '+'\nOPENAI: '.join(res.split('\n'))
        except Exception as e:
            print(e)
            return response

    def __call__(self, file_path: str):
        return self.parse(file_path)
