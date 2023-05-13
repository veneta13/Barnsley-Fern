import base64
import os

import imageio as imageio
import matplotlib.pyplot as plt
import streamlit as st

from barnsley_fern import barnsley_fern

st.set_page_config(
    page_title='Barnsley Fern Generator',
    page_icon=':herb:',
    layout='wide'
)

color_map = 'YlGn'


def create_gif(size):
    def animate(points, size):
        ax = plt.axes()

        ax.clear()  # clear axes object
        ax.set_xticks([], [])  # clear x-axis ticks
        ax.set_yticks([], [])  # clear y-axis ticks

        fractal = barnsley_fern(points, size, size)

        img = ax.imshow(fractal[::-1, :], interpolation="bicubic", cmap=color_map)
        return img

    filenames = []

    for points in [2_000, 5_000, 10_000, 20_000, 50_000, 100_000, 200_000, 300_000, 400_000, 500_000, 700_000]:
        points = (points * size) // 6000
        plt.figure(figsize=(10, 10), dpi=300)
        animate(points, size)
        filename = f'frame_{points}.jpg'
        print(filename)
        plt.savefig(filename, bbox_inches='tight')
        filenames.append(filename)
        plt.close()

    with imageio.get_writer('barnsley_fern.gif', mode='I', fps=5) as writer:
        for filename in filenames:
            image = imageio.v2.imread(filename)
            writer.append_data(image)

    for filename in filenames:
        os.remove(filename)


col1, col2 = st.columns(2, gap='large')

with col1:
    st.write("# Animation🌿")
    st.write("##")

    size_px = st.slider('Image size (px)', value=300, min_value=200, max_value=3000, step=10)

    color_map = st.selectbox(
        'Select color scheme',
        options=[
            'YlGn', 'viridis', 'terrain', 'spring', 'summer', 'autumn', 'winter',
            'gist_ncar', 'nipy_spectral', 'ocean', 'magma', 'seismic', 'gist_stern'
        ]
    )

with col2:
    try:
        create_gif(size_px)
        img_path = os.getcwd() + '\\barnsley_fern.gif'

        file_ = open("barnsley_fern.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="Barnsley Fern GIF" width=80% '
            f'style="display:block;margin:0 auto;">',
            unsafe_allow_html=True,
        )
    except IndexError:
        st.error('Image size is invalid, please enter another one.', icon='⚠️')
