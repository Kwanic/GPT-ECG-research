import wfdb
import matplotlib.pyplot as plt
from pathlib import Path

def plot_record(record_id="100", data_dir="data/raw/mitbih", out_dir="reports/plots"):
    """
    读取 MIT-BIH 记录并保存为 PNG 图像
    """
    rec_path = Path(data_dir) / record_id
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # 读取信号和注释
    record = wfdb.rdrecord(str(rec_path))
    ann = wfdb.rdann(str(rec_path), "atr")

    sig = record.p_signal[:, 0]   # 取第1通道 (MLII)
    fs = record.fs

    # 只画前10秒，避免太长
    n_samples = int(10 * fs)
    t = [i/fs for i in range(n_samples)]

    plt.figure(figsize=(12, 4))
    plt.plot(t, sig[:n_samples], label="ECG (MLII)")

    # 标注R峰位置（前10秒内的）
    ann_in_range = [(s, sym) for s, sym in zip(ann.sample, ann.symbol) if s < n_samples]
    for s, sym in ann_in_range:
        plt.axvline(s/fs, color="r", linestyle="--", alpha=0.6)
        plt.text(s/fs, sig[s]+0.1, sym, color="red", fontsize=8)

    plt.title(f"MIT-BIH Record {record_id} (First 10s)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (mV)")
    plt.legend()
    plt.tight_layout()

    save_file = out_path / f"{record_id}_first10s.png"
    plt.savefig(save_file, dpi=150)
    plt.close()

    print(f"✅ Saved {save_file}")

if __name__ == "__main__":
    plot_record("100")
