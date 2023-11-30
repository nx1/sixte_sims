import matplotlib.pyplot as plt
from astropy.table import Table
from matplotlib.animation import FuncAnimation

tab = Table.read('./rsp_files/athena_wfi_rib2.3_B4C_20210218_wo_filter_OnAxis.rsp')
print(tab)

y_maxes = []
energies = []
def animate(i):
    y = tab[i]['MATRIX']
    E_lo = tab[i]['ENERG_LO']
    E_hi = tab[i]['ENERG_HI']
    line1.set_data(range(len(y)), y)
    y_max = max(y)
    energies.append(E_lo)
    y_maxes.append(y_max)
    ax[0].set_title(f'CHANNEL={i} | ENERGY={E_lo:.2f} - {E_hi:.2f} keV')
    line2.set_data(energies, y_maxes)
    line3.set_ydata([y_max, y_max])
    return line1,line2, line3, ax[0], ax[1]

fig, ax = plt.subplots(1,2,figsize=(10,5), sharey=True)
line1, = ax[0].plot([], [])
line2, = ax[1].plot([1], [1])
line3 = ax[0].axhline(0, ls='--', lw=0.5, color='red')
ax[0].set_xlim(0,180)
ax[0].set_ylim(0,2500)
ax[1].set_xlim(0,15)
ax[1].set_ylim(0,2500)
ax[1].set_xlabel('Energy (keV)')
ax[0].set_ylabel('Response')

plt.subplots_adjust(wspace=0)
anim = FuncAnimation(fig, animate, interval=30, frames=len(tab))
plt.show()
