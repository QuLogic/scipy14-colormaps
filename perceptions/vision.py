'''
Apply various vision deficiency approximations to colormaps.
'''


import numpy as np
from skimage import color, io


cmaps = ['Sequential', 'Sequential2', 'Diverging', 'Qualitative',
         'Miscellaneous']

protanopia = np.array([
    [0.567, 0.433, 0.0],
    [0.558, 0.442, 0.0],
    [0.0,   0.242, 0.758],
])

protanomaly = np.array([
    [0.817, 0.183, 0.0],
    [0.333, 0.667, 0.0],
    [0.0,   0.125, 0.875],
])

deuteranopia = np.array([
    [0.625, 0.375, 0.0],
    [0.7,   0.3,   0.0],
    [0.0,   0.3,   0.7],
])

deuteranomaly = np.array([
    [0.8,   0.2,   0.0],
    [0.258, 0.742, 0.0],
    [0.0,   0.142, 0.858],
])

tritanopia = np.array([
    [0.95, 0.05,  0.0],
    [0.0,  0.433, 0.567],
    [0.0,  0.475, 0.525],
])

tritanomaly = np.array([
    [0.967, 0.033, 0.0],
    [0.0,   0.733, 0.267],
    [0.0,   0.183, 0.817],
])

achromatopsia = np.array([
    [0.299, 0.587, 0.114],
    [0.299, 0.587, 0.114],
    [0.299, 0.587, 0.114],
])

achromatomaly = np.array([
    [0.618, 0.320, 0.062],
    [0.163, 0.775, 0.062],
    [0.163, 0.320, 0.516],
])

for name in cmaps:
    data = io.imread('figures/' + name + '.png')

    data[:,:,:3] = np.dot(data[:,:,:3], deuteranopia.T)

    io.imsave('figures/' + name + 'Deuteranopia.png', data)
