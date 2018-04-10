import cv2 as cv
from skimage.measure import structural_similarity as ssim


# Calculate SSIM
first = cv.imread("real-screen-image.png")

#second = cv.imread("captured.png")
second = cv.imread("unfiltered.png")

first = cv.resize(first, (2576,1125))
second = cv.resize(second, (2576,1125))
first = cv.cvtColor(first, cv.COLOR_BGR2GRAY)
second = cv.cvtColor(second, cv.COLOR_BGR2GRAY)
s = ssim(first, second)

print(s)
