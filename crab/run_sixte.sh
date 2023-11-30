base=mcrab
#xml=/home/nkhan/.local/bin/sixte/share/sixte/instruments/athena-wfi/wfi_w_filter_B4C/fd_wfi_ff_df35mm.xml
xml=/home/nkhan/.local/bin/sixte/share/sixte/instruments/athena-wfi/wfi_w_filter_B4C/ld_wfi_ff_large.xml

runsixt XMLFile=${xml} RA=0.000 Dec=0.000 Prefix=sim_ Simput=${base}.fits EvtFile=evt_${base}.fits Exposure=1000
