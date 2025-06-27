from typing import Tuple
from typing import Any
import numpy as np

def butter(N: int, Wn: float, btype: str = ..., analog: bool = ...) -> Tuple[np.ndarray[Any, Any], np.ndarray[Any, Any]]: ...
def filtfilt(
	b: np.ndarray[Any, Any],
	a: np.ndarray[Any, Any],
	x: np.ndarray[Any, Any]
) -> np.ndarray[Any, Any]: ...
