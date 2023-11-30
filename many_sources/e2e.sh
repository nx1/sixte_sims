py extract_positions_irap.py

echo "============================"
echo "==== Creating Simput file==="
echo "============================"
./run_simput.sh

echo "============================"
echo "======= Running SIXTE ======"
echo "============================"
./run_sixte.sh

echo "============================"
echo "======= Creating image ====="
echo "============================"
./make_img.sh
echo "============================"
echo "===== Displaying image ====="
echo "============================"
ds9 -log img_mcrab.fits -cmap he

