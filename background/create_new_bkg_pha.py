# This script modifies the flat particle bkg file from
# https://www.sternwarte.uni-erlangen.de/sixte/instruments/
# That was last updated 2021-11-17
# to use instead the summed photon + particle background
# that was calculated by Arne Rau
# See https://www.mpe.mpg.de/ATHENA-WFI/response_matrices.html
import os
from astropy.io import fits

SIXTE = os.environ['SIXTE']
if SIXTE is None:
    raise ValueError(f'SIXTE enviroment variable not set!')

bkg_sixte = f'{SIXTE}/share/sixte/instruments/athena-wfi/calibration_files/sixte_wfi_particle_bkg_20190829.pha'

bkg_summed_w_filter = 'bkg_files/athena_wfi_rib2.3_B4C_20210329_bkgd_sum_psf_w_filter_FovAvg.pha'
bkg_summed_wo_filter = 'bkg_files/athena_wfi_rib2.3_B4C_20210329_bkgd_sum_psf_wo_filter_FovAvg.pha'

new_bkg_sixte_w = f'{SIXTE}/share/sixte/instruments/athena-wfi/calibration_files/athena_wfi_rib2.3_B4C_20210329_bkgd_sum_psf_w_filter_FovAvg.pha'
new_bkg_sixte_wo = f'{SIXTE}/share/sixte/instruments/athena-wfi/calibration_files/athena_wfi_rib2.3_B4C_20210329_bkgd_sum_psf_wo_filter_FovAvg.pha'

hdul1 = fits.open(bkg_sixte)
hdul2 = fits.open(bkg_summed_w_filter)

# Replace the first 1490 values 
hdul1[1].data[0:1490] = hdul2[1].data[0:1490]

# Renormalize values to 1
v = [hdul1[1].data[i][1] for i in range(1490)]
v2 = v / max(v)

# set values to new normalized values 
for i in range(0, 1489):
    hdul1[1].data[i][1] = v2[i]

# Replace the rest with the last value
for i in range(1490,1498):
    hdul1[1].data[i][1] = hdul1[1].data[1489][1]


print(f'writing new file to {new_bkg_sixte_wo}')
hdul1.writeto(new_bkg_sixte_w, overwrite=True)

hdul1 = fits.open(bkg_sixte)
hdul2 = fits.open(bkg_summed_wo_filter)

# Replace the first 1490 values 
hdul1[1].data[0:1490] = hdul2[1].data[0:1490]
# Replace the rest with the last value
for i in range(1490,1498):
    hdul1[1].data[i][1] = hdul1[1].data[1489][1]

print(f'writing new file to {new_bkg_sixte_wo}')
hdul1.writeto(new_bkg_sixte_wo, overwrite=True)
