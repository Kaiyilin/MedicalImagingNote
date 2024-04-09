# Basic concept of Biomedical Image Processing

## DICOM
* Go check the [DICOMNote](./DICOMLearning/DICOMNote.md) for the details

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
* Not important
### CT
* Go check the [CTReconstructionNote.md](./CTReconstructionLearning/CTReconstructionNote.md) to see the code implementations
### MRI
* Go check the [MRIReconstructionNote.md](./MRIReconstructionLearning/MRIReconstructionNote.md) to see the code implementations
### UltraSound
* Not important

## Digitalisation
* discrete nature of the images.
### 2 Concepts
#### Quantization
* digitization of the value range.
#### Sampling 
* Sampling refers to the digitization of the definition range. <br>
* Remember the [**Nyquist theory**](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem)?

## Image Enhancement
### Histogram Transforms (point operations )
#### Histogram
#### Look-Up Table (LUT)
* a cheat sheet that rapidly transforms pixel values in an image.
### Convolution
#### Filtering
* Smoothing, Sharpening, Edge Detection, Texture analysis 

### Morphological Operations 
* Integral part of many operations in image analysis.
* erosion (based on logical AND of structel and binary image),
* dilation or dilatation (based on logical OR of structel and binary image),
* opening (erosion followed by dilatation using the same structel),
* closing (dilation followed by erosion using the same structel), and
* skeleton (e.g., by erosion with various structels).

### Calibration
* Device-specific but disregards the biological content captured, and thus, it is part of low-level processing methods.

### Registration
* Registration can be used to achieve an approximation of two or more images such that at least a change in measured dimensions can be quantified.
#### Unimodal Registration
* Focuses on aligning images of the same type.
#### Multi-Modal Registration
* Deals with aligning images of different modalities.

## Segmentation 
### Thresholding 
### Clustering 
### Region growing 
### Morphometry 
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
* Generate features which are useful for other medical tasks (classification, regression,..)
* Examples: Texture feature, Shape feature,  
### Classification   
* Machine Learning tools 
## Image Registration   
* Is the process of aligning two or more images of the same scene that have been taken at different times, from different viewpoints, and/or by different sensors.
* See my [registration notebook](RegistrationLearn/imageRegistration.ipynb)
