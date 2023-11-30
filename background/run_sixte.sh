base=mcrab
#xml=/home/nkhan/.local/bin/sixte/share/sixte/instruments/athena-wfi/wfi_w_filter_B4C/fd_wfi_ff_df35mm.xml
#xml=/home/nkhan/.local/bin/sixte/share/sixte/instruments/athena-wfi/wfi_w_filter_B4C/ld_wfi_ff_large.xml
xml=/home/nkhan/.local/bin/sixte/share/sixte/instruments/athena-wfi/wfi_w_filter_B4C/ld_wfi_ff_large_sum_bkg.xml
#xml=/home/nkhan/sixte_sims/background/sim_files/wfi.xml
#bkg_file=/home/nkhan/.local/bin/sixte/share/sixte/instruments/athena-wfi/calibration_files/athena_wfi_rib2.3_B4C_20210329_bkgd_sum_psf_w_filter_FovAvg.pha

runsixt XMLFile=${xml} RA=0.000 Dec=0.000 Prefix=sim_ Simput=${base}.fits EvtFile=evt_${base}.fits Exposure=10000
#runsixt XMLFile=${xml} RA=0.000 Dec=0.000 Prefix=sim_ Simput=${base}.fits EvtFile=evt_${base}.fits Exposure=1000 BkgEventFile=${bkg_file}
