import base64
import os

import streamlit as st

import imageio as imageio
import matplotlib.pyplot as plt

from barnsley_fern import barnsley_fern

st.set_page_config(
    page_title='Barnsley Fern Generator',
    page_icon=':herb:',
    layout='wide'
)

# canvas width and height
width, height = 1200, 1200


def create_gif():
    def animate(points):
        ax = plt.axes()

        ax.clear()  # clear axes object
        ax.set_xticks([], [])  # clear x-axis ticks
        ax.set_yticks([], [])  # clear y-axis ticks

        fractal = barnsley_fern(points, width, height)

        img = ax.imshow(fractal[::-1, :], interpolation="bicubic", cmap='viridis')
        return img

    # number of points to plot
    max_num_points = width * height

    image = None

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

############################################## Main app ##############################################
col1, col2 = st.columns(2, gap='large')

with col1:
    st.write("##")

with col2:
    try:
        create_gif()
        img_path = os.getcwd() + '\\barnsley_fern.gif'

        file_ = open("barnsley_fern.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif" width=80% style="display:block;margin:0 auto;">',
            unsafe_allow_html=True,
        )
    except IndexError:
        st.error('Image size is invalid, please enter another one.', icon='⚠️')
