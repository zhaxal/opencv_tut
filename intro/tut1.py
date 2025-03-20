import cv2

img = cv2.imread("assets/img.JPEG", 0)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("assets/new_img.JPEG", img)

cv2.imshow("image", img)

k = cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()