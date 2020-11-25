"""
 Machine learning model for estimating the best suitable solar cell coefficent value for a given temperature (Made: Jauaries).
"""


# Python packets
import numpy as np
import pymc3 as pm
import arviz as az
import seaborn as sns
import matplotlib.pyplot as plt

import math

from multiprocessing import freeze_support
from sklearn.linear_model import LinearRegression


# Constant value
light_intensity = 1000 # [W/m^2]
A_cell = 0.25e-4 # [m^2]
sunPower = light_intensity * A_cell # Power of the Sun light [W]
folder_number = temperature = 0 # Definning the folder and temperature number before the program

# Empty list for storing temperature and efficiency
temp_data = []
neff_data = []
folder_data = []

# Folders | Ignoring the last 5 corrupted files
for i in range(1, 10, 1):
    # Checking if the specific folder is found in the solar cell dataset directory
    try:
        folder_number = i

        # Empty list for plotting linear line for one folder set
        folderTemp_data = []
        folderEfficinecy_data = []

        # Temperature
        for j in range(0, 100):
            # For checking if the specific temperature file can be found in the folder
            try:
                temperature = j

                solarCell_datasets = '../Solar_data/%s/%s.txt' % (folder_number, temperature)

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
                            voltage_efficiency = voltage
                            current_efficiency = current
                            power_efficiency = power
                            max_efficiency = solar_efficiency

                # Appending values into empty list
                folder_data.append(folder_number)
                temp_data.append(temperature)
                neff_data.append(max_efficiency)

            except OSError:
                continue

    except OSError:
        continue

"""
 For machine learning purpose a cluster format is going to be used in order to study the temperature shifts effect on solar cell coefficiency.
"""

length_temperature = len(temp_data)
length_efficiency = len(neff_data)

# Transforming two 1-dimensional arrays into one 2-dimensional array
combined = np.column_stack((folder_data, temp_data, neff_data)).T

# Bayesian linear regression model
x = np.array(temp_data) # Transforming appended data into a array
y = np.array(neff_data) # Transforming appended data into a array
z = np.array(folder_data) # Transforming appended data into a array
x = x.reshape(-1, 1) # Reshaping the x-axis array
y = y.reshape(-1, 1) # Reshaping the y-axis array
z = z.reshape(-1, 1) # Reshaping the z-axis array

print('Running on the PyMC3 v{}' .format(pm.__version__))
basic_model = pm.Model()

with basic_model as bm:
    # Priors starting from the middle of the points
    alpha = pm.Normal('alpha', mu = 0, sd = 5) # Too large mu value will cause the program to overflow | Maybe crash the system
    beta = pm.Normal('beta', mu  = 0, sd = 0.1)
    sigma = pm.HalfNormal('sigma', sd = 1)

    # Deterministics
    mu = alpha + beta * x

    # Likelihood in y axis
    Y_likelihood = pm.Normal('Y_likelihood', mu = mu, sd = sigma, observed = y)

    # Guarding the multiprocessed program
    if __name__ == '__main__':
        freeze_support() # Avoiding the RuntimeError of the multiprocessed program

        core = 1 # Amount of CPU cores, for avoiding 'Ctrl-C' event
        
        trace = pm.sample(draws = 10000, discard_tuned_samples = True, model = bm, cores = core)
        pm.traceplot(trace)
        print(pm.summary(trace).round(2))
        plt.show() # Shows the plot

        # Normal linear regression with sklearn
        lm = LinearRegression()
        y_prediction = lm.fit(x, y).predict(x)

        # Plotting linear regression graphs
        plt.scatter(x, y, c = z)
        plt.plot(x, y_prediction)
        plt.legend(loc = 'upper left', frameon = False, title = 'Simple Linear Regression\ny = {} + {} * x' .format(round(lm.intercept_[0], 2), round(lm.coef_[0][0], 2)))
        plt.title('Linear Regression')
        plt.xlabel('Temperature T [$K$]')
        plt.ylabel('Coefficent n$_{eff}$')
        plt.grid(True)
        plt.axis([min(x), max(x), min(y), max(y)])
        plt.show() # Shows the plot

        # Plotting the traces
        plt.plot(x, y, 'b.') # Plots blue dots in the figure

        idx = range(0, len(trace['alpha']), 10)
        alpha_m = trace['alpha'].mean()
        beta_m = trace['beta'].mean()

        # Appending the temperature array with the possible maximum and minimum
        x = np.append(x, 200) # Appending MAX
        x = np.append(x, -100) # Appending MIN
        x = x.reshape(-1, 1) # Reshaping the x-axis array after the appending

        plt.plot(x, trace['alpha'][idx] + trace['beta'][idx] * x, c = 'gray', alpha = 0.2) # Plots the gray line for definning the linear line for full dataset
        plt.plot(x, alpha_m + beta_m * x, c = 'black', label = 'y = {:.2f} + {:.2f} * x' .format(alpha_m, beta_m)) # Plots the black linear line
        plt.xlabel('x', fontsize = 15)
        plt.ylabel('y', fontsize = 15, rotation = 0)
        plt.title('Traces')
        plt.legend()
        plt.grid(True)
        plt.axis([min(x), max(x), 0, 35])
        plt.show() # Shows the plot
        
        pm.plots.plot_posterior(trace) # Posterior plots
        pm.plots.forestplot(trace) # Forest plot
        pm.plots.densityplot(trace) # Density plot
        pm.plots.energyplot(trace) # Energy plots
        plt.show() # Shows the plot

        # Sampling the data from the posterior chain
        y_prediction = pm.sampling.sample_posterior_predictive(model = bm, trace = trace, samples = 500)
        y_sample_posterior_predictive = np.asarray(y_prediction['Y_likelihood'])
        
        # Plotting posterior prediction
        _, ax = plt.subplots()
        ax.hist([n.mean() for n in y_sample_posterior_predictive], bins = 19, alpha = 0.5)
        ax.axvline(y.mean())
        ax.set(title = 'Posterior predictive of the mean', xlabel = 'mean(x)', ylabel = 'Frequency')
        plt.show() # Shows the plot

        # Removing the appended values from the x array for density graph
        x = np.delete(x, -1)
        x = np.delete(x, -1)
        x = x.reshape(-1, 1) # Reshaping the x-axis array after the deletion of the values

        # Reshaping and sorting the data
        inds = x.ravel().argsort()
        x_ord = x.ravel()[inds].reshape(-1)

        dfp = np.percentile(y_sample_posterior_predictive, [2.5, 25, 50, 70, 97.5], axis = 0)
        dfp = np.squeeze(dfp)
        dfp = dfp[:, inds]

        y_mean = y_sample_posterior_predictive.mean(axis = 0)
        y_mean = y_mean[inds]

        pal = sns.color_palette('Purples')
        plt.rcParams['axes.facecolor'] = 'white'
        plt.rcParams['axes.linewidth'] = 1.25
        plt.rcParams['axes.edgecolor'] = '0.15'

        # Defining the density plot
        fig = plt.figure(dpi = 100)
        ax = fig.add_subplot(111)
        plt.scatter(x_ord, y, s = 10, label = 'observed')
        ax.plot(x_ord, y_mean, c = pal[5], label = 'posterior mean', alpha = 0.5)
        ax.plot(x_ord, dfp[2, :], alpha = 0.75, color = pal[3], label = 'posterior median')
        ax.fill_between(x_ord, dfp[0, :], dfp[4, :], alpha = 0.5, color = pal[1], label = 'CR 95%')
        ax.fill_between(x_ord, dfp[1, :], dfp[3, :], alpha = 0.4, color = pal[2], label = 'CR 50%')
        ax.legend()
        plt.legend(frameon = True)
        plt.grid(True)
        plt.axis([min(x_ord), max(x_ord), 0, max(y) + 5])
        plt.show() # Shows the plot
        
