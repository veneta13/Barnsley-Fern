import streamlit as st
from matplotlib import pyplot as plt

from barnsley_fern import barnsley_fern

st.set_page_config(
    page_title='Barnsley Fern Generator',
    page_icon=':herb:',
    layout='wide'
)


def higher_order(trans, tau):
    return lambda x, y: trans(x, y, tau)


# Transformation 1
# Probability: 0.01
# Tau: -0.5 < tau < 0.5
trans_1 = lambda x, y: (0.,
                        0.16 * y)

trans_1_new = lambda x, y, tau: (tau * x,
                                 .16 * y)
trans_1_proba = 0.01

# Transformation 2
# Probability: 0.85
# Tau: -0.01 < tau < 0.09
trans_2 = lambda x, y: (0.85 * x + 0.04 * y,
                        -0.04 * x + 0.85 * y + 1.6)
trans_2_new = lambda x, y, tau: (0.85 * x + tau * y,
                                 -0.04 * x + 0.85 * y + 1.6)
trans_2_proba = 0.85

# Transformation 3
# Probability: 0.07
# Tau: -0.5 < tau < 0.5
trans_3 = lambda x, y: (0.2 * x - 0.26 * y,
                        0.23 * x + 0.22 * y + 1.6)
trans_3_new = lambda x, y, tau: (0.2 * x - 0.26 * y + tau,
                                 0.23 * x + 0.22 * y + 1.6)
trans_3_proba = 0.07

# Transformation 4
# Probability: 0.07
# Tau: -0.5 < tau < 0.5
trans_4 = lambda x, y: (-0.15 * x + 0.28 * y,
                        0.26 * x + 0.24 * y + 0.44)
trans_4_new = lambda x, y, tau: (-0.15 * x + 0.28 * y + tau,
                                 0.26 * x + 0.24 * y + 0.44)
trans_4_proba = 0.07

st.title("Experimental Transformations 🌿")

col1, col2 = st.columns(2, gap='large')

with col1:
    st.write("##")

    size_px = st.slider('Image size (px)', value=500, min_value=200, max_value=2000, step=10)
    num_points = st.select_slider('Number of points', value=10_000, options=[10 ** x for x in [*range(1, 7)]])

    st.write("###")

    col1_1, col1_2 = st.columns(2, gap='small')
    with col1_1:
        f1_tau = st.slider(label='f1 tau', value=0., min_value=-0.5, max_value=0.5, step=0.01, key=1)

    with col1_2:
        st.latex('f_1(P) = \\begin{bmatrix} \\tau &0 \\\\ 0 &0.16 \\end{bmatrix}P + \\begin{bmatrix} 0 \\\\ 0 \\end{'
                 'bmatrix}')

    col2_1, col2_2 = st.columns(2, gap='small')
    with col2_1:
        f2_tau = st.slider('f2 tau', value=0.04, min_value=-0.01, max_value=0.09, step=0.001, key=2)
    with col2_2:
        st.latex('f_2(P) = \\begin{bmatrix} 0.85 & \\tau \\\\ -0.04 &0.85 \\end{bmatrix}P + \\begin{bmatrix} 0 \\\\ 1.6'
                 '\\end{bmatrix}')

    col3_1, col3_2 = st.columns(2, gap='small')
    with col3_1:
        f3_tau = st.slider('f3 tau', value=0., min_value=-0.5, max_value=0.5, step=0.01, key=3)
    with col3_2:
        st.latex('f_3(P) = \\begin{bmatrix} 0.2 &-0.26 \\\\ 0.23 &0.22 \\end{bmatrix}P + \\begin{bmatrix} \\tau \\\\ '
                 '1.6 \\end{bmatrix}')

    col4_1, col4_2 = st.columns(2, gap='small')
    with col4_1:
        f4_tau = st.slider('f4 tau', value=0., min_value=-0.5, max_value=0.5, step=0.01, key=4)
    with col4_2:
        st.latex('f_4(P) = \\begin{bmatrix} -0.15 &0.28 \\\\ 0.26 &0.24 \\end{bmatrix}P + \\begin{bmatrix} \\tau \\\\ '
                 '0.44 \\end{bmatrix}')

transformations = [
    higher_order(trans_1_new, f1_tau),
    higher_order(trans_2_new, f2_tau),
    higher_order(trans_3_new, f3_tau),
    higher_order(trans_4_new, f4_tau)
]

with col2:
    fig, ax = plt.subplots()

    ax.clear()
    ax.set_xticks([], [])
    ax.set_yticks([], [])

    plt.figure(dpi=300)

    st.write("#")

    try:
        img = ax.imshow(barnsley_fern(num_points, size_px, size_px, transformations=transformations)[::-1, :],
                        interpolation="bicubic", cmap='summer')
        st.pyplot(fig)
    except IndexError:
        st.error('Image size is invalid, please enter another one.', icon='⚠️')
