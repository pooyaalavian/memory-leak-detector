
class Parser:
    def __init__(self, file_path, lang: str):
        self.file_path = file_path
        self.lang = lang
        self.blocks = []

    def parse(self):
        raise NotImplementedError('Must be implemented in child classx')

    def __call__(self):
        return self.parse()
