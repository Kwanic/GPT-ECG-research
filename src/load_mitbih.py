import wfdb
import pandas as pd
import numpy as np
from pathlib import Path

def download_mitbih(save_dir="data/raw/mitbih", record_ids=[100, 101, 102]):
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)

    for rec in record_ids:
        rec_name = str(rec)
        # 下载信号+注释
        wfdb.dl_database(
            "mitdb",
            dl_dir=str(save_path),
            records=[rec_name]
        )
    print(f"✅ MIT-BIH records {record_ids} downloaded to {save_path}")

def load_mitbih_record(rec_path="data/raw/mitbih/100"):
    # 读取信号
    record = wfdb.rdrecord(rec_path)
    annotation = wfdb.rdann(rec_path, "atr")

    sig = record.p_signal[:,0]  # 取第一导联
    fs = record.fs
    ann_samples = annotation.sample
    ann_symbols = annotation.symbol

    return sig, fs, ann_samples, ann_symbols

if __name__ == "__main__":
    download_mitbih()
    sig, fs, ann_s, ann_sym = load_mitbih_record("data/raw/mitbih/100")
    print(f"Signal length: {len(sig)} samples @ {fs}Hz")
    print("First 10 annotations:", ann_sym[:10])
