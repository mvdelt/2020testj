
# https://matplotlib.org/3.2.1/gallery/subplots_axes_and_figures/gridspec_multicolumn.html

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib as mpl


def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

fig = plt.figure(constrained_layout=True)

gs = GridSpec(3, 4, figure=fig)
ax1 = fig.add_subplot(gs[0, :])
# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])

fig.suptitle("GridSpec")
format_axes(fig)

# i. colorbar 적용 테스트.
fig.colorbar(mpl.cm.ScalarMappable(norm=None, cmap=None), cax=None, ax=ax1, use_gridspec=True)
fig.colorbar(mpl.cm.ScalarMappable(norm=None, cmap=None), cax=None, ax=ax2, use_gridspec=True)
# fig.colorbar(mpl.cm.ScalarMappable(norm=None, cmap=None), cax=None, ax=ax5, use_gridspec=True)
# fig.colorbar(mpl.cm.ScalarMappable(norm=None, cmap=None), cax=ax1, ax=[ax1,ax2,ax3,ax4,ax5], use_gridspec=False)

plt.show()