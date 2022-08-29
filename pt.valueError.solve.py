# POINT OF SALE PT GROUP 3

# TITLE OF THE SHOP
from importlib import invalidate_caches


print("*****WINGS CORNER*****")
print("\nSTORE LOG IN")
storelogin = input("CASHIER NAME: ").upper()
# WHILE IS A LOOP THAT EXECUTES SAME BLOCK OVER AND OVER UNTIL GIVEN CONDITION IS SATISFIED
# USED TO LOOP WHEN ANSWER ON "DO YOU WANT TO BUY WINGS?" IS WRONG OR INVALID
while (1):
    answer = input("Do you want to buy wings? (y/n): ").lower()

    # DEFINE ALL WINGS VARIABLE AS 0 SO THAT WHEN PRODUCT IS NOT CHOSEN IT WILL BE ADDED AS 0, OTHERWISE CODE IS ERROR
    wings_1 = 0
    wings_2 = 0
    wings_3 = 0
    wings_4 = 0
    wings_5 = 0
    wings_1_qty = 0
    wings_2_qty = 0
    wings_3_qty = 0
    wings_4_qty = 0
    wings_5_qty = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    total = 0 
    if answer == ('y'):
        print("==================================================")
        print("|MENU                            |CODE | PRICE   |")
        print("--------------------------------------------------")
        print("|> Buffalo Wings                 | [1] | ₱500.00 |")
        print("|> Garlic Parmesan Wings         | [2] | ₱600.00 |")
        print("|> Wings Corner's Original Wings | [3] | ₱650.00 |")
        print("|> BBQ Flavored Wings            | [4] | ₱750.00 |")
        print("|> Spicy Wings                   | [5] | ₱750.00 |")
        print("|> Cash Out                      | [6] |         |")
        print("|> Exit                          | [7] |         |")
        print("==================================================")
        
        # USE WHILE LOOP WHEN ANSWER ON "INPUT CODE" IS WRONG OR INVALID
        while (2):
            try:
                wingscode = int(input("\nInput Code (1-7):\n"))
                if (wingscode == 1):
                    quantity_1 = int(input("Input Quantity:\n"))
                    wings_1 = wings_1 + 500 * quantity_1
                    a = wings_1 / 500
                    wings_1_qty = int(a)
                    total = wings_1 + wings_2 + wings_3 + wings_4 + wings_5
                    print(f"Subtotal:₱{wings_1}")
                    print(f"Total:₱{total}")

                elif (wingscode == 2):
                    quantity_2 = int(input("Input Quantity:\n"))
                    wings_2 = wings_2 + 600 * quantity_2
                    b = wings_2 / 600
                    wings_2_qty = int(b)
                    total = wings_1 + wings_2 + wings_3 + wings_4 + wings_5
                    print(f"Subtotal:₱{wings_2}")
                    print(f"Total:₱{total}")

                elif (wingscode == 3):
                    quantity_3 = int(input("Input Quantity:\n"))
                    wings_3 = wings_3 + 650 * quantity_3
                    c = wings_3 / 650
                    wings_3_qty = int(c)
                    total = wings_1 + wings_2 + wings_3 + wings_4 + wings_5
                    print(f"Subtotal:₱{wings_3}")
                    print(f"Total:₱{total}")

                elif (wingscode == 4):
                    quantity_4 = int(input("Input Quantity:\n"))
                    wings_4 = wings_4 + 750 * quantity_4
                    d = wings_4 / 750
                    wings_4_qty = int(d)
                    total = wings_1 + wings_2 + wings_3 + wings_4 + wings_5
                    print(f"Subtotal:₱{wings_4}")
                    print(f"Total:₱{total}")

                elif (wingscode == 5):
                    quantity_5 = int(input("Input Quantity:\n"))
                    wings_5 = wings_5 + 750 * quantity_5
                    e = wings_5 / 750
                    wings_5_qty = int(e)
                    total = wings_1 + wings_2 + wings_3 + wings_4 + wings_5
                    print(f"Subtotal:₱{wings_5}")
                    print(f"Total:₱{total}")

                elif (wingscode == 6):
                    if total == 0:
                        print("You Didn't order anything!")
                        quit()
                    else:    
                        total = wings_1 + wings_2 + wings_3 + wings_4 + wings_5
                        print(f"\nTotal Amount:₱{total}")

                    while (3):
                        received = float(input("Money Received:\n₱"))

                        # IF MONEY GIVEN BY CUSTOMER IS LESSER THAN THE TOTAL AMOUNT, THEN MONEY IS INSUFFICIENT AND GOES BACK TO "MONEY RECEIVED"
                        if received < total:
                            print("Insufficient Money!")

                        else:
                            change = received - total
                            print(f"\nChange: \n₱{change}\n")
                            customer = input("Customer Name: ").upper()
                            print("============================================================")

                            print("                     SALES INVOICE       ")
                            from datetime import date

                            today = date.today()
                            print(f"-{today}-")
                            print(f"Cashier: {storelogin}")
                            print(f"Customer: {customer}")
                            print("ITEM                     PRICE       QTY         SUBTOTAL")

                            # WILL ONLY PRINT ITEM ON RECEIPT IF IT HAS VALUE GREATER THAN 0
                            if wings_1 > 0:
                                print(f"Buffalo Wings            500         {wings_1_qty}           {wings_1}")
                            if wings_2 > 0:
                                print(f"Garlic Parmesan Wings    600         {wings_2_qty}           {wings_2}")
                            if wings_3 > 0:
                                print(f"Original Wings           650         {wings_3_qty}           {wings_3}")
                            if wings_4 > 0:
                                print(f"BBQ Wings                750         {wings_4_qty}           {wings_4}")
                            if wings_5 > 0: 
                                print(f"Spicy Wings              750         {wings_5_qty}           {wings_5}")
                            print(f"                                           TOTAL:₱{total}")
                            print(f"                                            CASH:₱{received}")
                            print(f"                                          CHANGE:₱{change}")
                            print("\n*****THANK YOU FOR BUYING AT WINGS CORNER! COME AGAIN!*****")
                            print("============================================================")
                            quit()

                elif (wingscode == 7):
                    print("Thank you for using our program!")
                    quit()
                else:
                    print("Invalid Keyword!")          

            # IF CODE INPUT IS GREATER THAN 7, THEN IT IS INVALID AND WHILE LOOP DOES THE JOB
            except ValueError:
                print("Invalid Code! Try Again!")    

    if answer == ('n'):
        print("Thank you for using our program!")
        quit()

    # IF NOT Y OR N IS THE ANSWER, THEN IT IS INVALID AND WHILE LOOP DOES THE JOB
    else:
        print("Invalid Keyword! Try again!3")