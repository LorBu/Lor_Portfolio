# 3D Surface Plot Generation from Focus-Varying Images
## Overview
This project involves the generation of a 3D surface plot from a series of images with varying focus. By analyzing the standard deviation of pixel intensities across multiple images, we identify the most in-focus pixels and plot them in a 3D space. The primary objective is to visualize the surface profile of an object captured through these images.

## Optical Engineering Aspect
The initial phase of the project involves optical engineering tasks, which are essential for capturing the series of photos with varying focus. This aspect is considered beyond the scope of this project and is assumed to have been addressed separately.

## Features
* **Image Processing**: Utilizes OpenCV and NumPy for image loading, manipulation, and processing.
* **Standard Deviation Mapping**: Computes the standard deviation of pixel intensities within small regions across all images to create a 3D map.
* **Surface Plot Generation**: Utilizes Matplotlib's 3D plotting capabilities to visualize the surface profile.
* **Butterworth Filter (Optional)**: Offers an option to apply a Butterworth filter to the images for frequency domain processing.

## Usage
1. **Image Loading**: Ensure all images are stored in the specified directory and are in the .bmp format.
2. **Run the Script**: Execute the script to generate the 3D surface plot. Optionally, choose whether to apply a Butterworth filter to the images.
3. **View the Plot**: The generated plot will display the surface profile of the object captured in the images.

## File Structure
* **'3D_Surface_Plot_Generation.py'**: Python script containing the code for processing and plotting.
* **'README.md'**: Documentation providing an overview, usage instructions, and details about the project.
* **'Sample_Images/'**: Directory containing sample images used for testing.
* **'3D_StdDev_Data/'**: Directory to store output data files generated during processing.

## Requirements
* Python 3.x
* OpenCV
* NumPy
* Matplotlib

## Notes
* The z-axis of the generated plot represents the order of images processed, with lower values further focus.
* Data files containing the z-axis values of the in-focus pixels are saved for further analysis or visualization.

## Future Enhancements
* Implementation of additional image processing techniques for improved surface reconstruction.
* Integration of interactive features into the generated plot for enhanced user experience.
