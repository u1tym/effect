import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import argparse

from dataclasses import dataclass

@dataclass
class Parameters:
    inputfile: str
    outputfile: str

def parse_args() -> Parameters:
    parser = argparse.ArgumentParser(description="あいうえお")
    parser.add_argument("--inputfile", required=True, help="入力ファイル")
    parser.add_argument("--outputfile", required=True, help="出力ファイル")

    args: argparse.Namespace =  parser.parse_args()
    result: Parameters = Parameters(
        inputfile=args.inputfile,
        outputfile=args.outputfile
    )
    return result


def main() -> None:
    args = parse_args()

    print(f"input file = {args.inputfile}")
    return

if __name__ == '__main__':
    main()
