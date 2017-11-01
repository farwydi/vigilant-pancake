try:  # pragma: no cover
    import cv2
except ImportError:  # pragma: no cover
    raise ImportError("Please install OpenCV - pip install opencv-python")

try:  # pragma: no cover
    import numpy
except ImportError:  # pragma: no cover
    raise ImportError("Please install numpy - pip install numpy")
