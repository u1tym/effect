from typing import Any
import numpy as np

def reduce_noise(
    y: np.ndarray[Any, Any],
    sr: int,
    y_noise: np.ndarray[Any, Any] | None = None,
    prop_decrease: float = 1.0,
    time_mask_smooth_ms: float = 50.0,
    freq_mask_smooth_hz: float = 500.0,
    n_fft: int = 2048,
    win_length: int | None = None,
    hop_length: int | None = None,
    n_std_thresh_stationary: float = 1.5,
    n_std_thresh_nonstationary: float = 1.5,
    stationary: bool = True,
    use_tensorflow: bool = False
) -> np.ndarray[Any, Any]: ...
