#  we have to calculate downpayment cost not total cost with downpayment

# enter your dream house that u want to buy
totalcost=float(input("enter cost of your dream house"))
# enter the percent that you saved from salary e,g 5%=0.05
portionsaved=float(input("enter the percent salary to save as a decimal")) #
# enter your annual salary
annualsalary=float(input("enter ur annual salary"))

#enter the value in percentage how ur salary
annualsalaryinc=float(input("enter ur semi annual raise after 6months incremenr"))


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


    if monthly%6==0:
        annualsalary+=annualsalary * annualsalaryinc
        print('number of months after increment in 6',monthly)
    # elif monthly % 12==0:
    #     annualsalary = annualsalary * annualsalaryinc
    #     print('number of months after increment in 12',monthly)

# print("number of month",monthly)


