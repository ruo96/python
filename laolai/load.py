import pprint

import pandas as pd
import numpy as np
import hashlib


def convert_string(s: str, digits: int = 15) -> str:
    """Maps a string to a unique hash using SHA, converts it to a hash or an int"""
    if type(s) is str:
        new_hash = int(hashlib.sha256(s.encode("utf-8")).hexdigest(), 16) % 10 ** digits
        return new_hash
    else:
        return s


def convert_float(f: float, precision: int = 2) -> int:
    """由于默认精度是 .00 所以我们直接 * 100 后转成 int """
    if isinstance(f, float):
        return f * 10 ** precision
    else:
        return f


def load_column(csv: str, column: str, original_type: str) -> np.ndarray:
    """获取 int32 形式编码好的值"""
    pd_data = pd.read_csv(csv)
    print("------------------------{0}------------------------".format(csv))
    pprint.pprint(pd_data.head())
    column_data = pd_data[column].values
    ls = None
    if original_type == 'str':
        ls = [convert_string(s) for s in column_data]
    elif original_type == 'float':
        ls = [convert_float(s) for s in column_data]
    else:
        ls = [s for s in column_data]
    rt = np.array(ls).astype(np.int32)
    print("------------------------{0}------------------------".format(column))
    pprint.pprint(rt[0:5])
    return rt


if __name__ == "__main__":
    ids = load_column("dataset/zetyun.csv", "id", "str")
    values = load_column("dataset/zetyun.csv", "value", "float")