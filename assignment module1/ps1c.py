annualsalary=150000
semi_annual_raise=0.07
annual_return=0.04
downpayment=0.25*annualsalary
costhouse=1000000
monthsalary=annualsalary/12
currentsaving=0
minrate=int(0)
maxrate=input(1000)
sav_annualsalary=annual_return/12
portion_downpayment= costhouse * 0.25
monthlysalary=float(annualsalary/12)
portionsaved=float((maxrate-minrate)/2)
monthly=0



while(currentsaving<downpayment):
    monthly+= 1
    monthlyreturn = (currentsaving * monthsalary)
    currentsaving = currentsaving + (monthlyreturn + monthlysalary * portionsaved)

    for i in range(1,37):
        if monthly % 6 == 0:
            annualsalary += annualsalary * semi_annual_raise

    if currentsaving < portion_downpayment:
        maxrate = portionsaved
    else:
        high = portionsaved
    portion_saved = (maxrate + minrate) / 20000.0
    monthly += 1

    print("Best savings rate: ", portionsaved)
    print("Steps in bisection search", monthly)


