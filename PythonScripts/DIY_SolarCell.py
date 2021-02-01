"""
 Machine learning model for estimating the best suitable solar cell coefficent value for a given temperature in time for DIY Solar Cell (Made: Jauaries).
"""


# Python packets
import numpy as np
import pymc3 as pm
import arviz as az
import seaborn as sns
import matplotlib.pyplot as plt

import math
import sys

from multiprocessing import freeze_support
from sklearn.linear_model import LinearRegression



# Constants
light_intensity = 1000 # [W/m^2]
A_cell = 0.25e-4 # [m^2]
sunPower = light_intensity * A_cell # Power of the Sun light [W]


efficiencyData = cellData = []


# TODO: Expand the program for read more than 5 files!
for i in range(0, 5, 1):
    try:
        cell = i

        solarCell_datasets = 'C:/Users/jauar/Documents/text_files/Solar_data/Degrees/60/0/EL01_02_0%s_8mar' % (cell)

        # Reading file
        f = open(solarCell_datasets, 'r')
        solar_in = f.readlines()
        f.close()

        max_efficiency = voltage_efficiency = current_efficiency = power_efficiency = 0

        # Splitting the datasets values to their specific variables
        for k in range(0, len(solar_in) - 1): # -1 is set here to read the full dataset as it gets error in the last empty lines
            solar_line = solar_in[k].split(None, 2)

            voltage = float(solar_line[0]) # Solar cell voltage [V]
            current = float(solar_line[1]) * (-1) # Solar cell current [A] | Multiplying all the values with -1 for changinh their direction

            # Ignoring valus when the voltages is smaller than 0
            if (voltage < 0):
                voltage = 0
                current = 0

            else:
                # Converting current values that are smaller than 0 into 0.
                if (current < 0):
                    current = 0

                power = voltage * current # [W]
                solar_efficiency = power/sunPower # Efficiency

                # Stores the maximum efficiency and the specific V_pm and I_pm of the efficiency
                if (solar_efficiency > max_efficiency):
                    max_efficiency = solar_efficiency

        # Appending values into empty list
        cellData.append(cell)
        efficiencyData.append(max_efficiency)

    except OSError:
        continue


