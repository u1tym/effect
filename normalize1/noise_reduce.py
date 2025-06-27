import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import argparse

from pydub import AudioSegment

from dataclasses import dataclass

@dataclass
class Parameters:
    inputfile: str
    outputfile: str

def parse_args() -> Parameters:
    parser = argparse.ArgumentParser(description="ノイズ除去")
    parser.add_argument("--inputfile", required=True, help="入力ファイル")
    parser.add_argument("--outputfile", required=True, help="出力ファイル")

    args: argparse.Namespace =  parser.parse_args()
    result: Parameters = Parameters(
        inputfile=args.inputfile,
        outputfile=args.outputfile
    )
    return result


def proc(inputfile: str, outputfile: str) -> None:

    # 音量正規化（RMSノーマライズ）
    audio: AudioSegment = AudioSegment.from_wav(inputfile)

    # RMS値を基準に音量調整（例：-20dBを目指す）
    target_dBFS = -20.0
    change_dBFS = target_dBFS - audio.dBFS
    normalized_audio = audio.apply_gain(change_dBFS)

    # 保存
    normalized_audio.export(outputfile, format='wav')

    return

def main() -> None:
    args = parse_args()

    proc(args.inputfile, args.outputfile)

    return

if __name__ == '__main__':
    main()
