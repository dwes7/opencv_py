import numpy as np
import argparse
import cv2


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# define the list of boundaries (RGB color space)
# for example
# Here, we are saying that all pixels in our image that have a R >= 100, B >= 15, and G >= 17
# along with R <= 200, B <= 56, and G <= 50 will be considered red.
boundaries = [
    ([17, 15, 100], [50, 56, 200]),     # for red
    ([86, 31, 4], [220, 88, 50]),       # blue
    ([25, 146, 190], [62, 174, 250]),   # yellow
    ([103, 86, 65], [145, 133, 128]),   # gray
]

# loop over the boundaries
for (lower, upper) in boundaries:
    # python binding expects these limits to be arrays
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask. inRange function:
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    # show the images
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)
