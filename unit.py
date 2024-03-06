

#1 - define a function that takes a dictionary and a month name and returns the mean of sales in that month.
def monthMean(data,month):
    sales = dict(data[month])               #pull the list of tubles of the selected month and convert it to a dictionary 
    prices = list(sales.values())           #pull the values of sales of each product sold in that month
    return sum(prices)/len(prices)          # return the mean


#2 - define a function that takes a dictionary and product name and returns the mean of sales of the that product
def productMean(data,product):
    sum = 0                                 #variable to calcuate the sum of the sales
    n = 0                                   #number of samples
    for month in data.keys():
        monthSale = dict(data[month])       #convert the list of tupels to dictionary
        sum = sum + monthSale[product]      #pull the values assosiated with the product and sum it 
        n = n+1                             #calculate the number of loops
    return sum/n                            #calculate and return the mean

#3 - define a function that takes a dict and return the month with highest sales.
def hightestMonth(data):
    totalSales={}
                                            #looping throug the data dict
    for month, products in data.items() :
        sum = 0                             #variable to store the sum of products total sales in one month
        for product in products:            #looping through product names and total selling prices
            sum = sum + product[1]
        totalSales[month] = sum             #store the total sales in each month in totalSales dict
    month = list(totalSales.keys())         #pull the keys of totalSales dictionary and convert them to a list and save it into month variable
    sumOfSales = list(totalSales.values())  #pull the values of totalSales dictionary and convert them to a list and save it into sumOfSales variable
    return month[sumOfSales.index(max(sumOfSales))] #the month with the hights sales based on the index of the max value of sumOfSales

#4 - define a function that takes a dict and return the product with the highest sales
def highestProduct(data):
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
            sum[product] = sum[product] + products[product] #sum the values of selling tea during each month          #insert the values to the key "sugar"
        productName = list(sum.keys())        #pull the keys of sumSales dictionary and convert them into a list and save it into productName 
        sumOfSales = list(sum.values())       #pull the values of totalSales dictionary and convert them into a list and save it into sumOfSales
        return productName[sumOfSales.index(max(sumOfSales))]



#5 - define a function that takes two inputs a dictionary and a file name and then it write the dictionary content to the file.
def dictToTxt(data, fileName):
    handl = open(fileName, "w")                #open the file to write
    for month in data.keys():           #loop on keys and values of the dictionary
        handl.write(month + ":") #write to a .txt file and separate between values with ":"
        prices = data[month]
        prices = dict(prices)
        numberOfProduct = len(prices.keys())
        i = 1
        for key,value in prices.items():
            handl.write(key+":"+str(value))
            i = i+1
            if i == numberOfProduct :
                handl.write("\n")
                i = 1
    handl.close()                              #close the file

#6 - Define a function that reads from a .txt file and return a dictonary
def txtToDict(fileName):
    data={}                                    #define a dictionary variable
    handl = open(fileName, "r")                #open the file to read from it
    for line in handl:                         #loop through every line in the file
        values = line.split(":")
        numberOfProduct = len(values)  - 1             #return a list of vaules which were separated with ":" when we write the data to the file
        i=1
        prices = []
        while(i<=numberOfProduct):
            prices.append(tuple([values[i],int(values[i+1])]))
            i+2
        data[values[0]] = prices #reform the dictionary
    return data
