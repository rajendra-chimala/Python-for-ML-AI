# Question 1

# import numpy as np


# def Matrix_Multiplication (a,b):
#     return a@b

# def E_wise_multiplication(a,b):
#     return a*b

# def determinant(a):
#     det = np.linalg.det(a)
#     return det
    
# def transpose(a):
#     transposed = a.T
#     return transposed



# def main():
    
#     a = np.array([[2,3],[1,4]])
#     b = np.array([[5,2],[3,1]])
    
    
#     print(f"Matrix Multiplication : ",Matrix_Multiplication(a,b))
#     print(f"Element Wise Matrix Multiplication : ",E_wise_multiplication(a,b))
#     print(f"Determinant : ",determinant(a))
#     print(f"Transposed : ",transpose(a))
    
    
# main()

# ===========================================================================================
# Question 2

# import numpy as np

# array = np.random.randint(10,101,(6,6))

# print(f"Random array : {array}")

# diagonal_elemtnts = np.diag(array)

# print(f"Diagonal elements of an array : {diagonal_elemtnts}")


# new_matrix = array.astype(float)

# even_pos = (new_matrix %2 == 0)

# new_matrix[even_pos] = np.sqrt(new_matrix[even_pos])

# print(f"The Replaced Matrix with even number with squar root : {new_matrix}")

# print(f"Mean value : {np.mean(new_matrix)}")
# print(f"Median value : {np.median(new_matrix)}")
# print(f"Standard Deviation value : {np.std(new_matrix)}")


# reshaped_array = new_matrix.reshape(4,9)


# print(f"REshaped Matris is : {reshaped_array}")


# Question 3

# import cv2 as cv

# image = cv.imread("img\image.png")

# gray_img = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

# cv.imshow("Gray Image",gray_img)
# cv.imshow("Original Image",image)

# cv.waitKey(0)
# cv.destroyAllWindows()


# cv.imwrite("img\copy_img.png",gray_img)


# print(f"Image Height : ",image.shape[0])
# print(f"Image Weight : ",image.shape[1])
# print(f"Image Channel : ",image.shape[2])


# Question 4

# import cv2 as cv
# import os

# def resize_image_operations(image_path, output_dir="resized_outputs"):
    
#     image = cv.imread(image_path)
#     if image is None:
#         print("Error: Image not found.")
#         return

#     os.makedirs(output_dir, exist_ok=True)

#     original_height, original_width = image.shape[:2]
#     print(f"Original Dimensions: {original_width}x{original_height}")

#     # Resize 50% smaller
#     small = cv.resize(image, (0, 0), fx=0.5, fy=0.5)
    
#     cv.imshow("50% Smaller Image", small)
#     cv.imwrite(f"{output_dir}/resized_50_percent_smaller.jpg", small)

#     # Resize 200% larger
#     large = cv.resize(image, (0, 0), fx=2.0, fy=2.0)
   
#     cv.imshow("200% Larger Image", large)
#     cv.imwrite(f"{output_dir}/resized_200_percent_larger.jpg", large)

#     #  300x300 
#     fixed = cv.resize(image, (300, 300))
#     cv.imwrite(f"{output_dir}/resized_fixed_300x300.jpg", fixed)

#     # Maintain aspect ratio
#     aspect_ratio = original_height / original_width
#     new_height = int(300 * aspect_ratio)
#     aspect_resized = cv.resize(image, (300, new_height))
#     cv.imshow("Aspect Ratio Resized Image", aspect_resized)
#     cv.imwrite(f"{output_dir}/resized_300_aspect_ratio.jpg", aspect_resized)
    
#     cv.waitKey(0)
#     cv.destroyAllWindows()

    
# resize_image_operations("img\image0.jpg")


# # =======================================================================================

# # Question 5
# import cv2
# import numpy as np
# import argparse

# def apply_filters(image, k_gauss, k_avg, k_median):
#     # Ensure kernel sizes are odd and >= 3
#     k_gauss = max(3, k_gauss | 1)
#     k_avg = max(3, k_avg | 1)
#     k_median = max(3, k_median | 1)

#     # Blurring
#     gaussian = cv2.GaussianBlur(image, (k_gauss, k_gauss), 0)
#     average = cv2.blur(image, (k_avg, k_avg))
#     median = cv2.medianBlur(image, k_median)

#     # Convert to grayscale for edge detection
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Canny Edge Detection
#     canny = cv2.Canny(gray, 100, 200)

#     # Sobel Edge Detection
#     sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
#     sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
#     sobel_x = cv2.convertScaleAbs(sobel_x)
#     sobel_y = cv2.convertScaleAbs(sobel_y)
#     sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

#     return [image, gaussian, average, median, canny, sobel]

# def stack_images(images, scale=0.5):
#     img_row1 = cv2.hconcat([cv2.resize(img if len(img.shape) == 3 else cv2.cvtColor(img, cv2.COLOR_GRAY2BGR),
#                                         (0, 0), fx=scale, fy=scale) for img in images[:3]])
#     img_row2 = cv2.hconcat([cv2.resize(img if len(img.shape) == 3 else cv2.cvtColor(img, cv2.COLOR_GRAY2BGR),
#                                         (0, 0), fx=scale, fy=scale) for img in images[3:]])
#     return cv2.vconcat([img_row1, img_row2])

# def main():
#     parser = argparse.ArgumentParser(description="Image Filtering Tool")
#     parser.add_argument('--image', required=True, help="Path to input image")
#     parser.add_argument('--gauss', type=int, default=15, help="Gaussian blur kernel size (odd number)")
#     parser.add_argument('--avg', type=int, default=10, help="Average blur kernel size (odd number)")
#     parser.add_argument('--median', type=int, default=9, help="Median blur kernel size (odd number)")
#     args = parser.parse_args()

#     image = cv2.imread(args.image)
#     if image is None:
#         print("Error: Image not found!")
#         return

#     results = apply_filters(image, args.gauss, args.avg, args.median)
#     combined = stack_images(results)

#     cv2.imshow("Image Filtering Results", combined)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# main()

# =======================================================================================

# Question 6
# import cv2 as cv

# face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

# cap = cv.VideoCapture(0)


# while True :
#     tr,frame = cap.read()
    
#     gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
#     face = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5) #X Y W H
    
#     for(x,y,w,h) in face:
#         cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
#     cv.imshow("Face Detection",frame)
        
#     if cv.waitKey(1) & 0xFF == ord(" "):
#         break
        
# cap.release()
# cv.destroyAllWindows()
    
    
    
# =======================================================================================

# Question 7
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.feature_extraction import image

# # Load and convert to grayscale
# img_color = cv2.imread('img\image0.jpg')  
# if img_color is None:
#     print("[Error] Image not found. Make sure 'sample.jpg' exists.")
#     exit()

# img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# # Represent grayscale image as a 2D matrix
# gray_matrix = np.array(img_gray, dtype=np.float32)

# # Extract 5x5 patches from the image and compute the covariance matrix
# patches = image.extract_patches_2d(gray_matrix, (5, 5))
# patches_reshaped = patches.reshape(patches.shape[0], -1) 

# # Mean-center the data
# mean_patch = np.mean(patches_reshaped, axis=0)
# patches_centered = patches_reshaped - mean_patch

# #Compute covariance matrix (features x features)
# cov_matrix = np.cov(patches_centered, rowvar=False)

# eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)  

# alpha = 1.2  
# transform_matrix = np.array([[alpha]])  

# # Apply transformation
# transformed_matrix = gray_matrix * transform_matrix
# transformed_matrix = np.clip(transformed_matrix, 0, 255).astype(np.uint8)

# #Display original and transformed images side-by-side
# plt.figure(figsize=(10, 4))
# plt.subplot(1, 2, 1)
# plt.imshow(gray_matrix, cmap='gray')
# plt.title('Original Grayscale')
# plt.axis('off')

# plt.subplot(1, 2, 2)
# plt.imshow(transformed_matrix, cmap='gray')
# plt.title(f'Transformed (alpha={alpha})')
# plt.axis('off')
# plt.tight_layout()
# plt.show()

# #Plot histograms of intensity distributions
# plt.figure(figsize=(10, 4))
# plt.subplot(1, 2, 1)
# plt.hist(gray_matrix.ravel(), bins=256, range=[0, 256], color='gray')
# plt.title('Histogram - Original')

# plt.subplot(1, 2, 2)
# plt.hist(transformed_matrix.ravel(), bins=256, range=[0, 256], color='orange')
# plt.title('Histogram - Transformed')
# plt.tight_layout()
# plt.show()


# ============================================================================================
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from datetime import datetime

# Constants
INPUT_DIR = "images"  # Folder containing input images
OUTPUT_DIR = "results"
STANDARD_SIZE = (512, 512)
CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load Haar cascade
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
if face_cascade.empty():
    raise IOError("Haar cascade XML file not found!")

# Feature storage
summary = []
collage_images = []

# Utility Functions
def compute_edge_density(edge_img):
    return np.sum(edge_img > 0) / edge_img.size

def compute_contrast(gray_img):
    return np.std(gray_img)

def create_collage(images, rows, cols, title):
    h, w = images[0].shape[:2]
    collage = np.zeros((rows * h, cols * w, 3), dtype=np.uint8)
    for idx, img in enumerate(images):
        y, x = divmod(idx, cols)
        if img.ndim == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        collage[y*h:(y+1)*h, x*w:(x+1)*w] = img
    cv2.imwrite(os.path.join(OUTPUT_DIR, title), collage)

# Process each image
image_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]

for filename in image_files:
    filepath = os.path.join(INPUT_DIR, filename)
    original = cv2.imread(filepath)
    if original is None:
        print(f"[Warning] Skipping unreadable image: {filename}")
        continue

    resized = cv2.resize(original, STANDARD_SIZE)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Canny Edge Detection
    edges = cv2.Canny(blurred, 100, 200)
    edge_density = compute_edge_density(edges)

    # Face Detection
    faces = face_cascade.detectMultiScale(blurred, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(resized, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Statistics
    mean_intensity = np.mean(blurred)
    contrast = compute_contrast(blurred)

    # Store features
    summary.append([filename, mean_intensity, contrast, edge_density, len(faces)])
    collage_images.extend([cv2.resize(original, (256, 256)), cv2.resize(edges, (256, 256))])

    # Save intermediate images
    cv2.imwrite(os.path.join(OUTPUT_DIR, f"{filename}_gray.jpg"), gray)
    cv2.imwrite(os.path.join(OUTPUT_DIR, f"{filename}_edges.jpg"), edges)
    cv2.imwrite(os.path.join(OUTPUT_DIR, f"{filename}_faces.jpg"), resized)

# Convert summary to NumPy array
summary_np = np.array([row[1:] for row in summary], dtype=np.float32)

# Analysis: Normalize & Linear Algebra
scaler = StandardScaler()
summary_norm = scaler.fit_transform(summary_np)
cov_matrix = np.cov(summary_norm.T)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Identify image with highest edge density
densities = summary_np[:, 2]
max_density_idx = np.argmax(densities)
most_edges_filename = summary[max_density_idx][0]

# Save report
report_path = os.path.join(OUTPUT_DIR, "report.txt")
with open(report_path, "w") as report:
    report.write(f"Image Analysis Report - {datetime.now()}\n")
    report.write("="*40 + "\n")
    for row in summary:
        report.write(f"File: {row[0]}\n")
        report.write(f"Mean Intensity: {row[1]:.2f}, Contrast: {row[2]:.2f}, Edge Density: {row[3]:.4f}, Faces: {row[4]}\n\n")
    report.write(f"Image with highest edge density: {most_edges_filename}\n\n")
    report.write("Eigenvalues of Feature Covariance Matrix:\n")
    report.write(", ".join(f"{val:.4f}" for val in eigenvalues))

# Save collage
create_collage(collage_images, rows=len(image_files), cols=2, title="collage.jpg")

print("[✅] Pipeline completed successfully.")
print(f"📄 Report saved to: {report_path}")
print(f"🖼️ Collage saved to: {os.path.join(OUTPUT_DIR, 'collage.jpg')}")
