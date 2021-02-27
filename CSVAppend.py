import csv

with open('Original.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Description_Item", "Item_Name", "Price"])
    writer.writerow(["Set", "Steel Item", "$50"])
    writer.writerow(["Utensils", "Crockery", "$100"])
    writer.writerow(["Plates", "Glass", "$500"])
    writer.writerow(["Utensils", "Crockery", "$100"])


with open('NewFile.csv' ,'w',newline='') as outFile:
    fileWriter = csv.writer(outFile)
    with open('Original.csv','r',newline='') as inFile:
        fileReader = csv.reader(inFile)
        for row in fileReader:
            if(row[0]!='Utensils' or row[0]=='Description_Item'):
                 fileWriter.writerow(row)


print("Original FIle Data")
with open('Original.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print(" ")
print("After Updation data")
with open('NewFile.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


