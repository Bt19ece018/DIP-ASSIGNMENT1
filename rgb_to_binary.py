import cv2

# read the image file
img = cv2.imread('Ad.jpg', 2)

ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# converting to its binary form
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary", bw_img)

Ad_binary = 'Ad_bnary.jpg'
  
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(Ad_binary, bw_img)
  
cv2.waitKey(0)
cv2.destroyAllWindows()
