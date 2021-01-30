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


