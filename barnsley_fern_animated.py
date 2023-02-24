import os

import imageio as imageio
import matplotlib.pyplot as plt

from barnsley_fern import barnsley_fern


def animate(points):
    ax = plt.axes()

    ax.clear()  # clear axes object
    ax.set_xticks([], [])  # clear x-axis ticks
    ax.set_yticks([], [])  # clear y-axis ticks

    fractal = barnsley_fern(points, width, height)

    img = ax.imshow(fractal[::-1, :], interpolation="bicubic", cmap='viridis')
    return img


if __name__ == '__main__':

    # canvas width and height
    width, height = 1200, 1200

    # number of points to plot
    max_num_points = width * height

    filenames = []

    for points in [2_000, 5_000, 10_000, 20_000, 50_000, 100_000, 200_000, 300_000, 400_000, 500_000, 700_000]:
        plt.figure(figsize=(10, 10), dpi=300)
        animate(points)
        filename = f'frame_{points}.jpg'
        plt.savefig(filename, bbox_inches='tight')
        filenames.append(filename)
        plt.close()

    with imageio.get_writer('barnsley_fern.gif', mode='I', fps=5) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)

    for filename in set(filenames):
        os.remove(filename)
