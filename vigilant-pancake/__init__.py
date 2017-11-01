try:
    import cv2
except ImportError:
    raise ImportError("Please install OpenCV - pip install opencv-python")

try:
    import numpy
except ImportError:
    raise ImportError("Please install numpy - pip install numpy")

from . import graphics