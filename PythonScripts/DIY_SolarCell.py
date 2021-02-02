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

efficiencyData = []
cellData = []
plateData = []
hourData = []

# TODO: Expand the build for large quantity of files by building system with the following parameters
hour = 0
temperature = 60

# Measurement
for measurement in range(0, 6, 1):
    # Checking if the measurement number is found in the solar cell file name
    try:
        # Plate
        for plate in range(0, 6, 1):
            # Checking if the plate number is found in the solar cell file name
            try:
                # Cell
                for cell in range(0, 6, 1):
                    # Checking if the cell number is found in the solar cell file name
                    try:
                        # File path
                        solarCell_datasets = 'C:/Users/jauar/Documents/text_files/Solar_data/Degrees/%s/%s/EL0%s_0%s_0%s_8mar' % (temperature, hour, measurement, plate, cell)

                        # Reading file
                        f = open(solarCell_datasets, 'r')
                        solar_in = f.readlines()
                        f.close()

                        max_efficiency = 0

                        # Splitting the datasets values to their specific variables
                        for k in range(0, len(solar_in)):
                            # Checking for IndexErrors in the read files
                            try:
                                solar_line = solar_in[k].split(None, 2)

                                voltage = float(solar_line[0]) # Solar cell voltage [V]
                                current = float(solar_line[1]) * (-1) # Solar cell current [A] | Multiplying all the values with -1 for changinh their direction

                                # Ignoring valus when the voltages is smaller than ZERO
                                if (voltage < 0):
                                    voltage = 0
                                    current = 0

                                else:
                                    # Converting current values that are smaller than 0 into 0.
                                    if (current < 0):
                                        current = 0

                                    power = voltage * current # Power [W]
                                    solar_efficiency = power/sunPower # Efficiency

                                    # Stores the maximum efficiency and the specific V_pm and I_pm of the efficiency
                                    if (solar_efficiency > max_efficiency):
                                        max_efficiency = solar_efficiency

                            except IndexError:
                                continue

                        # Appending values into empty list
                        cellData.append(cell)
                        hourData.append(hour)
                        plateData.append(plate)
                        efficiencyData.append(max_efficiency)

                    except OSError:
                        continue

            except OSError:
                continue

    except OSError:
        continue


print(hourData)
print(plateData)
print(cellData)
print(efficiencyData)

measurementHour = np.array(hourData) # Transforming appended data into a array
cellPlate = np.array(plateData) # Transforming appended data into a array
measurementCell = np.array(cellData) # Transforming appended data into a array
maxEfficiency = np.array(efficiencyData) # Transforming appended data into a array

plt.scatter(measurementHour, maxEfficiency, c = cellPlate) # Cluster graph for the data | Colouring based on the folder number
plt.show()
