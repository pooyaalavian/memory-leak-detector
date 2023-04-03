import sys
import os
from pathlib import Path
sys.path.append(str(Path('.').absolute()))
from src.main import main


class Arg:
    def __init__(self, src: str, lang: str, msg: str, exts=[]):
        self.source = src
        self.lang = lang
        self.system_msg = msg
        self.ext = exts
        os.environ['SYSTEM_MSG'] = self.system_msg




if __name__ == '__main__':
    args = Arg(
        'test_dir/web', 'c#',
        '''\
As a code reviewer, examine the below code inside the <code> tag, which is from a web app written in C# for memory leak.
Respond with only a json object with a key "has_leak" boolean and a key "explanation" explaining your reasoning if there is memory leak. 
Do not return anything else.
''', exts=['cs'])
    main(args)
