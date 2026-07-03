# Loan_Category =("House Loan","Personal Loan","Car loan")
# HLoan=[5000000,7000000,9000000]
# PLoan=[2000000,4000000,6000000]
# CLoan=[1000000,2000000,3000000]
# i=1
# print("Welcome to the Bank Loan Application")
#
# Name= input("Enter your Name")
# Age= input("Enter your Age")
# for x in Loan_Category:
#     print(f"{i}. {x}")
#     i+=1
# category=int(input("Enter your Loan Category Number"))
# match category:
#     case 1 :print("You have selected", Loan_Category[0])
#     case 2 :print("You have selected", Loan_Category[1])
#     case 3 :print("You have selected", Loan_Category[2])
#     case _:print("Enter the valid no")
#     #Return
# User_Loan =HLoan if category==1 else CLoan if category==2 else PLoan if category==3 else ("Enter the valid no")
# salary=int(input("Enter your Salary"))
# if category==1:
#     if salary>=675000:
#         print("You are Eligible for category 3 which is PKR 9000000")
#     elif salary>=350000:
#         print("You are Eligible for category 2 which is PKR 7000000")
#     elif salary>=125000:
#         print("You are Eligible for category 1 which is PKR 5000000")
#     else :
#         print("You are not eligible for any category in User_Loan")
#
# elif category==2:
#     if salary>=450000:
#         print("You are Eligible for category 3 which is PKR 6000000")
#     elif salary>=200000:
#         print("You are Eligible for category 2 which is PKR 4000000")
#     elif salary>=50000:
#         print("You are Eligible for category 1 which is PKR 2000000")
#     else :
#         print("You are not eligible for any category in User_Loan")
#
# elif category==3:
#     if salary>=225000:
#         print("You are Eligible for category 3 which is PKR 3000000")
#     elif salary>=100000:
#         print("You are Eligible for category 2 which is PKR 2000000")
#     elif salary>=25000:
#         print("You are Eligible for category 1 which is PKR 1000000")
#     else :
#         print("You are not eligible for any category in User_Loan")


Loan_Category =("House Loan","Personal Loan","Car loan")
HLoan=[5000000,7000000,9000000]
PLoan=[2000000,4000000,6000000]
CLoan=[1000000,2000000,3000000]
Hloanrange=(125000,350000,675000)
CLoanrange=(25000,100000,225000)
PLoanrange=(50000,200000,450000)
i=1
print("Welcome to the Bank Loan Application")
Name= input("Enter your Name")
Age= input("Enter your Age")
for x in Loan_Category:
    print(f"{i}. {x}")
    i+=1
category=int(input("Enter your Loan Category Number"))
match category:
    case 1 :print("You have selected", Loan_Category[0])
    case 2 :print("You have selected", Loan_Category[1])
    case 3 :print("You have selected", Loan_Category[2])
    case _:print("Enter the valid no")
def Calc(HLoan,HLoanrange):
    if salary>=HLoanrange[2]:print("You are Eligible for category 1 which is PKR",HLoan[2])
    elif salary>=HLoanrange[1]:print("You are Eligible for category 2 which is PKR",HLoan[1])
    elif salary>=HLoanrange[0]:print("You are Eligible for category 1 which is PKR",HLoan[0])
    else:print("You are not eligible for any category")
User_Loan =HLoan if category==1 else CLoan if category==2 else PLoan if category==3 else ("Enter the valid no")
salary=int(input("Enter your Salary"))
if category==1:
    Calc(HLoan,Hloanrange)
elif category==2:
    Calc(PLoan,PLoanrange)
elif category==3:
    Calc(CLoan,CLoanrange)
else:print("You didnt selected  any category")