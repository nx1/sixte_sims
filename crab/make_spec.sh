xmldir=$SIXTE/share/sixte/instruments/athena-wfi/wfi_wo_filter_B4C
makespec \
EvtFile=sim_evt_mcrab.fits \
Spectrum=spec_mcrab.pha \
EventFilter="(RA>359.95 || RA<0.05) && Dec>-0.05 && Dec<+0.05" \
RSPPath=${xmldir} clobber=yes
