echo "============================"
echo "======= Removing Files ====="
echo "============================"
./cleanup.sh

echo "============================"
echo "==== Creating Simput file==="
echo "============================"
./make_simput.sh

echo "============================"
echo "======= Running SIXTE ======"
echo "============================"
./run_sixte.sh

echo "============================"
echo "======= Creating image ====="
echo "============================"
./make_img.sh

echo "============================"
echo "==== Creating Spectrum ====="
echo "============================"
./make_spec.sh

echo "============================"
echo "===== Displaying image ====="
echo "============================"
ds9 -log img_mcrab.fits -cmap he

echo "============================"
echo "==== Displaying spectra ===="
echo "============================"
./show_spec.sh

