#Qeustion 3
#selling data analysier
#Damascus on 04/20/2023

#program that calculate
# 1- the mean of selling prices of Tea, Cofee and sugar. in every month of the year.
# 2- the mean price of every products
# 3- define the month with the hieghest selling.
# 4- define the most selling product in the year


# the data are stored in a dictionary with name "data" and the months will be the keys of that dictionary.
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

print("Request 2\n")
#calculate the mean of each month
#dict.items() allows to loop throug the keys and its values.
#looping throug the data dict
for month, products in data.items() :
    sum = 0 #variable to store the sum of products total sales in one month
    i = 0 #number of selling product in that month
    for product in products: #looping through product names and total selling prices
        sum = sum + product[1]
        i = i+1
    mean = sum/i #calculate the mean
    print("The mean of selling products in {} is {:.2f}".format(month,mean)) #print the mean total selling in each month.


print("Request 3\n")
#calculate the mean of the total selling price of each product during the year.

#define a dictionary called 'sum' to calculate the sum of sales for each product
#the keys of this variable are the name of product
sum = {}
for month, products in data.items():
    products = dict(products)
    for product in products:
        sum[product] = 0
    break

#looping throug the data dict
for month, products in data.items():
    products = dict(products) #convert the list of tuples to a dictionary 
    for product in products:
        sum[product] = sum[product] + products[product] #sum the values of selling tea during each month

#print the result
for product in sum.keys():
    print("the mean of the total sales of {} during the year is {:.2f}\n".format(product,sum[product]/len(data.keys()))) 


print("Request 4\n")
#define the month of the hights total sales

#define a dict to stor the total Sales of each month
totalSales={}
#looping throug the data dict
for month, products in data.items() :
    sumMonth = 0 #variable to store the sum of products total sales in one month
    for product in products: #looping through product names and total selling prices
        sumMonth = sumMonth + product[1]
    totalSales[month] = sumMonth #store the total sales in each month in totalSales dict
month = list(totalSales.keys()) #pull the keys of totalSales dictionary and convert them to a list and save it into month variable
sumOfSales = list(totalSales.values())#pull the values of totalSales dictionary and convert them to a list and save it into sumOfSales variable
print("the month with the highest sales is {} with \
total sales equal to\
 {}".format(month[sumOfSales.index(max(sumOfSales))],max(sumOfSales))) #print the name of the month with the hights sales based on the index of the max value of sumOfSales


print("\nRequest 5\n")

#define the product with the highest sales during the year
productName = list(sum.keys()) #pull the keys of the sum dictionary and convert them into a list and save it into productName 
sumOfSales = list(sum.values()) #pull the values of sum dictionary and convert them into a list and save it into sumOfSales
print("the product with the highest sales is {} with \
total sales equal to\
 {}".format(productName[sumOfSales.index(max(sumOfSales))],max(sumOfSales)))#print the name of the prouduct with the hights sales based on the index of the max value of sumOfSales


