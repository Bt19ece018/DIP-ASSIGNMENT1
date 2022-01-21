# Python program for adding
# images using OpenCV

# import OpenCV file
import cv2

# Read Image1
one  = cv2.imread('Ad.jpg', 1)

# Read image2
two = cv2.imread('Ad1.jpg', 1)

one = cv2.resize(one,(512,512))
two = cv2.resize(two,(512,512))


# Add the images
img = cv2.add(one, two)

# Show the image
cv2.imshow('image', img)
Ad_added = 'Ad_added.jpg'
  
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(Ad_added, img)

# Wait for a key
cv2.waitKey(0)

# Distroy all the window open
cv2.distroyAllWindows()
