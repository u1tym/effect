import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import argparse

import noisereduce as nr
import librosa
import soundfile as sf

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

    # WAVファイルの読み込み
    y, sr = librosa.load(inputfile, sr=None)

    # ノイズ除去（3～5秒区間をノイズと仮定）
    noise_st: int = int(sr * 3)
    noise_ed: int = int(sr * 5)
    reduced_noise = nr.reduce_noise(
        y=y,
        sr=sr,
        n_fft=4096,
        win_length=4096,
        hop_length=1024,
        prop_decrease=0.8,
        stationary=False,
        y_noise=y[noise_st:noise_ed])

    # 結果を保存
    sf.write(outputfile, reduced_noise, sr)

    return

def main() -> None:
    args = parse_args()

    proc(args.inputfile, args.outputfile)

    return

if __name__ == '__main__':
    main()
