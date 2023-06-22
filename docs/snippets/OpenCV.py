import cv2

# Read an image from file
image = cv2.imread('image.jpg')

# Display an image in a window
cv2.imshow('Window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save an image to file
cv2.imwrite('output.jpg', image)

# Convert an image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize an image
resized_image = cv2.resize(image, (width, height))

# Rotate an image
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

# Apply Gaussian blur to an image
blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

# Perform Canny edge detection on an image
edges = cv2.Canny(image, threshold1, threshold2)

# Detect objects using Haar cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray_image, scaleFactor, minNeighbors)

# Draw rectangles on an image
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), thickness)

# Apply image thresholding
ret, thresholded_image = cv2.threshold(gray_image, threshold_value, max_value, threshold_type)

# Perform image morphology operations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
morphology_result = cv2.morphologyEx(image, cv2.MORPH_OPERATION, kernel)

# Apply image masking
masked_image = cv2.bitwise_and(image, image, mask=mask)

# Calculate image gradients using Sobel operators
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize)

# Perform image blending
blended_image = cv2.addWeighted(image1, alpha, image2, beta, gamma)

# Perform template matching
result = cv2.matchTemplate(image, template, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), thickness)

# Apply perspective transformation
src_points = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
dst_points = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
warped_image = cv2.warpPerspective(image, perspective_matrix, (width, height))

# Access pixel values of an image
pixel_value = image[y, x]
image[y, x] = (blue, green, red)

# Split and merge image channels
b, g, r = cv2.split(image)
merged_image = cv2.merge((b, g, r))
