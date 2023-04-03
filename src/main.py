import dotenv
import sys
from  pathlib import Path

sys.path.append(str(Path('.').absolute()))
print(sys.path)
dotenv.load_dotenv()
from src import file_iterator, get_language, assert_lang_supported, get_parser, parse_args


def main(args):
    for file_path in file_iterator(args.source, args.ext):
        lang = get_language(file_path, args.lang)
        assert_lang_supported(args.lang)
        parser = get_parser(lang)
        content = parser(file_path)
        print(content)
        # result = parser(file_path)
        # break



if __name__ == "__main__":
    args = parse_args()
    main(args)
