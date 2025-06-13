import cv2

# Load the image (change to cat.jpg or add a dog image to assets folder)
img = cv2.imread("assets/Balkan.jpg", cv2.IMREAD_COLOR)  # or use a dog image
print(img.shape) # print the image dimensions
print(img[0, 0]) # print the first pixel

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow("Gray Dog", gray_img) 
# Save the grayscale image
cv2.imwrite("assets/Balkan_gray.jpg", gray_img)
cv2.waitKey(0) # pause the program until any key is pressed
cv2.destroyAllWindows()