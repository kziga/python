# SLIC / click based image segmentation
# Or maybe just a bunch of segmentation implementations

import cv2 # import opencv
import numpy as np


if __name__ == "__main__":

	filename = "images/Lenna.png"

	im = cv2.imread(filename,cv2.IMREAD_COLOR)

	print( im.shape )

	cv2.imshow("Test",im)
	cv2.waitKey()
	cv2.destroyAllWindows()