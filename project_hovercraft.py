
# A hovercraft factory makes ten hovercraft per month.
# It cost 2,000,000 to build one
# They also pay 1,000,000 for insurance
# Selling price of one hovercraft is 3,000,000
# This program determine whether profit is made or not based on how many of the ten hovercraft was sold

print("This is a program to determine the profit in a hovercraft factory.")
cost_of_buiding_ten_hovercraft_for_one_month = 2_000_000 * 10
sales_of_one_hovercraft = 3_000_000
insurance = 1_000_000

total_monthly_production_cost = cost_of_buiding_ten_hovercraft_for_one_month + insurance


while True:
    try:
        sales_made = int(input("Enter the number of hovercraft sold in one month: "))
    except :
        print("Enter a digit")

    total_amount_of_sales = sales_made * sales_of_one_hovercraft

    if total_monthly_production_cost < total_amount_of_sales:
        print("Profit")
    elif total_monthly_production_cost > total_amount_of_sales:
        print("Loss")
    elif total_monthly_production_cost == total_amount_of_sales:
        print("Even")
