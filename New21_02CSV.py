import csv

with open('Original2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Description_Item", "Item_Name", "Price"])
    writer.writerow(["Set", "Steel Item", "$50"])
    writer.writerow(["Utensils", "Crockery", "$100"])
    writer.writerow(["Plates", "Glass", "$500"])
    writer.writerow(["Utensils", "Crockery", "$100"])
    