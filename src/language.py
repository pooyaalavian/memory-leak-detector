
CSHARP = 'c#'
CPP = 'cpp'
PYTHON = 'python'
OTHER = 'other'
SUPPORT_LANGS = [CSHARP]

LANG_LOOKUP = {
    'cs': CSHARP,
    'c#': CSHARP,
    'c++': CPP,
}

def get_language(file_path:str, lang:str)->str:
    if lang != 'auto':
        return lang
    # get the language from the file path
    # return the language
    ext = file_path.split('.')[-1].lower()
    detected_lang = LANG_LOOKUP.get(ext, OTHER)
    return detected_lang


def assert_lang_supported(lang:str):
    if lang not in SUPPORT_LANGS:
        raise Exception(f'Language {lang} is not supported')
    