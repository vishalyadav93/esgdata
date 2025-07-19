import pandas as pd
from typing import Dict
from config import CONVERSION_FACTORS as cf

class Indicator:
    """Represents an environmental indicator with detailed emissions tracking."""
    
    CONVERSION_FACTORS = cf

    def __init__(self, name: str, category: str, measuring_unit: str, value: float, 
                 GHG_factors: Dict[str, float], source: str, year: int, threshold: float = None):
        """
        :param name: Name of the indicator (e.g., Electricity, Diesel)
        :param category: ESG category (e.g., Energy, Transport, Industrial)
        :param measuring_unit: Unit of measurement (e.g., kWh, liters, m³)
        :param value: Activity data (e.g., amount of fuel used)
        :param GHG_factors: Dict with Global Warming Potential (GWP) for CO₂, CH₄, N₂O
        :param source: Data source (e.g., "EPA", "GHG Protocol")
        :param year: Year of recorded data
        :param threshold: Optional threshold for emissions benchmarking
        """
        self.name = name
        self.category = category
        self.measuring_unit = measuring_unit
        self.value = value
        self.GHG_factors = GHG_factors  # GWP factors for CO₂, CH₄, N₂O
        self.source = source
        self.year = year
        self.threshold = threshold  # Warning level for emissions

    def calculate_emissions(self) -> Dict[str, float]:
        """Calculates individual emissions for CO₂, CH₄, and N₂O."""
        emissions = {gas: round(self.value * factor, 2) for gas, factor in self.GHG_factors.items()}
        emissions["total_CO2e"] = round(sum(emissions.values()), 2)  # Total CO₂ equivalent
        return emissions

    def convert_unit(self, new_unit: str):
        """Converts the value to another unit based on predefined conversion factors."""
        key = (self.measuring_unit, new_unit)
        if key in self.CONVERSION_FACTORS:
            self.value *= self.CONVERSION_FACTORS[key]
            self.measuring_unit = new_unit
        else:
            raise ValueError(f"Conversion from {self.measuring_unit} to {new_unit} not defined.")

    def compare_with_threshold(self) -> str:
        """Checks if emissions exceed the defined threshold."""
        if self.threshold and self.calculate_emissions()["total_CO2e"] > self.threshold:
            return f"⚠️ Warning! {self.name} emissions exceed threshold of {self.threshold} tons CO₂e."
        return "✅ Emissions within acceptable limits."

    def __repr__(self):
        emissions = self.calculate_emissions()
        return (f"Indicator(name={self.name}, category={self.category}, unit={self.measuring_unit}, "
                f"value={self.value}, source={self.source}, year={self.year}, total_CO2e={emissions['total_CO2e']})")

# Sample data table (can be expanded or fetched from APIs)
data_table = pd.DataFrame([
    {"name": "Electricity", "category": "Energy", "measuring_unit": "kWh", "value": 1000, 
     "GHG_factors": {"CO2": 0.4, "CH4": 0.0002, "N2O": 0.0001}, "source": "EPA", "year": 2024, "threshold": 450},
    
    {"name": "Diesel", "category": "Transport", "measuring_unit": "Liters", "value": 500, 
     "GHG_factors": {"CO2": 2.7, "CH4": 0.002, "N2O": 0.001}, "source": "GHG Protocol", "year": 2023, "threshold": 1400},

    {"name": "Natural Gas", "category": "Energy", "measuring_unit": "m³", "value": 300, 
     "GHG_factors": {"CO2": 2.0, "CH4": 0.01, "N2O": 0.005}, "source": "IPCC", "year": 2024, "threshold": 1000}
])
print(data_table)
# Assigning values from the table
indicators = [Indicator(**row) for _, row in data_table.iterrows()]

# Display results
for indicator in indicators:
    print(f"{indicator.name} ({indicator.year}) - Emissions: {indicator.calculate_emissions()}")
    print(indicator.compare_with_threshold())

# Convert a unit (example: converting electricity from kWh to MJ)
indicators[0].convert_unit("MJ")
print(f"\nConverted {indicators[0].name} to {indicators[0].measuring_unit}: {indicators[0].value} MJ")
