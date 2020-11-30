# ML-project
Machine Learning in Material Science course project

Purpose of this program is to study the connection of solar cell temperature and solar cell efficiency for designing and teaching Machine Learning (ML) model for solar cell studies.

Program is called by selecting first correct directory and correctly named dataset (can be changed). This program considers the datasets name to be the solar cell temperature for easily accessign the dataset from the specific folder.

Program is runned in the following method after going to the folder where the program is in your OS shell:
 - If Windows -> python .\solarEfficiency.py
 - If Linux -> python3 solarEfficiency.py

Also check that you have the needed datasets and dependencies. Packets and libraries used by the ML program can be found in requirments.txt file.

Programs algorithms can be used for plotting other kind of datasets if wanted.

src folder holds the soure code of C++ program that reads the dataset and generates a output file that consists of 5 different values from each datasets found in the read datasets:
 - T_cell -> solar cell temperature
 - n_eff -> efficiency at highest P_pm
 - P_max -> highest power (MAX[P_pm])
 - V_max -> voltage of highest power
 - I_max -> current of highest power

NOTE: For operating the program in Linux based OS, you must comment or remove 'freeze_support()' from the script (also explained in the script itself).


# Goal
The goal of the project is to teach the machine learning model to estimate maximum efficiency of the solar cell, n_eff, based on the cell's temperature, T_cell.

# Main Contributers:
Jauaries, Imran, and Mario
