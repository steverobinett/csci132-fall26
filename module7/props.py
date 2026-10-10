class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15°C is not possible.")
        self._celsius = value

    celsius = property(get_celsius, set_celsius)

    def get_fahrenheit(self):
        return (self._celsius * 9/5) + 32

    def set_fahrenheit(self, value):
        if value< -459.67:
            raise ValueError("Temperature below -459.67°F is not possible.")    
        
        self._celsius = (value - 32) * 5/9

    fahrenheit = property(get_fahrenheit, set_fahrenheit)

def main():
    t = Temperature(25)
    print(f"Temperature in Celsius: {t.celsius}°C")
    print(f"Temperature in Fahrenheit: {t.fahrenheit}°F")

    t.fahrenheit = 100
    print(f"Updated Temperature in Celsius: {t.celsius:.2f}°C")
    print(f"Updated Temperature in Fahrenheit: {t.fahrenheit}°F")

main()