from typing import Tuple
from typing import Any
from typing import Optional
from typing import Union
import numpy as np

def butter(N: int, Wn: float, btype: str = ..., analog: bool = ...) -> Tuple[np.ndarray[Any, Any], np.ndarray[Any, Any]]: ...
def filtfilt(
	b: np.ndarray[Any, Any],
	a: np.ndarray[Any, Any],
	x: np.ndarray[Any, Any]
) -> np.ndarray[Any, Any]: ...

def wiener(
	im: np.ndarray[Any, Any],
	mysize: Union[int, tuple[int, ...]] = 3,
	noise: Optional[float] = None
) -> np.ndarray[Any, Any]: ...
