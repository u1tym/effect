import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import argparse

import numpy as np
import scipy.io.wavfile as wav
import scipy.signal as signal

from dataclasses import dataclass

@dataclass
class Parameters:
    inputfile: str
    outputfile: str

def parse_args() -> Parameters:
    parser = argparse.ArgumentParser(description="ハイパスフィルター")
    parser.add_argument("--inputfile", required=True, help="入力ファイル")
    parser.add_argument("--outputfile", required=True, help="出力ファイル")

    args: argparse.Namespace =  parser.parse_args()
    result: Parameters = Parameters(
        inputfile=args.inputfile,
        outputfile=args.outputfile
    )
    return result


def proc(inputfile: str, outputfile: str) -> None:

    # WAVファイルの読み込み
    rate, data = wav.read(inputfile)

    # ステレオの場合はモノラルに変換
    if len(data.shape) == 2:
        data = data.mean(axis=1)

    # ハイパスフィルタ設計（例：300Hz以上を通す）
    cutoff = 300    # Hz
    nyquist = 0.5 * rate
    normal_cutoff = cutoff / nyquist
    b, a = signal.butter(4, normal_cutoff, btype='high', analog=False)

    # フィルタ適用
    filtered_data = signal.filtfilt(b, a, data)

    # 結果の保存
    wav.write(outputfile, rate, filtered_data.astype(np.int16))


    return

def main() -> None:
    args = parse_args()

    proc(args.inputfile, args.outputfile)

    return

if __name__ == '__main__':
    main()
