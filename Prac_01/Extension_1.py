TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = int(input("Which tariff? 11 or 31"))
while tariff != 11 and tariff != 31:
    print("Invalid choice")
    tariff = int(input("Which tariff? 11 or 31"))
if tariff == 11:
    per_price = TARIFF_11
else:
    per_price = TARIFF_31


"""
per_price = int(input("Enter price per kWh in cents"))
while per_price < 0:
    print("Invalid value")
    per_price = int(input("Enter price per kWh in cents"))
"""

daily_use = float(input("Enter daily use in kWh"))
while daily_use < 0:
    print("Invalid value")
    daily_use = float(input("Enter daily use in kWh"))

num_days = int(input("Enter the number of days in the billing period"))
while num_days < 0:
    print("Invalid value")
    num_days = int(input("Enter the number of days in the billing period"))

estimator = per_price * daily_use * num_days
"""/ 100"""
print("Estimated bill: ${:.2f}".format(estimator))
