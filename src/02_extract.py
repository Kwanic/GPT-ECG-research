import numpy as np

def pnn50(rr_ms):
    diff = np.abs(np.diff(rr_ms))
    return (diff > 50).mean()

FEATURE_FUNCS = {
    "pnn50": lambda beats: pnn50(rr_from_beats(beats)),
    # TODO: 其他特征函数
}
