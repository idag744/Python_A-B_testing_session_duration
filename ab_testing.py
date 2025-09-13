import numpy as np
import pandas as pd
from scipy import stats
from utils import get_stats, degrees_of_freedom, t_value, p_value, make_decision

# Load the experiment dataset
data = pd.read_csv("background_color_experiment.csv")

# Separate control and variation groups
control_data = data[data["user_type"] == "control"]["session_duration"].to_numpy()
variation_data = data[data["user_type"] == "variation"]["session_duration"].to_numpy()

# Perform AB test for average session duration
decision = make_decision(variation_data, control_data, alpha=0.05)

print(f"Decision based on AB test: {decision}")

