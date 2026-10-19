import cv2
import numpy as np
import os
from pathlib import Path

output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

dataset_dir = Path("coins-dataset")

coin_files = {
    "20_piso": dataset_dir / "20_piso.jpg",
    "1_piso": dataset_dir / "1_piso.jpeg",
    "10_sentimo": dataset_dir / "10_sentimo.jpeg"
}

images = {}
for name, path in coin_files.items():
    img = cv2.imread(str(path))
    if img is None:
        raise FileNotFoundError(f"Could not load {path}")
    images[name] = img
    print(f"Loaded {name}: {img.shape}")

target_h = 500

resized = {}
for name, img in images.items():
    h, w = img.shape[:2]
    scale = target_h / h
    new_w, new_h = int(w * scale), int(h * scale)
    resized[name] = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

combined = np.hstack(list(resized.values()))
cv2.imwrite(str(output_dir / "output_01_original_combined.jpg"), combined)
print(f"Saved combined original: {combined.shape}")

gray = cv2.cvtColor(combined, cv2.COLOR_BGR2GRAY)
cv2.imwrite(str(output_dir / "output_02_grayscale.jpg"), gray)
print("Saved grayscale")

median = cv2.medianBlur(gray, 5)
cv2.imwrite(str(output_dir / "output_03_median_filter.jpg"), median)
print("Saved median filter")

gaussian = cv2.GaussianBlur(median, (7, 7), 1.5)
cv2.imwrite(str(output_dir / "output_04_gaussian_blur.jpg"), gaussian)
print("Saved Gaussian blur")

sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], dtype=np.float32)

sharpened = cv2.filter2D(gaussian, -1, sharpen_kernel)
cv2.imwrite(str(output_dir / "output_05_sharpened.jpg"), sharpened)
print("Saved sharpened")

edges = cv2.Canny(sharpened, 45, 120)
cv2.imwrite(str(output_dir / "output_06_canny_edges.jpg"), edges)
print("Saved Canny edges")

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
cv2.imwrite(str(output_dir / "output_07_morph_closed.jpg"), closed)
print("Saved morphological closing")

contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
result = cv2.cvtColor(closed, cv2.COLOR_GRAY2BGR)
cv2.drawContours(result, contours, -1, (0, 255, 0), 2)
cv2.imwrite(str(output_dir / "output_08_final_contours.jpg"), result)
print("Saved final with contours")

overlay = combined.copy()
overlay_gray = cv2.cvtColor(overlay, cv2.COLOR_BGR2GRAY)
overlay_edges = cv2.Canny(cv2.GaussianBlur(cv2.medianBlur(overlay_gray, 5), (7, 7), 1.5), 45, 120)
overlay_edges = cv2.morphologyEx(overlay_edges, cv2.MORPH_CLOSE, kernel)
overlay[overlay_edges > 0] = [0, 255, 0]
cv2.imwrite(str(output_dir / "output_09_final_overlay.jpg"), overlay)
print("Saved final overlay")

print("\nPipeline complete. Outputs saved to output/")