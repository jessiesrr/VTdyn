import numpy as np
import libs.contact_inhibition_lib as lib #library for simulation routines
import libs.data as data
import libs.plot as vplt #plotting library
from structure.global_constants import *
import structure.initialisation as init
from structure.cell import Tissue, BasicSpringForceNoGrowth

"""run a single voronoi tessellation model simulation"""

l = 10 # population size N=l*l
timend = 50. # simulation time (hours)
timestep = 1. # time intervals to save simulation history

rand = np.random.RandomState()

simulation = lib.simulation_contact_inhibition  #simulation routine imported from lib
CIP_parameters = {'threshold':0.0}
rates = (None,0.5,0.1) #deaths_rate,G_to_S_rate,S_to_div_rate


history = lib.run_simulation(simulation,l,timestep,timend,rand,progress_on=True,
            init_time=None,til_fix=False,save_areas=False,cycle_phase=True,
            return_events=True,CIP_parameters=CIP_parameters,rates=rates)
                