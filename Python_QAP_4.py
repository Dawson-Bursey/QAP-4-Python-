# Title: Project 1 - Python - Function and Lists (Individual)

# Discription:  The One Stop Insurance Company needs a program to enter and calculate new insurance policy
# information for its customers. Allow the program to repeat to allow the user to enter as many customers
# as they want. Add at least 3 functions to the program. I will accept the FormatValues library as a function
# option – but you need to add a new function to the library.

# Start Date: November 17, 2023.
# Due Date: November 28, 2023.

# Group # 3.
# Group Members: Dawson Bursey, Dave Husk, Michael Fewer.
# Author: Dawson Bursey.


print(" \n ")   

# LIBRARIES:
import datetime
from datetime import timedelta

#   CONSTANTS:
POLICY_NUMBER = 1944
BASIC_PREMIUM = 869.00
ADDIT_CAR_DISCOUNT = 0.25
EXT_LIABILITY_COVERAGE = 130.00
GLASS_COVERAGE = 86.00
LOANER_CAR_COVERAGE = 58.00
HST_RATE = 0.15
MONTHLY_PROCESS_FEE = 39.99

#   DATES:
invoiceDate = datetime.datetime.now()
invoiceDateDsp = (invoiceDate.strftime("%Y/%m/%d"))

claimDay = invoiceDate.day
claimMonth = invoiceDate.month
claimYear = invoiceDate.year

claimDay = 1
claimDate = datetime.date(claimYear, claimMonth, claimDay)


#   LISTS:
validProvinces = ['ON', 'BC', 'NL', 'PE', 'AB', 'SK', 'MB', 'QC', 'NS', 'NB']
PaymentValidation = ['Monthly', 'Down Pay', 'Full']


#   FUNCTIONS:
def PersonalInfo(): # Top of the Reciept
    global firstName, lastName, address, city, province, postalCode, phoneNumber, fullName
    firstName = str(input("Enter your first name: ")).title()
    lastName = str(input("Enter your last name: ")).title()
    fullName = lastName + " " + firstName
    address =  str(input("Enter you adress: "))
    city = str(input("Enter your city: ")).title()

    province = str(input("Enter your province: ")).upper()
    while province not in validProvinces:
        print("Invalid provance, please enter a valid province (XX): ")
        province = str(input("Enter your province: ")).upper()

    postalCode = str(input("Enter your postal code (X9X9X9): "))
    phoneNumber = str(input("Enter your phone number (09090909090): "))



def InsuranceDetails():
    global numOfCarsInsured, paymentOpt, optGlassCoverage, optLoanerCar, insurancePremium, downPayment

    numOfCarsInsured = int(input("Enter the amount of cars to be insured: "))
    optGlassCoverage = str(input("Would you want optional glass coverage? (Y for yes or N for no): ")).upper()
    if optGlassCoverage == "Y":
        optGlassCoverage = "Yes"
    elif optGlassCoverage == "N":
        optGlassCoverage = "No"
    
    optLoanerCar = str(input("Would you want optional loaner car? (Y for yes or N for no): ")).upper()
    if optLoanerCar == "Y":
        optLoanerCar = "Yes"
    elif optLoanerCar == "N":
        optLoanerCar = "No"

    paymentOpt = str(input("Pick out of the following payment options: Full, Monthly, or Down Pay: ")).title()
    while paymentOpt not in PaymentValidation:
        print("Please pick a valid payment option (Full, Monthly, or Down Payment)")
        paymentOpt = str(input("Pick out of the following payment options: Full, Monthly, or Down Pay: ")).title()

    insurancePremium = BASIC_PREMIUM + (BASIC_PREMIUM * (numOfCarsInsured - 1) * ADDIT_CAR_DISCOUNT)
   

   

def CalcTotalCost():
    global totalCost, hst, totalExtraCost, totalInsurancePremium
    totalExtraCost = EXT_LIABILITY_COVERAGE + GLASS_COVERAGE + LOANER_CAR_COVERAGE
    totalInsurancePremium = insurancePremium + totalExtraCost
    hst = totalInsurancePremium * HST_RATE
    totalCost = totalInsurancePremium + hst



def CalcMonthlyPayment():
    global monthlyPayment, remainingBalance, downPayment, claimDay, claimMonth, claimYear, claimDate
    
    if paymentOpt == "Full":
       monthlyPayment = 0.00
       downPayment = 0.00
       remainingBalance = 0.00
       return totalCost

    elif paymentOpt == "Monthly":
        claimDate = datetime.date(claimYear, claimMonth, claimDay)
        monthlyPayment = (totalCost + MONTHLY_PROCESS_FEE) / 8
        downPayment = 0.00
        remainingBalance = totalCost - monthlyPayment
        return monthlyPayment
        
    
    elif paymentOpt == "Down Pay":
        claimDate = datetime.date(claimYear, claimMonth, claimDay)
        downPayment = float(input("Enter the down pay amount: "))
        remainingBalance = totalCost - downPayment
        monthlyPayment = (remainingBalance + MONTHLY_PROCESS_FEE) / 8
        return monthlyPayment



#   DISPLAY RECEIPT
def displayReceipt():
    dateNum = 1
    claimDay = invoiceDate.day
    claimMonth = invoiceDate.month
    claimYear = invoiceDate.year
    claimMonth = claimMonth + 1
    totalCostDsp  = "${:,.2f}".format(totalCost)
    totalExtraCostDsp = "${:,.2f}".format(totalExtraCost)
    totalInsurancePremiumDsp = "${:,.2f}".format(totalInsurancePremium)
    hstDsp = "${:,.2f}".format(hst)
    downPaymentDsp = "${:,.2f}".format(downPayment)
    remainingBalanceDsp = "${:,.2f}".format(remainingBalance)
    monthlyPaymentDsp = "${:,.2f}".format(monthlyPayment)


    print("")
    print(f"                One Stop Insurance")
    print(f"Invoice Date: {invoiceDateDsp:>36}")
    print(f"{'____':_^50s}")
    print(f"{'Customer Information':^50s}")
    print("")
    print(f"Name (Last/First): {fullName:>31}")
    print(f"Address & City: {address:>21}, {city:>11}")
    print(f"Province: {province:>32}, {postalCode}")
    print(f"Phone number: {phoneNumber:>36}")

    print(f"{'____':_^50}")
    print(f"{'Insurance Details':^50s}")
    print("")
    print(f"Number of cars: {numOfCarsInsured:>34}")
    print(f"Glass coverage: {optGlassCoverage:>34}")
    print(f"Loaner car: {optLoanerCar:>38}")
    print(f"Payment option: {paymentOpt:>34}")

    print(f"{'____':_^50}")
    print(f"{'Total':^50s}")
    print("")
    print(f"Total Insurance Premium: {totalInsurancePremiumDsp:>25}")
    print(f"Total extra cost: {totalExtraCostDsp:>32}")
    print(f"HST: ${hstDsp:>44}")
    print(f"Total cost: {totalCostDsp:>38}")
    print(f"{'____':_^50}")
   
    print(f"{'Payment Information':^50}")
    print("")
    print(f"Total cost: {totalCostDsp:>38}")
    print(f"Down payment: {downPaymentDsp:>36}")
    print(f"Remaining balance: {remainingBalanceDsp:>31}")
    print(f"Monthly payment: {monthlyPaymentDsp:>33}")
    
    print(f"{'____':_^50}")
    print(f"Claim #             Claim Date             $Amount")
    print(f"{'____':_^50}")
   
   #    CLAIMS
    for dateNum in range(1,9):
        if claimMonth >= 12:
            claimYear = claimYear + 1
            claimDay = 1
            claimMonth = 1
        else:
            
            claimMonth = claimMonth + 1
        claimDate = datetime.date(claimYear, claimMonth, claimDay)
        print(f"  {dateNum}.                {claimDate} {monthlyPaymentDsp:>19}")
        
   
    print("")
    
    




#   MAIN PROGRAM / OUTPUT

def main():
    print("")
    PersonalInfo()
    InsuranceDetails()
    CalcTotalCost()
    CalcMonthlyPayment()
    displayReceipt()

main()



print(" \n ")