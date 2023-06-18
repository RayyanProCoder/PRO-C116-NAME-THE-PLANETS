import cv2

# Read the image
img = cv2.imread("solar-system.jpg")

# Add text to the image
cv2.putText(img, "Sun", (20, 300), cv2.FONT_HERSHEY_COMPLEX, 8.5, (255, 255, 255))
cv2.putText(img, "Mercury", (300, 50), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255))
cv2.putText(img, "Venus", (500, 50), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255))
cv2.putText(img, "Earth", (750, 50), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255))
cv2.putText(img, "Mars", (1050, 50), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255))
cv2.putText(img, "Jupiter", (200, 900), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255))
cv2.putText(img, "Saturn", (600, 900), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255))
cv2.putText(img, "Uranus", (950, 900), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255))
cv2.putText(img, "Neptune", (1300, 900), cv2.FONT_HERSHEY_COMPLEX, 4, (255, 255, 255))

# Display the image
cv2.imshow("output", img)
cv2.waitKey(0)

# Save the final image
cv2.imwrite("Solar_systemwithname.jpg", img)
