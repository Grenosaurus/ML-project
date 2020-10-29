# ML-project
Machine Learning in Material Science project

This program generates multiple solar cell dataset graphs. Purpose of this program is to study the connection of solar cell temperature and solar cell efficiency.

Program is called by selecting first correct directory and correctly named dataset. This program considers the datasets name to be the solar cell temperature for easily accessign the dataset from the specific folder.

Program is runned in the following method after going to the folder where the program is in your OS shell:
 - If Windows -> python .\solarEfficiency.py
 - If Linux -> python3 solarEfficiency.py
Also check that you have the needed datasets.

Programs algorithms can be used for plotting other kind of datasets if wanted.

src folder holds the soure code of C++ program that reads the dataset and generates a output file that consists of 5 different values from each datasets found in the read datasets:
 - T_cell -> solar cell temperature
 - n_eff -> efficiency at highest P_pm
 - P_max -> highest power, max(P_pm)
 - V_max -> voltage of highest power
 - I_max -> current of highest power

# Goal
The goal of the project is to teach the machine learning model to estimate maximum efficiency of the solar cell, n_eff, based on the cell's temperature, T_cell.

# Contributers
Jauaries
Imran
Mario
