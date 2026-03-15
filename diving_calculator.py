class DivingCalculator:
    def __init__(self):
        pass

    def depth_to_pressure(self, depth):
        # Convert depth in meters to pressure in bar
        # Pressure = Depth * 0.1, taking into account 1 bar at surface
        return depth * 0.1 + 1.0

    def nitrogen_narcosis(self, depth):
        # Check nitrogen narcosis effects at depth
        if depth > 30:
            return "Potential for nitrogen narcosis. Be cautious!"
        return "Low risk of nitrogen narcosis."

    def oxygen_toxicity(self, depth):
        # Check for oxygen toxicity; 1.4 atm is a common limit
        pressure = self.depth_to_pressure(depth)
        if pressure > 1.4:
            return "Risk of oxygen toxicity. Limit your time at this depth."
        return "Safe for oxygen toxicity."

    def no_decompression_limits(self, depth):
        # Placeholder for actual no-decompression limit calculation
        # Normally this would depend on dive tables or algorithms
        return "No-decompression limit for this depth is 60 minutes."

    def air_consumption_calculation(self, depth, time):
        # Simple calculation assuming 20 liters/min at surface
        # Adjusting for depth: (20 liters/min) * (pressure in bar)
        pressure = self.depth_to_pressure(depth)
        air_consumed = 20 * pressure * time / 60  # Convert minutes to hours
        return air_consumed

if __name__ == '__main__':
    calculator = DivingCalculator()
    depth = 40  # Example depth in meters
    time = 30   # Example time in minutes
    pressure = calculator.depth_to_pressure(depth)
    print(f"Pressure at {depth} meters: {pressure} bar")
    print(calculator.nitrogen_narcosis(depth))
    print(calculator.oxygen_toxicity(depth))
    print(calculator.no_decompression_limits(depth))
    print(f"Air consumed during {time} minutes at {depth} meters: {calculator.air_consumption_calculation(depth, time)} liters."  
