import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Transformation 1
# Probability: 0.01
trans_1 = lambda x, y: (0.,
                        0.16 * y)
trans_1_proba = 0.01

# Transformation 2
# Probability: 0.85
trans_2 = lambda x, y: (0.85 * x + 0.04 * y,
                        -0.04 * x + 0.85 * y + 1.6)
trans_2_proba = 0.85

# Transformation 3
# Probability: 0.07
trans_3 = lambda x, y: (0.2 * x - 0.26 * y,
                        0.23 * x + 0.22 * y + 1.6)
trans_3_proba = 0.07

# Transformation 4
# Probability: 0.07
trans_4 = lambda x, y: (-0.15 * x + 0.28 * y,
                        0.26 * x + 0.24 * y + 0.44)
trans_4_proba = 0.07

transformations = [trans_1, trans_2, trans_3, trans_4]
transformation_proba = [trans_1_proba, trans_2_proba, trans_3_proba, trans_4_proba]

# canvas width and height
width, height = 1200, 1200

# number of points to plot
num_points = width * height

# fill image with zeros
image = np.zeros((width, height))

# set start points
x, y = 0, 0

for i in range(num_points):
    # Choose a transformation with defined probabilities
    current_trans = np.random.choice(transformations,
                                     p=transformation_proba)

    # change current point
    x, y = current_trans(x, y)

    # map transformation to image pixels
    pix_y, pix_x = int(width / 2 + x * width / 10),int(y * height / 11)

    # color pixel in image
    image[pix_x, pix_y] = 1

# plot image
plt.imshow(image[::-1, :], cmap=cm.viridis)
plt.show()
