import numpy as np
import libs.run_lib as lib
import libs.data as data

rand = np.random.RandomState()

N = 20
timend = 100.
timestep = 0.1


history = lib.run_simulation_poisson_death_and_div(N,timestep,timend,rand)
# history = lib.run_simulation_no_death(N,timestep,timend,rand)
data.save_N_cell(history,'test',2)
