import glob


def file_iterator(source: str, exts: list[str]) -> list:
    '''iterate through the files in the source folder and subfolders
    filter the files by the extension
    return an iterator object'''
    if type(exts) == str:
        exts = [exts]
    res = [glob.glob(f"{source}/**/*.{ext}", recursive=True) for ext in exts]
    res = [item for sublist in res for item in sublist]
    return res
