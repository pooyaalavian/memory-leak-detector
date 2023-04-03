import os
import re
from .base import BaseParser
from src.language import CSHARP
from src.tokenizer import get_token_count

BATCH_READ_THRESH_BYTE = 15*1024  # If file size is larger, read file in chunks
BATCH_READ_THRESH_TOKEN = 2500  # If text has more tokens, read file in chunks


def remove_block_comments(s: str):
    t = s
    while True:
        comment_start = t.find('/*')
        if comment_start == -1:
            break
        comment_end = t.find('*/', comment_start+1)+2
        t = t[0:comment_start]+t[comment_end:-1]
    return t


def remove_line_comments(s: str):
    t = s
    while True:
        comment_start = t.find('//')
        if comment_start == -1:
            break
        comment_end = t.find('\n', comment_start+1)
        t = t[0:comment_start]+t[comment_end:-1]
    return t

def remove_long_spaces(s:str):
    return re.sub(' +', ' ', s)

class CSharpParser(BaseParser):
    def __init__(self):
        super().__init__(CSHARP)

    def parse(self, file_path: str):
        self.file_path = file_path
        file_size = os.path.getsize(file_path)
        print(f'{file_path}: {file_size} bytes', end=' ')
        if file_size < BATCH_READ_THRESH_BYTE:
            return self.parse_small()
        self.parse_large()

    def parse_small(self):
        print('C# small')
        content = open(self.file_path, 'r').read()
        n_tokens = get_token_count(content)
        print(f'before: {n_tokens}',end=' ')

        content = remove_block_comments(content)
        # n_tokens = get_token_count(content)
        # print(f'tokens after block cmt: {n_tokens}')

        content = remove_line_comments(content)
        # n_tokens = get_token_count(content)
        # print(f'tokens after line cmt: {n_tokens}')

        content = remove_long_spaces(content)
        # n_tokens = get_token_count(content)
        # print(f'tokens after space: {n_tokens}')

        n_tokens = get_token_count(content)
        print(f'after: {n_tokens}')

        if n_tokens > BATCH_READ_THRESH_TOKEN:
            return self.parse_large()
        feedback = self.call_api(content)
        return feedback

    def parse_large(self):
        print('C# large')
        pass
