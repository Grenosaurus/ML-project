"""
 Simple program for reading and plotting solar cell datasets (Made: Jauaries).
"""


# Python packets
import numpy as np
import matplotlib.pyplot as plt
import sklearn as skl

from sklearn.cluster import KMeans


# Constant value
light_intensity = 1000 # [W/m^2]
A_cell = 0.81e-4 # [m^2]
sunPower = light_intensity * A_cell

folder_number = temperature = 0

# Empty list for storing temperature and efficiency
temp_data = []
neff_data = []

# Folders
for i in range(1, 100):
    # Checking if the specific folder is found in the solar cell dataset directory
    try:
        folder_number = i

        # Empty list for plotting linear line for one folder set
        folderTemp_data = []
        folderEfficinecy_data = []
        
        # Temperature
        for j in range(25, 100):
            # For checking if the specific temperature file can be found in the folder
            try:
                temperature = j
                
                solarCell_datasets = '/Users/Käyttäjä/Documents/text_files/Solar_data/%s/%s.txt' % (folder_number, temperature)
                
                # Reading file
                f = open(solarCell_datasets, 'r')
                solar_in = f.readlines()
                f.close()
                
                # Empty list for storing voltage, current and power
                solarVoltage_data = []
                solarCurrent_data = []
                solarPower_data = []
                
                max_efficiency = voltage_efficiency = current_efficiency = power_efficiency = 0
                
                # Splitting the datasets values to their specific variables
                for k in range(0, len(solar_in) - 1): # -1 is set hr'ere to read the full dataset as it gets error in the last empty lines
                    solar_line = solar_in[k].split(None, 2)

                    voltage = float(solar_line[0]) # Solar cell voltage
                    current = float(solar_line[1]) * (-1) # Solar cell current | Multiplying all the values with -1.
                    
                    # Ignoring valus when the voltages is smaller than 0
                    if (voltage < 0):
                        voltage = 0
                        current = 0
                    
                    else:
                        # Converting current values that are smaller than 0 into 0.
                        if (current < 0):
                            current = 0

                        power = voltage * current
                        solar_efficiency = power/sunPower # Efficiency

                        # Stores the maximum efficiency and the specific V_pm and I_pm of the efficiency
                        if (solar_efficiency > max_efficiency):
                            voltage_efficiency = voltage
                            current_efficiency = current
                            power_efficiency = power
                            max_efficiency = solar_efficiency
                    
                        solarVoltage_data.append(voltage)
                        solarCurrent_data.append(current)
                        solarPower_data.append(power)

                
                # Plotting current/voltage and power/voltage graphs for single dataset
                fig = plt.figure(j)
                fig.subplots_adjust(hspace = 0.4, wspace = 0.4)
                fig.set_figheight(10)
                fig.set_figwidth(10)

                # Plot: Current as voltage profile
                plt.subplot(1, 2, 1)
                plt.plot(solarVoltage_data, solarCurrent_data, '-o', color = 'red')
                plt.plot(voltage_efficiency, current_efficiency, 'o', color = 'black')
                plt.title('Current & Voltage curve', fontsize = 10)
                plt.xlabel('Voltage $[V]$', fontsize = 10)
                plt.ylabel('Current $[A]$', fontsize = 10)
                plt.grid(True)
                plt.axis([min(solarVoltage_data), max(solarVoltage_data), min(solarCurrent_data), max(solarCurrent_data) + 0.01])

                # Plot: Power as voltage function
                plt.subplot(1, 2, 2)
                plt.plot(solarVoltage_data, solarPower_data, '-o', color = 'green')
                plt.plot(voltage_efficiency, power_efficiency, 'o', color = 'black')
                plt.title('Power', fontsize = 10)
                plt.xlabel('Voltage $[V]$', fontsize = 10)
                plt.ylabel('Power $[W]$', fontsize = 10)
                plt.grid(True)
                plt.axis([min(solarVoltage_data), max(solarVoltage_data), min(solarPower_data), max(solarPower_data) + 0.01])

                # Shows the plot
                plt.show(j)
                

                temp_data.append(temperature)
                neff_data.append(max_efficiency)
                folderTemp_data.append(temperature) # For single folder
                folderEfficinecy_data.append(max_efficiency) # For single folder
                
                print('Maximum efficiency for temperature %s is %s' %(temperature, max_efficiency))
                print('V_pm = %s V and I_pm = %s A' % (voltage_efficiency, current_efficiency))

            except OSError:
                continue

        
        # Plotting linear line for maximum efficiency in temperature profile for one folder
        fig = plt.figure(i)
        fig.subplots_adjust(hspace = 0.4, wspace = 0.4)
        fig.set_figheight(10)
        fig.set_figwidth(10)

        # Plot: Efficiency as temperature function
        plt.subplot(1, 1, 1)
        plt.plot(folderTemp_data, folderEfficinecy_data, 'o', color = 'red')
        plt.plot([min(folderTemp_data), max(folderTemp_data)], [max(folderEfficinecy_data), min(folderEfficinecy_data)], color = 'blue')
        plt.xlabel('T [$^o$C]', fontsize = 10)
        plt.ylabel('\u03B7$_{eff}$ [%]', fontsize = 10)
        plt.grid(True)
        plt.axis([min(folderTemp_data) - 1, max(folderTemp_data) + 1, min(folderEfficinecy_data) - 0.1, max(folderEfficinecy_data) + 0.1])

        # Shows the plot
        plt.show(i)
        

    except OSError:
        continue


# Plots unclustered graph of all the maximum solar cell efficiencies found in all the datasets
fig = plt.figure('efficiency')
fig.subplots_adjust(hspace = 0.4, wspace = 0.4)
fig.set_figheight(10)
fig.set_figwidth(10)

# Plot: Unclustered graph
plt.subplot(1, 1, 1)
plt.plot(temp_data, neff_data, 'o', color = 'red')
#plt.title('Efficiency', fontsize = 10)
plt.xlabel('T [$^o$C]', fontsize = 10)
plt.ylabel('\u03B7$_{eff}$ [%]', fontsize = 10)
plt.grid(True)
plt.axis([min(temp_data) - 1, max(temp_data) + 1, min(neff_data) - 0.1, max(neff_data) + 0.1])

# Shows the plot
plt.show('efficiency')



"""
 For machine learning purpose a cluster format is going to be used in order to study the temperature shifts effect on solar cell efficinecy.
"""

# Model
model = KMeans(n_clusters = 2)

# Transforming two 1-dimensional arrays into one 2-dimensional array
combined = np.column_stack((temp_data, neff_data)).T


# Plots clustered graph of all the maximum solar cell efficiencies found in all the datasets
fig = plt.figure('cluster')
fig.subplots_adjust(hspace = 0.4, wspace = 0.4)
fig.set_figheight(10)
fig.set_figwidth(10)

# Plot: lustered graph
plt.subplot(1, 1, 1)
plt.scatter(temp_data, neff_data, c = temp_data)
plt.xlabel('T [$^o$C]', fontsize = 10)
plt.ylabel('\u03B7$_{eff}$ [%]', fontsize = 10)
plt.grid(True)
plt.axis([min(temp_data) - 1, max(temp_data) + 1, min(neff_data) - 0.1, max(neff_data) + 0.1])

plt.show('cluster')

