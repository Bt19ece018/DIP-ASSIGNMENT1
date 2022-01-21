# Python program for adding
# images using OpenCV

# import OpenCV file
import cv2

# Read Image1
one  = cv2.imread('Ad.jpg', 1)

# read scaler value of 20
two = 20 


# Add the images
img = cv2.add(one, two)

# Show the image
cv2.imshow('image', img)
Ad_added_scaler = 'Ad_added_scaler.jpg'
  
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(Ad_added_scaler, img)

# Wait for a key
cv2.waitKey(0)

# Distroy all the window open
cv2.distroyAllWindows()
