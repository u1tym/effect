
from typing import Tuple
from typing import Any
import numpy as np

def load(
    path: str,
    sr: int | None = None,
    mono: bool = True,
    offset: float = 0.0,
    duration: float | None = None,
    dtype: type = np.float32,
    res_type: str = "kaiser_best"
) -> Tuple[np.ndarray[Any, Any], int]: ...
