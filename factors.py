"""
factors.py - Carbon Emission Factors
All values are in kg CO2e (carbon dioxide equivalent)

Source: Based on typical carbon footprint calculators and environmental data
"""

# Number of days in an average month
DAYS_PER_MONTH = 30


# TRANSPORT FACTORS (kg CO2e per km)
TRANSPORT_FACTORS = {
    'car': 0.2,       # Average car: 0.2 kg CO2e per km
    'bus': 0.1,       # Public bus: 0.1 kg CO2e per km
    'train': 0.05,    # Train: 0.05 kg CO2e per km
    'bike': 0.0,      # Bicycle: 0 emissions
    'walk': 0.0       # Walking: 0 emissions
}

# Example calculation check:
# CAR: 1 km daily = 1 * 0.2 * 30 = 6 kg CO2e monthly ✓


# DIET FACTORS (kg CO2e per month)
DIET_FACTORS = {
    'meat_heavy': 250,    # Meat with every meal
    'average': 150,       # Balanced diet with some meat
    'vegetarian': 100,    # No meat, but dairy and eggs
    'vegan': 75           # Plant-based only
}


# ENERGY FACTORS
ENERGY_FACTORS = {
    'electricity': 0.5,   # kg CO2e per kWh
    'heating': {
        'gas': 100,       # Gas heating: 100 kg CO2e per month
        'electric': 80,   # Electric heating: 80 kg CO2e per month
        'none': 0         # No heating: 0 emissions
    }
}
#this was the end of the code
# Example calculation check:
# ELECTRICITY: 100 kWh monthly = 100 * 0.5 = 50 kg CO2e
# GAS HEATING: Fixed at 100 kg CO2e per month
# Total Energy: 50 + 100 = 150 kg CO2e monthly ✓
