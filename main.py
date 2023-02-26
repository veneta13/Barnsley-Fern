import streamlit as st
from matplotlib import pyplot as plt, cm

from barnsley_fern import barnsley_fern

st.set_page_config(
    page_title='Barnsley Fern Generator',
    page_icon=':herb:',
)

st.title("Barnsley Fern Generator 🌿")

num_points = st.select_slider('Number of points', value=10_000, options=[10 ** x for x in [*range(1, 7)]])

width = st.slider('Image width (px)', value=500, min_value=200, max_value=2000, step=10)
height = st.slider('Image height (px)', value=500, min_value=200, max_value=2000, step=10)

color_map = st.selectbox(
    'Select color scheme',
    options=[
        'YlGn', 'viridis', 'terrain', 'spring', 'summer', 'autumn', 'winter',
        'gist_ncar', 'nipy_spectral',  'ocean', 'magma', 'seismic', 'gist_stern'
    ]
)

fig, ax = plt.subplots()

ax.clear()
ax.set_xticks([], [])
ax.set_yticks([], [])

plt.figure(dpi=300)

try:
    img = ax.imshow(barnsley_fern(num_points, width, height)[::-1, :], interpolation="bicubic", cmap=color_map)
    st.pyplot(fig)
except IndexError:
    st.error('Image size is invalid, please enter another one.', icon='⚠️')
