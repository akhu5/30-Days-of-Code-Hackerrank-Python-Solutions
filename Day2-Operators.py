# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    # Calculating total tip to be paid
    tip_cost = meal_cost * (tip_percent / 100)
    # Calculating total tax to be paid
    tax_cost = meal_cost * (tax_percent / 100)
    # Calculating total meal cost to be paid
    total_meal_cost = meal_cost + tip_cost + tax_cost
    # Rounding and printing
    print(round(total_meal_cost))


if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)
