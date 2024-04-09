# Basic concept of Biomedical Image Processing

## DICOM
- Go check the [DICOMNote](./DICOMLearning/DICOMNote.md) for the details

## Concept of image processing
### 4 steps
<ol>
<li> Image Formation </li>
    All that helps forming a digital image matrix

<li> Image Visualisation </li>
    All types of manipulation of this matrix, resulting in an optimized output of the image.

<li> Image Analysis </li>
    All the steps of processing, which are used for quantitative measurements as well as abstract interpretations of biomedical images. Priori knowledge required
<li> Image Management </li>
    Efficient storage, communication, transmission, archiving, and access (retrieval) of image data.
</ol>

## Image Formation
### X-ray
- Not important
### CT
- Go check the [CTReconstructionNote.md](./CTReconstructionLearning/CTReconstructionNote.md) to see the code implementations
### MRI
- Go check the [MRIReconstructionNote.md](./MRIReconstructionLearning/MRIReconstructionNote.md) to see the code implementations
### UltraSound
- Not important

## Digitalisation
- discrete nature of the images.
### 2 Concepts
#### Quantization
- digitization of the value range.
#### Sampling 
- Sampling refers to the digitization of the definition range. <br>
- Remember the [**Nyquist theory**](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem)?

## Image Enhancement
### Histogram Transforms (point operations )
#### Histogram
#### Look-Up Table (LUT)
- a cheat sheet that rapidly transforms pixel values in an image.
### Convolution
#### Filtering
- Smoothing, Sharpening, Edge Detection, Texture analysis 

### Morphological Operations 
- Integral part of many operations in image analysis.
- erosion (based on logical AND of structel and binary image),
- dilation or dilatation (based on logical OR of structel and binary image),
- opening (erosion followed by dilatation using the same structel),
- closing (dilation followed by erosion using the same structel), and
- skeleton (e.g., by erosion with various structels).

### Calibration
- Device-specific but disregards the biological content captured, and thus, it is part of low-level processing methods.

### Registration
- Registration can be used to achieve an approximation of two or more images such that at least a change in measured dimensions can be quantified.
- See my [registration notebook](RegistrationLearning/imageRegistration.ipynb)
#### Unimodal Registration
- Focuses on aligning images of the same type.
#### Multi-Modal Registration
- Deals with aligning images of different modalities.

## Image Data Visualisation

## Segmentation
- dividing an image into connected regions. 
- By definition, the result of segmentation is always on the regional level of abstraction.
- Depending on the level of feature extraction as an input to the segmentation, we can methodically classify **pixel-, edge-, and texture- or region-oriented** procedures.<br>
### Pixel-Based Segmentation
- Only consider the gray scale or color value of current pixels disregarding its surroundings. 
- **Not** segmentation procedures in the strict sense of the definition.
- post-processing is **required**

#### Static Thresholding
Static thresholding is a simple and widely used image segmentation technique that divides an image into two regions: objects and background. It works by setting a threshold value and assigning each pixel to one of the two regions based on its intensity value.

**Algorithm:**

1. Choose a threshold value, T.
2. For each pixel in the image:
   - If the pixel's intensity value is greater than or equal to T, assign it to the object region.
   - Otherwise, assign it to the background region.

**Properties:**

* **simplicité:** Easy to implement and computationally inexpensive.
* **Flexibilité:** The threshold value can be adjusted to control the balance between object and background regions.
* **Robustness:** Relatively insensitive to noise in the image.

**Disadvantages:**

* **Sensitivity to image intensity:** The threshold value may need to be adjusted for different images with varying lighting conditions.
* **May produce only binary images:** Does not preserve intensity variations within the object and background regions.

#### Adaptive Thresholding
Adaptive thresholding is a technique used in image processing to determine the optimal threshold value for binarizing an image based on local image characteristics. Unlike global thresholding, which uses a single threshold value for the entire image, adaptive thresholding dynamically adjusts the threshold value based on the pixel neighborhood.


**Algorithm:**

The most commonly used adaptive thresholding algorithm is the **Sauvola's algorithm**. It calculates the threshold value for each pixel as follows:

```
T(x, y) = m(x, y) * (1 + k * (s(x, y) / R - 1))
```

where:

* T(x, y) is the threshold value at pixel (x, y)
* m(x, y) is the mean value of the pixel's neighborhood
* s(x, y) is the standard deviation of the pixel's neighborhood
* R is the dynamic range of the image (typically 255)
* k is a constant value (typically between 0.1 and 0.5)

**Steps:**

1. Calculate the mean and standard deviation of a circular or rectangular neighborhood around each pixel.
2. Adjust the threshold value based on the formula above.
3. Use the threshold value to binarize the image.

***Advantages of Adaptive Thresholding***

* **Local adaptation:** Adjusts the threshold value based on local image variations, resulting in better results for non-uniform images.
* **Noise resilience:** Less sensitive to noise than global thresholding, especially in low-contrast regions.
* **Object segmentation:** Can effectively separate objects from the background even in complex images.

***Disadvantages of Adaptive Thresholding***

* **Computational cost:** Can be slower than global thresholding due to the computation of local statistics.
* **Parameter sensitivity:** The choice of the neighborhood size, shape, and constant value can impact the results.
* **Edge detection:** May not be suitable for edge detection tasks, as it can smooth out edges.



#### Clustering (**Otsu's method:)

### Edge-Based Segmentation
#### Livewire Segmentation

### Region-Based Segmentation
#### Agglomerative Algorithm
#### Divisive Algorithm

### Deep Learning Based Segmentation 

## Image Analysis
### Quantitative measurements
- Measurements of length, area, volume, angles, density, etc.
### Abstract interpretations
- Detection and classification of objects (e.g., tumors, organs),
- Evaluation of disease progression,
- Identification of anatomical structures and their relationships,
- Analysis of dynamic processes (e.g., blood flow, heart motion)

## Image Management
- Storage: Efficient storage of large image datasets on various media (e.g., hard drives, cloud storage)
- Communication: Transmission of images between different systems and devices (e.g., PACS, telemedicine)
- Archiving: Long-term preservation and accessibility of image data
- Retrieval: Fast and efficient searching and accessing of specific images or sets of images based on various criteria (e.g., patient ID, study date, image type).## Feature extraction   
- Generate features which are useful for other medical tasks (classification, regression,..)
- Examples: Texture feature, Shape feature,  
### Classification   
- Machine Learning tools 



