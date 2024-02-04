import random

def simulate_investment(amount, years, rate_min, rate_max):
    # Simulate the growth of the investment each year with a randomly chosen annual interest rate
    for _ in range(years):
        rate = random.uniform(rate_min, rate_max)
        amount += amount * rate
    return amount

if __name__ == "__main__":
    # Assuming placeholders for other activities are just for demonstration
    # Dice Simulation placeholder
    print("Rolling 3 dice with 6 sides each: Placeholder for actual function call")
    
    # Temperature Conversion placeholders
    print("Converting 100F to Celsius: Placeholder for actual function call")
    print("Converting 0C to Fahrenheit: Placeholder for actual function call")
    
    # Generate a Single Random Number placeholder
    random_number = "Placeholder for actual function call"
    print(f"The generated random number is: {random_number}")
    
    # Investment Simulation
    initial_amount = 1000  # Example investment amount
    investment_years = 5  # Time frame
    interest_rate_min = 0.01  # Minimum annual interest rate
    interest_rate_max = 0.05  # Maximum annual interest rate
    final_amount = simulate_investment(initial_amount, investment_years, interest_rate_min, interest_rate_max)
    print(f"Final investment value after {investment_years} years: ${final_amount:.2f}")
