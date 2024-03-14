import cv2
import numpy as np
from numpy import asarray
import matplotlib.pyplot as plt
import glob
from mpl_toolkits.mplot3d import Axes3D
from scipy import ndimage

# THESE LINES OF CODE NEEDS AN ARRAY OF SPECIFIC CAPTURED PICTURES TO WORK. 
# I CANNOT UPLOAD THEM BUT FEEL FREE TO ASK FOR MORE INFO AND PICTURE SAMPLES

# this program takes a bunch of pictures with varying focus and makes a 3D Plot of the most in-focus pixels of the images array
# then it saves a file with the data in grayscale to use as you like
# ATTENTION: the z axis is in pictures order but after the extraction of the file it reads them as grayscale level. you should keep it in mind...


# read the images in .bmp format at this directory and makes them a list
images = [cv2.imread(image, 0) for image in glob.glob(r"D:\Sample_Images\*.bmp")]
y = images[0].shape[0]  # y axis length
x = images[0].shape[1]  # x axis length

fft = input(print("Do you want Butterworth highpass filter to your images:"))
fft.lower()

if fft == "yes":
    F1 = np.fft.fft2(images)  # fourier image transformation
    F2 = np.fft.fftshift(F1)  # shift the low freq in the center
    print(F2.shape)

    h = np.zeros((y, x), )  # filter map
    d0 = 80                 # filter size (adjust accordingly)

    # making of filter map
    for u in range(y):
        for v in range(x):
            d = np.sqrt((u - (y / 2)) ** 2 + (v - (x / 2)) ** 2)
            h[u, v] = 1-(1/(1+((d/d0)**4)))


   
    Fhighpass = [i * h for i in F2]      # filtered image

    G1 = np.fft.ifftshift(Fhighpass)     # shift high freq in the center
    G2 = np.fft.ifft2(G1)                # real image from fourier transformation

    array = np.array(G2)                 # takes the list and turns it into an array
    image_arr = np.array(array)          # takes each item of the array and turns it into array, shortly pixels
    stack = np.stack(image_arr)          # takes each pixelated array and stacks it in 3rd dimension

print(stack.shape)                       # checking if the matrix dimension is what we aimed for (z,y,x)

# choose how many squared pixels will be added for the algorithm
gap = 5
gap2 = 10
threshold = 0

# create a standard deviation map, the size of our stack with zero values
std_map = np.zeros((int(stack.shape[0]), int(stack.shape[1] / gap), int(stack.shape[2] / gap)))

# extract values for the std_map and map them
for i in range(gap2, 1200, gap):
    for j in range(gap2, 1920, gap):
        for k in range(int(stack.shape[0])):
            sub_arr = stack[k, i - gap2:i + gap2, j - gap2:j + gap2]
            std = np.std(sub_arr)
            a = int(i / gap)
            b = int(j / gap)
            std_map[k, a, b] = std

            # If the standard deviation is below the threshold, select the first image in an image array
            # this way we eliminate the noise from our 3D plot
            if std_map[k, a, b] < threshold:
                 std_map[k, a, b] = std_map[0, a, b] - 0.000001*k
            else:
                 std_map[k, a, b] = std_map[k, a, b]

print(std_map.shape)
prof = np.nanargmax(std_map, 0)            # returns the maximum index of z axis
print(prof.shape)
print(prof)

# Visualization
# set x y z values
x1 = np.linspace(0, prof.shape[1], prof.shape[1])
y1 = np.linspace(0, prof.shape[0], prof.shape[0])
x, y = np.meshgrid(x1, y1)

for i in x1:
    for j in y1:
        z = 1800 + (50 * prof[:][:])

x2 = [int(i) for i in [i * gap for i in x1]]
y2 = [int(i) for i in [i * gap for i in y1]]

# set 3D projection and plot appearance details
fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(8, 5))
ax.plot_surface(x, y, z, cmap='coolwarm', linewidth=10, antialiased=False)
ax.set_title('3D Surface Plot', fontsize=15)


ax.set_xticks(x1[::100])
ax.set_xticklabels([int(i) for i in x1[::100]])
ax.set_yticks(y1[::50])
ax.set_yticklabels([int(i) for i in y1[::50]])
ax.tick_params(axis='both', labelsize=8)
ax.tick_params(axis='z', which='major', labelsize=8)

ax.set_xlabel('X [pixels]', fontsize=10)
ax.set_ylabel('Y [pixels]')
ax.set_zlabel('Height [μm]')

plt.show()

# Save the data exported into a file
if fft == "yes":
    np.savetxt("3D_StdDev_Image [" + str(gap) + "]-[" + str(gap2) + "], B[" + str(d0) + "], T[" + str(threshold) + "].txt", prof)
else:
    np.savetxt("3D_StdDev_Image [" + str(gap) + "]-[" + str(gap2) + "].txt", prof)
