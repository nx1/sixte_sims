# A total of 35 .pha files are provided for the WFI
# background, these were last been updated on
# 29/03/2021
# Some of these files are in units of COUNTS, while 
# Other are in units of RATE.

prefix = "athena_wfi_rib2.3_B4C_20210329_bkgd"


# COUNTS
pha_counts = [
    "athena_wfi_bkgd_particle.pha",
    "athena_wfi_bkgd_particle_psf.pha",
    f"{prefix}_photon_w_filter_5aminAvg.pha",
    f"{prefix}_photon_w_filter_FovAvg.pha",
    f"{prefix}_photon_w_filter_OnAxis.pha",
    f"{prefix}_photon_wo_filter_5aminAvg.pha",
    f"{prefix}_photon_wo_filter_FovAvg.pha",
    f"{prefix}_photon_wo_filter_OnAxis.pha",
    f"{prefix}_photon_Be_filter_OnAxis.pha"
]

# RATE
pha_rate_extended_w = [
    f"{prefix}_photon_extended_w_filter_5aminAvg.pha",
    f"{prefix}_photon_extended_w_filter_FovAvg.pha",
    f"{prefix}_photon_extended_w_filter_OnAxis.pha",
    f"{prefix}_sum_extended_w_filter_5aminAvg.pha",
    f"{prefix}_sum_extended_w_filter_FovAvg.pha",
    f"{prefix}_sum_extended_w_filter_OnAxis.pha"
]

pha_rate_extended_wo = [
    f"{prefix}_photon_extended_wo_filter_5aminAvg.pha",
    f"{prefix}_photon_extended_wo_filter_FovAvg.pha",
    f"{prefix}_photon_extended_wo_filter_OnAxis.pha",
    f"{prefix}_sum_extended_wo_filter_5aminAvg.pha",
    f"{prefix}_sum_extended_wo_filter_FovAvg.pha",
    f"{prefix}_sum_extended_wo_filter_OnAxis.pha"
]
 
pha_rate_extended_Be = [
    f"{prefix}_photon_extended_Be_filter_OnAxis.pha",
    f"{prefix}_sum_extended_Be_filter_OnAxis.pha"
]

pha_rate_psf_w = [
      f"{prefix}_photon_psf_w_filter_5aminAvg.pha",
      f"{prefix}_photon_psf_w_filter_FovAvg.pha",
      f"{prefix}_photon_psf_w_filter_OnAxis.pha",
      f"{prefix}_sum_psf_w_filter_5aminAvg.pha",
      f"{prefix}_sum_psf_w_filter_FovAvg.pha",
      f"{prefix}_sum_psf_w_filter_OnAxis.pha",

]

pha_rate_psf_wo = [
    f"{prefix}_photon_psf_wo_filter_5aminAvg.pha",
    f"{prefix}_photon_psf_wo_filter_FovAvg.pha",
    f"{prefix}_photon_psf_wo_filter_OnAxis.pha",
    f"{prefix}_sum_psf_wo_filter_5aminAvg.pha",
    f"{prefix}_sum_psf_wo_filter_FovAvg.pha",
    f"{prefix}_sum_psf_wo_filter_OnAxis.pha",
]

pha_rate_psf_Be = [
    f"{prefix}_photon_psf_Be_filter_OnAxis.pha",
    f"{prefix}_sum_psf_Be_filter_OnAxis.pha",
]

all_pha = [
    pha_counts,
    pha_rate_extended_w,
    pha_rate_extended_wo,
    pha_rate_extended_Be,
    pha_rate_psf_w,
    pha_rate_psf_wo,
    pha_rate_psf_Be
]
          
