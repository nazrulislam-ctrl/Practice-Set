# Write a python program using function to convert Celsius to Fahrenheit.


def celsiusToFahrenheit(c):
    f= (c*(9/5)+32)
    return f

c=int(input("Enter the Temperature in degree: "))

print(f"{celsiusToFahrenheit(c)}°F")
