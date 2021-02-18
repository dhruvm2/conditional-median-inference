# -*- coding: utf-8 -*-
"""
A script for generating the graph of $P^{\delta}$ seen in Figure 1 of [1].

[1] Dhruv Medarametla and Emmanuel Candès, "Distribution-Free Conditional Median Inference." 2021.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from google.colab import drive
drive.mount('/content/gdrive')

#datapoint_size = 5
datapoint_color = 'c'
datapoint_scale = 5.
datapoint_linewidth = 5

median_linewidth = 1
median_color = 'k'

title_fontsize = 16
label_fontsize = 14
text_fontsize = 15

text_loc = 0.3
diag_offset = 0.01
vert_offset = 0.02

alpha = 0.5

images_dir = '/content/gdrive/My Drive/Conditional Median Inference/'
dpi = 2000

X = [-0.5,0.5]
Y1 = [-0.5,0.5]
Y2 = [0,0]

plt.plot(X, Y1, color = datapoint_color, linewidth = datapoint_linewidth)
plt.plot(X, Y2, color = datapoint_color, linewidth = datapoint_linewidth, alpha = alpha)
plt.scatter([-0.5],[-0.5],color = datapoint_color, s = 1, label = 'Datapoints')
plt.plot(X, Y1, color = median_color, linewidth = median_linewidth, label = r"Conditional Median")
plt.legend(markerscale = datapoint_scale)

plt.text(text_loc - diag_offset,text_loc + diag_offset, s = r"$0.5 + \delta$", fontsize = text_fontsize, horizontalalignment = 'right', verticalalignment = 'bottom')
plt.text(-text_loc + diag_offset,-text_loc - diag_offset, s = r"$0.5 + \delta$", fontsize = text_fontsize, horizontalalignment = 'left', verticalalignment = 'top')
plt.text(text_loc,0 - vert_offset, s = r"$0.5 - \delta$", fontsize = text_fontsize, horizontalalignment = 'center', verticalalignment = 'top')
plt.text(-text_loc,0 + vert_offset, s = r"$0.5 - \delta$", fontsize = text_fontsize, horizontalalignment = 'center', verticalalignment = 'bottom')

plt.xlabel(r"$X$", fontsize = label_fontsize)
plt.ylabel(r"$Y$", fontsize = label_fontsize)
plt.title(r"$P^{\delta}$", fontsize = title_fontsize)


save_figs = True
if save_figs:
  filename = "P_delta.pdf"
  plt.savefig(images_dir + filename)


plt.show()