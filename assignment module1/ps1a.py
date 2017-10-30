#  we have to calculate downpayment cost not total cost with downpayment

# enter your dream house that u want to buy
totalcost=float(input("enter cost of your dream house"))
# enter the percent that you saved from salary e,g 5%=0.05
portionsaved=float(input("enter the percent salary to save as a decimal")) #
# enter your annual salary
annualsalary=float(input("enter ur annual salary"))

# monthly salary 120000 will calculate 10000 per month
monthly_salary=float(annualsalary /12)
# current saving in month 0
currentsaving=float(0)
# downpayment 0.25*120000
downpayment=0.25*totalcost
# annual return that you saved from annual salary means 4%
annual_return=0.04
savingannualsalary= annual_return/ 12

# monthlysaved=monthly_salary*0.1

monthly=0
while currentsaving < downpayment:
    monthly +=1
    monthlyreturn=(currentsaving*savingannualsalary)
    currentsaving=currentsaving+(monthlyreturn+monthly_salary*portionsaved)
print("number of month",monthly)
















# annual_salary=float(input("Enter your annual salary: "))
# portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
# total_cost=float(input("Enter the cost of your dream home: "))
# portion_down_payment=0.25*total_cost
# current_savings=float(0)
# monthly_salary=float(annual_salary/12)
# r=0.04
# rate=0.04/12
# monthly_savings=monthly_salary*0.1
# m=0
# while current_savings < portion_down_payment:
#     returns = (current_savings * r / 12)
#     current_savings = current_savings + ( returns + monthly_salary*portion_saved )
#     m+=1
# print(m)
