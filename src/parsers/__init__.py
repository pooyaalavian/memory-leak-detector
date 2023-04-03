from .base import BaseParser
from .csharp import CSharpParser


def get_parser(lang: str) -> BaseParser:
    if lang == 'c#':
        return CSharpParser()
    raise Exception(f'Language {lang} is not supported')
