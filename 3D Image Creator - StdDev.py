import cv2
import numpy as np
from numpy import asarray
import matplotlib.pyplot as plt
import glob
from mpl_toolkits.mplot3d import Axes3D
from scipy import ndimage

# this program takes a bunch of pictures with varying focus and makes a 3D Plot of the most in-focus pixels of the images array
# then it saves a file with the data in grayscale to use as you like
# ATTENTION: the z axis is in pictures order but after the extraction of the file it reads them as grayscale level. you should keep it in mind


# reads the images in .bmp format at this directory and makes them a list
images = [cv2.imread(image, 0) for image in glob.glob(r"D:\Users\Lor Studio\Desktop\Archive\Mina\Lor MSc\Lab\Lab\22_11_21 (the best rusty)\rustyball\*.bmp")]
y = images[0].shape[0]  # y axis length
x = images[0].shape[1]  # x axis length

fft = input(print("Do you want Butterworth filter to your images:"))
fft.lower()

if fft == "yes":
    F1 = np.fft.fft2(images)  # fourier image
    F2 = np.fft.fftshift(F1)  # low freq in the center
    print(F2.shape)

    h = np.zeros((y, x), )  # filter map
    d0 = 80                 # filter size

    # making of filter map
    for u in range(y):
        for v in range(x):
            d = np.sqrt((u - (y / 2)) ** 2 + (v - (x / 2)) ** 2)
            h[u, v] = 1-(1/(1+((d/d0)**4)))


    # filtered image
    Fhighpass = [i * h for i in F2]

    G1 = np.fft.ifftshift(Fhighpass)     # high freq in the center
    G2 = np.fft.ifft2(G1)                # real image from fourier transformation

    array = np.array(G2)                 # takes the list and turns it into an array
    image_arr = np.array(array)          # takes each item of the array and turns it into array, shortly pixels
    stack = np.stack(image_arr)          # takes each pixelated array and stacks it in 3rd dimension

print(stack.shape)                       # here we can check if the matrix dimension is what we aimed for (z,y,x)

# I choose how many squared pixels will be added for the algorithm
gap = 5
gap2 = 10
threshold = 0

# create a standard deviation map, the size of our stack with zero values
std_map = np.zeros((int(stack.shape[0]), int(stack.shape[1] / gap), int(stack.shape[2] / gap)))

# I extract values for the std_map and name them
for i in range(gap2, 1200, gap):
    for j in range(gap2, 1920, gap):
        for k in range(int(stack.shape[0])):
            sub_arr = stack[k, i - gap2:i + gap2, j - gap2:j + gap2]
            std = np.std(sub_arr)
            a = int(i / gap)
            b = int(j / gap)
            std_map[k, a, b] = std

            # If the standard deviation is below the threshold, select the first image in an image array
            if std_map[k, a, b] < threshold:
                 std_map[k, a, b] = std_map[0, a, b] - 0.000001*k
            else:
                 std_map[k, a, b] = std_map[k, a, b]

print(std_map.shape)
prof = np.nanargmax(std_map, 0)            # returns the maximum index of z axis
print(prof.shape)
print(prof)


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
ax.plot_surface(x, y, z, cmap='coolwarm', linewidth=20, antialiased=False)
ax.set_title('3D Surface Plot', fontsize=15)

ax.set_xticks(x1, x2, fontsize=6, ha='left', color='blue')
ax.set_yticks(y1, y2, fontsize=6, ha='left', color='purple')
ax.tick_params(axis='x', pad=3)
ax.tick_params(axis='y', pad=3)
ax.tick_params(axis='z', which='major', labelsize=8)

ax.set_xlabel('X [pixels]', fontsize=10)
ax.set_ylabel('Y [pixels]')
ax.set_zlabel('Height [μm]')
plt.show()


if fft == "yes":
    np.savetxt("3D_StdDev_slope_3 [" + str(gap) + "]-[" + str(gap2) + "], B[" + str(d0) + "], T[" + str(threshold) + "].txt", prof)
else:
    np.savetxt("3D_StdDev_fixed_tissue1 [" + str(gap) + "]-[" + str(gap2) + "].txt", prof)
