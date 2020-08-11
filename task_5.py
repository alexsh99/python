proceeds = int(input("Proceeds: "))
costs = int(input("Costs: "))

if proceeds > costs:
    print("The company worked profitably")
    profit = proceeds - costs
    print(f"Profitability: {(profit / proceeds) * 100:0.2f}%")
    employees = int(input("Number of employees: "))
    print(f"Firm profit per employee: {profit / employees :0.2f}")
elif proceeds < costs:
    print("The company worked at a loss")
else:
    print("The company worked to zero")
