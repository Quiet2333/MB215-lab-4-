# Activity 2: Temperature Converter
def convert_temperature(temp, unit):
    if unit.lower() == 'c':
        return(temp*9/5)+32
    elif unit.lower() == 'f':
        return (temp - 32)
    else:
        return None 
    
Celsius_temp = float(input("enter the temperature in fahrenheit:"))
fahrenheit_temp = float(input("enter the temperature in celsius:"))

result_fahrenheit = convert_temperature(Celsius_temp, 'C')
print(f"{Celsius_temp}degrees celsius is equal to {result_fahrenheit: .2f}degrees of fahrenheit")

result_celsius = convert_temperature(fahrenheit_temp, 'F')
print(f"{fahrenheit_temp}degrees fahrenhit is equal to {result_celsius: .2f}degrees of celsius")
# Add the missing code here. Can use the following formulas to do #the do #conversion
     # Celsius to Fahrenheit    return (temp * 9/5) + 32  
     # Fahrenheit to Celsius return (temp - 32) * 5/9  