import cv2
  
image = cv2.imread('Ad.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)
Ad_gray = 'Ad_gray.jpg'
  
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(Ad_gray, gray)
  
cv2.waitKey(0)
cv2.destroyAllWindows()

