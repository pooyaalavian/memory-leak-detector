import dotenv
dotenv.load_dotenv()
import argparse
from src import file_iterator, get_language, assert_lang_supported, get_parser

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", help="Source folder", required=True)
    parser.add_argument("-l", "--lang", help="Language",  default='auto')
    parser.add_argument("-e", "--ext", help="File extensions to be processed",required=True, nargs='+')
    args = parser.parse_args()
    return args


def file_reader(file_path:str)->str:  
    # read the file
    # return the content
    with open(file_path, 'r') as f:
        res = f.read()
        print(file_path)
        print('----------------')
        print(res)
        print('<--EOF')

def main():
    # read the source folder
    pass

if __name__ == "__main__":
    args = parse_args()
    print(args)
    for file_path in  file_iterator(args.source, args.ext):
        lang = get_language(file_path, args.lang)
        assert_lang_supported(args.lang)
        parser = get_parser(lang)
        result = parser(file_path)

