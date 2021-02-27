def sorted():
    n = int(input())
    for i in range(n):
        mystr = input()
        mystr = mystr.lower()
        mystrlength = len(mystr)
        str1 = ""
        str2 = ""
        k = mystrlength // 2
        if (mystrlength % 2 == 0):
            middle = k
        else:
            middle = k + 1
        for i in range(0, k):
            str1 += mystr[i]
            str2 += mystr[middle + i]

        a = sorted(str1)
        b = sorted(str2)
        if (a == b):
            print("Yes")
        else:
            print("No")


def MaxRevenue():
    clients = int(input("Enter number of customers"))
    mybudgetList = []
    # Declaring a dictionary for
    mycountdict = {}
    for i in range(clients):
        # Insert the budgets in list
        mybudgetList.append(int(input()))
    myresultList=[]
    for i in range(0, clients):
        SelectedIndex = mybudgetList[i]
        countTimes = 0
        for j in mybudgetList:
            if (SelectedIndex <= j):
                countTimes += 1
        myresultList.append(SelectedIndex*countTimes)

        mycountdict[SelectedIndex] = countTimes
    print("Max Revenue we can generate",max(myresultList))

    #print(mycountdict)


MaxRevenue()


















