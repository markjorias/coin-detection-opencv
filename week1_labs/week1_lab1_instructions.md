# Laboratory Activity 1: Coin Detection

## Objective
Use convolution, spatial filtering, and edge detection techniques to process images of Philippine coins from the provided dataset and generate a clean edge-detected result where the coins forming **₱21.10** can be clearly identified.

This activity demonstrates how convolutional filters highlight boundaries and suppress noise in digital image processing.

---

## Dataset
Use the coin images from the provided dataset:

- **Dataset Folder:** [Google Drive Folder](https://drive.google.com/drive/folders/1vcuIU2rPh72d7wJWrpvklLmTvRodnpDH)

> **Note:** Do not capture new images. Only use images from this dataset.

---

## Task Overview
Using the images from the dataset, select coins that add up to: **₱21.10**

Your goal is to process the selected coin images so that:
- The edges of the coins are clear
- The denominations can still be recognized
- The total amount can be visually verified

---

## Activity Steps

### 1. Select Images: Loading and Displaying the Selected Coins (5 pts)
From the dataset:
1. Choose the coins needed to make **₱21.10**.

### 2. Pre-Processing
Prepare the image for filtering.

Recommended preprocessing steps:
1. Convert to Grayscale
2. Apply Noise Reduction:
   - Median Filter
   - Gaussian Blur

### 3. Apply Convolution
Students must apply a convolution operation using a filter kernel.

Example kernels students may use:
- Sharpening Filter

### 4. Perform Edge Detection
Apply an edge detection technique.

### 5. Clean the Result
Post-process the result to ensure:
- Minimal noise
- Clear circular coin edges
- Visible coin markings (**A MUST**)

---

## Expected Output
Students must submit the following:
1. Original combined coin image
2. Grayscale / filtered image
3. Convolution result
4. Final edge-detected output

*The final output should clearly show coins totaling **₱21.10**, with clean, well-defined edges.*

---

## Submission Requirements
- **Output images**
- **Short explanation of:**
  - Kernel used
  - Convolution process
  - Edge detection method
  - How the result was improved
- **Submission Link:** [Submit Here via Google Forms](https://forms.gle/3JTdFgy4Q81r13Pi7)

---

## Reference Code
- [Convolution_Sample_Codes.ipynb](file:///home/asriyo/Repositories/csec5-projects/week1_labs/Convolution_Sample_Codes.ipynb)
