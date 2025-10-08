import andes
import numpy as np
from andes.utils.tsat import tsat_to_df, plot_comparison, run_cmp

andes.config_logger(stream_level=30)

# load scenario 1 data
omega_lt2 = tsat_to_df('omega_lt2s.xls')
v_lt2 = tsat_to_df('v_lt2s.xls')

# load scenario 2 data
omega_gt = tsat_to_df('omega_gt.xls')
v_gt = tsat_to_df('v_gt.xls')
