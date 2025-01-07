import cv2

# Load an image
image = cv2.imread('image.jpg')  # Replace 'image.jpg' with your image file name

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image.")
    exit()

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Detect edges using Canny edge detector
edges = cv2.Canny(blurred_image, 50, 150)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)

# Save the edges image
cv2.imwrite('edges.jpg', edges)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()