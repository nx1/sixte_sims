import xspec
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from astropy.table import Table

from pha_files import pha_counts, pha_rate_psf_wo

# Convert .xcm to pyxspec .xcm
# xspec.Xset.restore(fileName='./athenabkg.xcm')
# xspec.Xset.save(fileName='athenabkg_pyxspec.xcm')

# Read xcm file
xspec.Xset.restore(fileName='./athenabkg_pyxspec.xcm')

# Plot data in /xw
xspec.Plot.device = '/xw'
xspec.Plot('model')

# Get plot data
chans = xspec.Plot.x()
model = xspec.Plot.model()

# Plotting in matplotlib
plt.figure(figsize=(5,4))
plt.step(chans, model, color='black', lw=0.5)
#plt.ylim(1e-5)
plt.loglog()
plt.title('Celestial background model [apec + wabs(apec + pow)]')
plt.xlabel('Energy (keV)')
plt.ylabel(r'Photons $\mathrm{cm^{-2} \ s^{-1} \ keV^{-1}}$')
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False))

# Plot the COUNT pha files
plt.figure(figsize=(13,8))
plt.title('pha files that are in COUNTS')
for pha in pha_counts:
    file = f'bkg_files/{pha}'
    tab = Table.read(file)
    plt.step(tab['CHANNEL'], tab['COUNTS'], label=pha)

plt.xlabel('CHANNEL')
plt.ylabel('COUNTS (ct)')
plt.legend()
plt.loglog()
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False))

# Plot the RATE pha files with no filter
plt.figure(figsize=(13,8))
plt.title('pha PSF ')
for pha in pha_rate_psf_wo:
    file = f'bkg_files/{pha}'
    tab = Table.read(file)
    plt.step(tab['CHANNEL'], tab['RATE'], label=pha)

plt.xlabel('CHANNEL')
plt.ylabel('RATE (ct/s)')
plt.legend()
plt.loglog()
plt.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.show()


