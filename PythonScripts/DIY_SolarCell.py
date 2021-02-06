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

#File directory
filePath = 'C:/Users/jauar/Documents/text_files/Solar_data/Degrees/60'

efficiencyData = []
cellNumberData = []
moduleNumberData = []
hourData = []
visibilityData = []


# Hour
for hour in range(0, 145, 1):
    filePath_hour = '%s/%s' % (filePath, hour)

    # Checking if the hour number in the folder
    try:
        # Measurement
        for sampleNumber in range(0, 6, 1):
            # Checking if the plate number is found in the solar cell file name
            try:
                # Plate
                for moduleNumber in range(0, 6, 1):
                    # Checking if the module number is found in the solar cell file name
                    try:
                        # Cell
                        for cellNumber in range(0, 6, 1):
                            # Checking if the cell number is found in the solar cell file name
                            try:
                                for dayNumber in range(0, 30, 1):
                                    # Checking if the day number is found in the solar cell file name
                                    try:
                                        max_efficiency = 0

                                        try:
                                            solarCell_dataset = '%s/EL0%s_0%s_0%s_%smar_Vis_60C' % (filePath_hour, sampleNumber, moduleNumber, cellNumber, dayNumber) # File path
                                            # Reading file
                                            f = open(solarCell_dataset, 'r')
                                            solar_in = f.readlines()
                                            f.close()

                                            VisibilityValue = 1

                                            # Splitting the datasets values to their specific variables
                                            for i in range(0, len(solar_in)):
                                                # Checking for IndexErrors in the read files
                                                try:
                                                    solar_line = solar_in[i].split(None, 2)

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
                                            cellNumberData.append(cellNumber)
                                            hourData.append(hour)
                                            moduleNumberData.append(moduleNumber)
                                            efficiencyData.append(max_efficiency)
                                            visibilityData.append(VisibilityValue)

                                        except OSError:
                                            continue

                                    except OSError:
                                        continue

                            except OSError:
                                continue

                    except  OSError:
                        continue

            except OSError:
                continue

    except OSError:
        continue


# Hour
for hour in range(0, 145, 1):
    filePath_hour = '%s/%s' % (filePath, hour)

    # Checking if the hour number in the folder
    try:
        # Measurement
        for sampleNumber in range(0, 6, 1):
            # Checking if the plate number is found in the solar cell file name
            try:
                # Plate
                for moduleNumber in range(0, 6, 1):
                    # Checking if the module number is found in the solar cell file name
                    try:
                        # Cell
                        for cellNumber in range(0, 6, 1):
                            # Checking if the cell number is found in the solar cell file name
                            try:
                                for dayNumber in range(0, 30, 1):
                                    # Checking if the day number is found in the solar cell file name
                                    try:
                                        max_efficiency = 0

                                        try:
                                            solarCell_dataset = '%s/EL0%s_0%s_0%s_%smar_UV+Vis_60C' % (filePath_hour, sampleNumber, moduleNumber, cellNumber, dayNumber) # File path
                                            # Reading file
                                            f = open(solarCell_dataset, 'r')
                                            solar_in = f.readlines()
                                            f.close()

                                            VisibilityValue = 2

                                            # Splitting the datasets values to their specific variables
                                            for j in range(0, len(solar_in)):
                                                # Checking for IndexErrors in the read files
                                                try:
                                                    solar_line = solar_in[j].split(None, 2)

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
                                            cellNumberData.append(cellNumber)
                                            hourData.append(hour)
                                            moduleNumberData.append(moduleNumber)
                                            efficiencyData.append(max_efficiency)
                                            visibilityData.append(VisibilityValue)

                                        except OSError:
                                            continue

                                    except OSError:
                                        continue

                            except OSError:
                                continue

                    except  OSError:
                        continue

            except OSError:
                continue

    except OSError:
        continue


# Hour
for hour in range(0, 145, 1):
    filePath_hour = '%s/%s' % (filePath, hour)

    # Checking if the hour number in the folder
    try:
        # Measurement
        for sampleNumber in range(0, 6, 1):
            # Checking if the plate number is found in the solar cell file name
            try:
                # Plate
                for moduleNumber in range(0, 6, 1):
                    # Checking if the module number is found in the solar cell file name
                    try:
                        # Cell
                        for cellNumber in range(0, 6, 1):
                            # Checking if the cell number is found in the solar cell file name
                            try:
                                for dayNumber in range(0, 30, 1):
                                    # Checking if the day number is found in the solar cell file name
                                    try:
                                        max_efficiency = 0

                                        try:
                                            solarCell_dataset = '%s/EL0%s_0%s_0%s_%smar_oven_60C' % (filePath_hour, sampleNumber, moduleNumber, cellNumber, dayNumber) # File path
                                            # Reading file
                                            f = open(solarCell_dataset, 'r')
                                            solar_in = f.readlines()
                                            f.close()

                                            VisibilityValue = 3

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
                                            cellNumberData.append(cellNumber)
                                            hourData.append(hour)
                                            moduleNumberData.append(moduleNumber)
                                            efficiencyData.append(max_efficiency)
                                            visibilityData.append(VisibilityValue)

                                        except  OSError:
                                            continue

                                    except OSError:
                                        continue

                            except OSError:
                                continue

                    except  OSError:
                        continue

            except OSError:
                continue

    except OSError:
        continue


measurementHour = np.array(hourData) # Transforming appended data into a array
cellPlateNumber = np.array(moduleNumberData) # Transforming appended data into a array
measurementCellNumber = np.array(cellNumberData) # Transforming appended data into a array
maxEfficiency = np.array(efficiencyData) # Transforming appended data into a array
VisibilityColor = np.array(visibilityData)


plt.scatter(measurementHour, maxEfficiency, c = VisibilityColor) # Cluster graph for the data | Colouring based on the folder number
plt.show()
