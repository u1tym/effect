import numpy as np

from typing import Tuple
from typing import Union
from typing import Any

def write(
    file: str,
    data: np.ndarray[Any, Any],
    samplerate: int,
    subtype: str | None = None,
    endian: str | None = None,
    format: str | None = None,
    closefd: bool = False
) -> None: ...

def read(
    file: str,
    frames: int | None = None,
    start: int = 0,
    stop: int | None = None,
    dtype: type = np.float64,
    always_2d: bool = False,
    fill_value: Union[int, float] = 0,
    out: np.ndarray[Any, Any] | None = None
) -> Tuple[np.ndarray[Any, Any], int]: ...
