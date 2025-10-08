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

ss = run_cmp('ieee14.raw', dyr='ieee14.dyr', fault_line='Line_1',
             t1=1.0, t2=3.0, tstep=1/120)

fig, ax = plot_comparison(ss, ss.GENROU.omega,
                omega_lt2, a=[0, 1],
                ylabel="Rotor Speed [Hz]",
                tsat_header=[r'$\omega$ TSAT 1', r'$\omega$ TSAT 2'],
                scale=60, left=0, right=1

fig, ax = plot_comparison(ss, ss.GENROU.v,
                v_lt2, a=[0, 1],
                ylabel="Terminal Voltage [pu]",
                tsat_header=['V TSAT 1', 'V TSAT 2'],
                left=0, right=10)