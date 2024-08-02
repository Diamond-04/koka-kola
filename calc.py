# number = input("Add number here")
# NamburType = int(number)

# if (NamburType % 2 == 0 ):
#     print(f"evenNumber {NamburType}" )
# else:print(f"oddNumber {NamburType}")

month = input("add month number")  
monthType = int(month)
if (monthType == 1 or 2 or 12):
    print(f"Winter")
elif (monthType == 3 or 4 or 5):
    print(f"spring")
elif (monthType == 6 or 7 or 8):
    print(f"Summer")
elif (monthType ==9 or 10 or 11):
    print(f"autumn")
else:print("add number from 1 to 12")