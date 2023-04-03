import argparse 
import os 


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", help="Source folder", required=True)
    parser.add_argument("-l", "--lang", help="Language",  default='auto')
    parser.add_argument("-m", "--system_msg", help="Language",  default=None)
    parser.add_argument(
        "-e", "--ext", help="File extensions to be processed", required=True, nargs='+')
    args = parser.parse_args()
    if args.system_msg is not None:
        os.environ['SYSTEM_MSG'] = args.system_msg
    return args

