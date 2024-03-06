#Qeustion 4
#selling data analysier using modules 
#Damascus on 04/20/2023
from unit import *

data = {}

print("kindlu enter the total selling price according to the product and month showed to you")
print("to end the entring kind type \"end\"")

#first we request the name of products that were in sales during the year
products = [] 
i = 1
while(1):
    product = input("kindly ente the name of product number {}, Or type 'end' when you're done :".format(i))
    if (product == "end"):
        break
    else:
        products.append(product)

print(products)

#second we are requesting to enter the name of the month and the values of sales durring that month for each product
while(1):
    month = input("kindly, enter the name of the month, or type 'end' to end the process : ")
    if(month =="end"):
        break
    info = []
    for product in products:
        price = input("Kindly enter the total selling of {} in the month of {} :".format(product,month))
        info.append(tuple([product,int(price)]))
    data[month] = info

#Resolve the question three using the defined functions.
#data = {
#    "jan": [("tea",3000), ("cofee",5000), ("sugar",2300)],
#    "feb": [("tea",2800), ("cofee",5500), ("sugar",2300)],
#    "mar": [("tea",1900), ("cofee",4700), ("sugar",4000)],
#    "apr": [("tea",3300), ("cofee",6000), ("sugar",3600)],
#    "may": [("tea",3500), ("cofee",6100), ("sugar",3200)],
#    "jun": [("tea",1900), ("cofee",4700), ("sugar",4000)],
#    "jul": [("tea",2000), ("cofee",2300), ("sugar",1900)],
#    "aug": [("tea",3500), ("cofee",3200), ("sugar",3600)],
#    "sep": [("tea",6000), ("cofee",4000), ("sugar",4500)],
#    "oct": [("tea",1200), ("cofee",2100), ("sugar",2000)],
#    "nov": [("tea",3500), ("cofee",3200), ("sugar",3600)],
#    "dec": [("tea",4000), ("cofee",8000), ("sugar",4400)]
#    }

dictToTxt(data,"salesData") #write the dictionary data to a file named "salesData".
newData = txtToDict("salesData") #read the data and assign it to a new dictionary.

#prith the mean of each month.
for month in newData.keys():
    print("The mean of selling products in {} is {:.2f}".format(month,monthMean(newData,month)))

#print the mean of each product
for month,products in data.items():
    for product in products:
        print("the mean of the total sales of {} during the year is {:.2f}\n".format(product,productMean(newData,product)))
    break

#print the month with the highest sales
print("the month with the highest sales is {}".format(hightestMonth(newData)))

#print the product with the highest sales.
print("the product with the highest sales is {}".format(highestProduct(newData)))



