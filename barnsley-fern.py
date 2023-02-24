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
