import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import argparse

import librosa
import soundfile as sf
from scipy.signal import wiener

from typing import Union
from typing import Optional
from typing import Tuple

from dataclasses import dataclass

@dataclass
class Parameters:
    inputfile: str
    outputfile: str

def parse_args() -> Parameters:
    parser = argparse.ArgumentParser(description="残響軽減処理")
    parser.add_argument("--inputfile", required=True, help="入力ファイル")
    parser.add_argument("--outputfile", required=True, help="出力ファイル")

    args: argparse.Namespace =  parser.parse_args()
    result: Parameters = Parameters(
        inputfile=args.inputfile,
        outputfile=args.outputfile
    )
    return result


def proc(inputfile: str, outputfile: str) -> None:

    # 音声ファイルの読み込み
    y, sr = librosa.load(inputfile, sr=None)

    # フィルターサイズ
    # 大きくすると滑らかになるが、ディテールが失われる
    fsize: Union[int, Tuple[int, ...]] = (5,)

    # ノイズ指定値
    # 値を大きくすると、より強くフィルタリング
    # ex) None, 0.1, 0.5
    noise: Optional[float] = None

    # 残響軽減のための簡易的な処理（Wienerフィルター）
    y_dereverb = wiener(
        y,
        mysize=fsize,
        noise=noise)

    # 出力ファイルの保存
    sf.write(outputfile, y_dereverb, sr)

    print("残響軽減処理が完了しました。")



    return

def main() -> None:
    args = parse_args()

    proc(args.inputfile, args.outputfile)

    return

if __name__ == '__main__':
    main()
