import numpy as np
import pandas as pd

np.random.seed(50)

num_samples = 5000

# speeds from 0-262 km/h, acceleration from -3.0 to 3.0 m/s^2, temperature from -10 to 50 degrees Celsius, current battery level from 10 to 100%
speed = np.random.randint(low=0, high=262, size=num_samples)
acceleration = np.random.uniform(low=-3.0, high=3.0, size=num_samples)
temperature = np.random.randint(low=-10, high=50, size=num_samples)
current_battery_level = np.random.uniform(low=10, high=100, size=num_samples)

# battery_life = 100 - (speed * 0.1 + acceleration * 0.2 + temperature * 0.3 + current_battery_level * 0.4)

# max battery capacity range assumed 500 km
base_range = 500
range_penalty_speed = speed * 0.3
range_penalty_acceleration = acceleration * 0.2
range_penalty_temperature = [abs(t-25) * 0.5 for t in temperature]
range_penalty_battery = (100 - current_battery_level) * 3

predicted_range = base_range - range_penalty_speed - range_penalty_acceleration - range_penalty_temperature - range_penalty_battery

data = pd.DataFrame({
    'speed': speed, 
    'acceleration': acceleration, 
    'temperature': temperature, 
    'current_battery_level': current_battery_level, 
    'range_remaining': predicted_range
})

data = data.sample(frac=1).reset_index(drop=True)
data.to_pickle('data.pkl')
print(data.head())