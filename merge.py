import cv2
image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")
mergeImage = cv2.addWeighted(image1,0.7,image2,0.3,100)
cv2.imshow("mergeImage",mergeImage)
cv2.waitKey(0)
#cv2.imwrite("newImage.jpg",mergeImage)