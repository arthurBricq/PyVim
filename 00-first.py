# Startup script for a good jupyter-qtconsole Python workflow
# @arthur-bricq

# 1. Three basic imports 
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
pd.set_option("display.max_columns", 0)

# 2. a few I-Python settings
from IPython import get_ipython 
ipython = get_ipython()
ipython.magic("matplotlib qt")
ipython.magic("load_ext autoreload")
ipython.magic("autoreload 2")

