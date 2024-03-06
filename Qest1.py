#First question 
#Passpoert needed doucuments
#Damascus on 04/17/2023
#A program asks the user to enter data in order to show him the needed doucuments according to his input.



#A fuction that requests from the user to enter a value of his age ang chck if it is valid.
def setValueAge():
    while(1): #loop that repeats itself untile the user has entered an acceptable value
        userAge = input("PLEASE ENTER YOUR AGE:")
        try: #check if the value entered is a number
            userAge = int(userAge);
        except:#if the value is not a number re-ask the user to re-enter the value.
            print("Kindly the age should be a number") 
        else:
            return userAge #if the value is accepted end the loop and return the value
        

#A function to check the sex of the user.
def setValueSex():
    while(1): #loop that repeats itself untile the user has entered an acceptable value
        userSex = input("PLEASE DEFINE YOUR SEX : [male] or [female] : ")
        if (userSex =="male" or userSex =="female"):#check the value entered if it is "yes" or "no"
            return userSex #if the value is accepted end the loop and return the value
        else:
            print("kindly the answer should be 'male' or 'female' only")#if the value is not accepted re-ask the user to re-enter the value.



#Define the employment status of the user.
def setValueEmp():
    while(1):#loop that repeats itself untile the user has entered an acceptable value
        employmentStatus = input("ARE YOU CURRENTLY EMPLOYED? [yes] or [no] :")
        if (employmentStatus =="yes" or employmentStatus =="no"): #check the value entered if it is "yes" or "no"
            return employmentStatus #if the value is accepted end the loop and return the value
        else:
            print("kindly the answer should be 'yes' or 'no' only ") #if the value is not accepted re-ask the user to re-enter the value.


#Dose the user hold his/her identity card
def identityCard():
     while(1): #loop that repeats itself untile the user has entered an acceptable value
        identity = input("DO YOU CURRENTLY HOLD YOUR IDENTITY CARD? [yes] or [no] :")
        if identity =="yes" or identity =="no": #check the value entered if it is "yes" or "no"
            return identity #if the value is accepted end the loop and return the value
        else:
            print("kindly the answer should be 'yes' or 'no' only")#if the value is not accepted re-ask the user to re-enter the value.



#A function to process the information and view the required doucument accordingly.
def reqPapers(age,sex,emp,iden):
    print("\nHere are the required doucumnet based on the data you've entered: \n")

    #identity need check
    if (age <18 ):
        print("- A personal record since you are younger than 18.")
    else:
        if (iden == "no"):
            print("- A personal record and a police note since you don't have your identity card")
        else:
            print("- An identity card")

    #check if the user need the his military division approval
    if(sex =="male"):
        if age>=18 and age <=42:
            print("- Recruitment division approval showing your military service status")
    
    #check if the user need the his company approval
    if (emp == "yes") :
        print("- A travele approval from your company")
    



#Welcome message.
print("Welcom to passport doucuments assistance \n\
The programe will ask you several question in order to help you prepare the right doucuments.\n\
Please answer each question correctly. THANK YOU\n")

#Pull the information from the user and save them in variables.
age = setValueAge() #ask the for the user's age
if age >= 18 : #if the user age is equal or older than 18 ask if he has his identity card and his employment status
    iden = identityCard() 
    emp = setValueEmp()
else: #if the user is younger than 18 we don't need to ask fro his identity card and his employment status
    iden = "not required"
    emp = "not required"
sex = setValueSex()

#show the required document according to the entered data.
reqPapers(age,sex,emp,iden)

