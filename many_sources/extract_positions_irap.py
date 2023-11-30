from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
import astropy.units as u

image = Image.open('irap.png')

image_array = np.array(image)

red_pixels = np.argwhere((image_array[:,:,0] == 255) & (image_array[:,:,1]==0) & (image_array[:,:,2] == 0))

wcs = WCS(naxis=2)
extent = 0.25
wcs.wcs.cdelt = [extent/60,extent/60]
wcs.wcs.crpix = [image_array.shape[1] / 2, image_array.shape[0] / 2]
wcs.wcs.crval = [0,0]

ra_dec_coords = wcs.pixel_to_world(red_pixels[:,1], red_pixels[:,0])

print(red_pixels)
xs, ys = [], []
for x, y in red_pixels:
    xs.append(x)
    ys.append(y)



ras = -ra_dec_coords[0]
decs = -ra_dec_coords[1]

lines = []
simput_files = []
for i in range(len(ras)):
    flux = np.random.uniform(low=3e-13, high=3e-11)
    ra = ras[i].value%360 
    dec = decs[i].value
    simput_file = f"src{i+1}.fits"
    simput_files.append(simput_file)
    line = f'simputfile Simput={simput_file} RA={ra:.4f} Dec={dec:.4f} srcFlux={flux:.4e} XSPECFile=mcrab.xcm Emin=2 Emax=10 clobber=yes'
    print(line)
    lines.append(line)

files=str(simput_files).replace("'",'')[1:-1].replace(' ','')
line = f'simputmerge clobber=yes FetchExtensions=yes Infiles={files} Outfile=mcrab.fits'
lines.append(line)

with open('run_simput.sh', 'w+') as f:
    f.writelines(s + '\n' for s in lines)

"""
plt.figure()
plt.scatter(xs,ys)
plt.show()

plt.figure()
plt.scatter(ras,decs)
plt.show()
"""
