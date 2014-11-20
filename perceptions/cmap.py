'''
Colormaps are plotted in categories as in the original matplotlib gallery.
'''


from skimage import color
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib as mpl

mpl.rcParams.update({'font.size': 14})
mpl.rcParams['font.sans-serif'] = ('Arev Sans, Bitstream Vera Sans, '
                                   'Lucida Grande, Verdana, Geneva, Lucid, '
                                   'Helvetica, Avant Garde, sans-serif')
mpl.rcParams['mathtext.fontset'] = 'custom'
mpl.rcParams['mathtext.cal'] = 'cursive'
mpl.rcParams['mathtext.rm'] = 'sans'
mpl.rcParams['mathtext.tt'] = 'monospace'
mpl.rcParams['mathtext.it'] = 'sans:italic'
mpl.rcParams['mathtext.bf'] = 'sans:bold'
mpl.rcParams['mathtext.sf'] = 'sans'
mpl.rcParams['mathtext.fallback_to_cm'] = 'True'


# Have colormaps separated into categories:
# http://matplotlib.org/examples/color/colormaps_reference.html

cmaps = [('Sequential', ['binary', 'Blues', 'BuGn', 'BuPu', 'gist_yarg',
                         'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd', 'PuBu',
                         'PuBuGn', 'PuRd', 'Purples', 'RdPu', 'Reds', 'YlGn',
                         'YlGnBu', 'YlOrBr', 'YlOrRd']),
         ('Sequential2', ['afmhot', 'autumn', 'bone', 'cool', 'copper',
                          'gist_gray', 'gist_heat', 'gray', 'hot', 'pink',
                          'spring', 'summer', 'winter']),
         ('Diverging', ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
                        'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'seismic',
                        'Spectral']),
         ('Qualitative', ['Accent', 'Dark2', 'hsv', 'Paired', 'Pastel1',
                          'Pastel2', 'Set1', 'Set2', 'Set3']),
         ('Miscellaneous', ['gist_earth', 'gist_ncar', 'gist_rainbow',
                            'gist_stern', 'jet', 'brg', 'CMRmap', 'cubehelix',
                            'gnuplot', 'gnuplot2', 'ocean', 'rainbow',
                            'terrain', 'flag', 'prism', 'nipy_spectral'])]

# indices to step through colormap
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

# In the following, the number of rows is hard-coded to the value used in the
# original plots, so that adding new rows does not change the plot too much.
nrows = 20  # max(len(cmap_list) for cmap_category, cmap_list in cmaps)
height = 6  # Default in matplotlib
top_space = 0.05 * height
bottom_space = 0.01 * height
row_height = (height - top_space - bottom_space) / nrows


def plot_color_gradients(cmap_category, cmap_list):
    nrows = len(cmap_list)
    width = 8
    height = row_height * nrows + top_space + bottom_space
    fig, axes = plt.subplots(nrows=nrows, ncols=1, figsize=(width, height))
    fig.subplots_adjust(top=1-top_space/height, bottom=bottom_space/height,
                        left=0.2, right=0.99, wspace=0.05)
    fig.suptitle(cmap_category + ' colormaps', fontsize=14, y=1.0, x=0.6)

    for ax, name in zip(axes, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3] / 2.0
        fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()
    fig.savefig('figures/' + cmap_category + '.png', dpi=100,
                bbox_inches='tight')
    plt.close(fig)


for cmap_category, cmap_list in cmaps:
    plot_color_gradients(cmap_category, cmap_list)
