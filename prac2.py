# Considerashowroom ofelectronicproducts,wheretherearevarious salesmen.Eachsalesmanisgivenacommissionof5%,dependingonthesales madepermonth.Incasethesaledoneislessthan50000,thenthesalesmanis notgivenanycommission.Writeafunctiontocalculatetotalsalesofasalesman inamonth,commissionandremarksforthesalesman.Salesdonebyeach salesmanperweekistobeprovidedasinput.Usetuples/listtostoredataof salesmen
def calculateRenumeration(n):
    for item in range(1,n+1):
        totalSale=0.0
        commission=0.0
        remark=""
        print("For Salesman {}".format(item))
        for j in range(1,5):
            x=int(input("Enter the sales of Week {}:".format(j)))
            totalSale+=x
        rate=5 if (totalSale>50000) else 0
        commission=totalSale+(totalSale*rate)
        if totalSale>=80000:
            remark="Excellent"
        elif totalSale>=60000 and totalSale<80000:
            remark="Good"
        elif totalSale>=40000 and totalSale<60000:
            remark="Average"
        elif totalSale<40000:
            remark="Work Hard"
        ans=[totalSale,commission,remark]
        print("-"*50)
        print("Total Sale of Salesman{}: ".format(item),ans[0])
        print("Comission of Salesman{}: ".format(item),ans[1])
        print("Remarks of Salesman{}: ".format(item),ans[2])
        print("-"*50)


n = int(input('Enter Number of Salesmen: ')) 
calculateRenumeration(n)