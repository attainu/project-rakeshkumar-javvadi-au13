# used for decrementing processing capacity after a defined period of time
import time
import threading                            # to process the multiple task
print("\n" * 5)


class Spiky():
    print("\n" * 5)

    def __init__(self):
        # dict for restaurant name and processing capacity #dict for restaurant name and processing capacity
        self.restaurent_dict = {"PARADISE": 0,
                                "CHINA BISTRO": 0, "CHUTNEYS": 0}
        self.menu_restaurent = {
            "PARADISE": {"IDLY         ": 110, "CHICKEN BIRYANI": 649, "VEG BIRYANI  ": 550, "ROAST CHICKEN": 450,
                         "CHICKEN TIKKA ": 499},

            "CHINA BISTRO": {"VEG SOUP        ": 250, "CHICKEN BIRYANI": 849, "PANEER TIKKA": 350, "SPECIAL MOMO": 399,
                             "CHICKEN LOLLIPOP": 350},
            "CHUTNEYS": {"IDLY         ": 190, "MASALA DOSA ": 150, "UPMA PESARATU   ": 129, "SPECIALPOORI ": 199}}  # dict to maintain the records of food_item and food_price with reference to restaurant name

        self.auth = {"PARADISE": {"pallavi": 123},


                     "CHINA BISTRO": {"chintu": 123},

                     "CHUTNEYS": {"rakesh": 123}}

    def mainMenu(self):
        while True:
            print("\n")
            print("#"*35, "WELCOME TO SPIKY", "#"*35)
            print("\n"*2)
            print("#"*39, "MAIN MENU", "#"*39)  # Design for Main Menu
            print("(O) ORDER FOOD" + "\n"
                  "(J) JOIN SERVICES\n"
                  "(E) EXIT\n")
            print("-"*89)
            mm_input = input("PLEASE SELECT YOUR OPERATION: ").upper()
            if (mm_input == "O"):
                self.orderFood()  # Calling orderFood() function
                break
            elif (mm_input == "J"):
                self.joinServices()  # Calling joinServices()
                break
            elif (mm_input == "E"):
                print("#"*39, "THANK YOU", "#"*39)
                exit()  # exiting main function and terminating the code
                break
            else:
                print("\n" + "ERROR: Invalid Input (" +
                      str(mm_input) + "). Try again!")  # Invalid input

    def orderFood(self):  # Order food menu
        while True:
            print("\n"*1)
            print("#"*39, "ORDER FOOD", "#"*39)
            print("PLEASE SELECT THE RESTAURENT OF YOUR CHOICE FROM BELOW OPTIONS: \n")
            # itterating over the restaurants names with referrence to count
            for i in range(0, len(self.restaurent_dict)):
                # converting restaurant names into list and printing them along with count which increases with each itteration
                print("(", i+1, ")", " ",
                      (list(self.restaurent_dict.keys())[i]), sep='')
                print()
            print()
            print("(M) BACK TO MAIN MENU", "\t"*5,
                  "(S) SEARCH FOR DISH / RESTAURENT")
            print("-"*89)
            # input for operation to be performed in orderFood function
            of_input = input("PLEASE SELECT YOUR OPERATION: ")
            num_input_check = []
            if of_input.upper() == "M":
                # calling mainMenu function and breaking the current function loop
                self.mainMenu()
                break
            elif of_input.upper() == "S":
                # calling search_Menu() function and breaking the current function loop
                self.search_Menu()
                break
            elif of_input != "M" or of_input != "S":
                for i in of_input:
                    # checking for the input whether integer or not
                    if ord(i) >= 48 and ord(i) <= 57:
                        num_input_check.append("True")
                    else:
                        num_input_check.append("False")
            if "False" in num_input_check:
                print("\n" + "ERROR: Invalid Input (",
                      of_input, "). Try again!", sep='')
            else:
                of_input = int(of_input)
                if of_input <= len(self.restaurent_dict):
                    # Calling restaurant_Menu function with argument as user defined restaurant name and breaking the current function loop
                    self.restaurent_Menu(
                        list(self.restaurent_dict.keys())[of_input-1])
                    break
                else:
                    print("\n" + "ERROR: Invalid Input (",
                          of_input, "). Try again!", sep='')

                    # dict ot maintain the records of username and password with reference to restaurant name

    def restaurent_Menu(self, res):
        # it will check for the processing capacity of that particualr restaurant in restaurant_dict
        if self.restaurent_dict[res] > 2:
            print("SORRY WE ARE CURRENTLY NOT ACCEPTING ANY ORDERS FOR THIS RESTAURENT!")
            self.orderFood()  # if the processing capacity is greater than 2, than it wont accept further orders untill processing capacity decreases
        else:
            dish_input_food_list = []  # for appending only user defined food item names
            dish_input_price_list = []  # for appending only user defined food_item prices
            dish_quantity_list = []  # for keeping the count of every dish selected by user
            while True:
                print("\n"*2)
                print("#"*34, "MENU OF", res, "#"*34)
                print("\n"*2)
                if res in self.menu_restaurent:
                    print("ITEMS", "\t"*9, "PRICE")
                    print("-"*89)
                    i = 0
                    for k, v in self.menu_restaurent[res].items():
                        i += 1
                        # print menu of the restaurent
                        print("(", i, ")", " ", k, "\t"*7, v, sep="")
                    print("-"*89)
                    print("(V) VIEW CART", "\t"*7,
                          "(B) BACK TO ORDER FOOD PAGE")
                    print("-"*89)
                    dish_input = input("PLEASE SELECT DISH OF YOUR CHOICE: ")
                num_input_check = []
                if dish_input.upper() == "B":
                    # gets u back to previous menu
                    self.orderFood()
                    break
                elif dish_input.upper() == "V":
                    print("\n"*2)
                    print("#"*39, "YOUR CART", "#"*39)
                    # if all the list are empty at initial stage then it wont call the cart function
                    if dish_input_food_list != [] and dish_input_price_list != [] and dish_quantity_list != []:
                        self.cart(dish_input_food_list,
                                  dish_input_price_list, dish_quantity_list, res)
                        break
                    else:                                           # when cart is empty
                        print("\n"*2)
                        print("\t"*4, "YOUR CART IS EMPTY!!")
                        continue
                elif dish_input != "V" or dish_input != "B":
                    for i in dish_input:
                        # when input is not either V nor B then it will check if the number is integer
                        if ord(i) >= 48 and ord(i) <= 57:
                            num_input_check.append("True")
                        else:
                            num_input_check.append("False")
                    if "False" in num_input_check:
                        # displays error if input is not a number nor either V or B
                        print("\n" + "ERROR: Invalid Input (",
                              dish_input, "). Try again!", sep='')
                    else:
                        # created a list to add food_item name and food_item price
                        food_and_price_list = []
                        dish_input = int(dish_input)
                        if dish_input <= len(self.menu_restaurent[res].items()):
                            try:
                                dish_quantity = int(
                                    input("PLEASE SELECT THE QUANTITY FOR THE DISH SELECTED: "))
                                dish_quantity_list.append(dish_quantity)
                            except Exception:
                                print("\n" + "ERROR: Invalid Input. Try again!")
                                continue
                            print("\n"*2)
                            for food, price in self.menu_restaurent[res].items():
                                # appending the food_item name to the list above defined
                                food_and_price_list.append(food)
                                # appending the food_item price to the list above defined
                                food_and_price_list.append(price)
                            # now appending the exact user defined food name from the list to another list
                            dish_input_food_list.append(
                                food_and_price_list[(dish_input)*2-2])
                            # now appending the exact user defined food price from the list to another list
                            dish_input_price_list.append(
                                food_and_price_list[dish_input*2-1])
                            print("#"*34, "TEST", "#"*34)
                            print("\n"*2)
                        else:
                            print("\n" + "ERROR: Invalid Input (",
                                  dish_input, "). Try again!", sep='')
                else:
                    print("\n" + "ERROR: Invalid Input (",
                          dish_input, "). Try again!", sep='')

    def cart(self, dish_input_food_list, dish_input_price_list, dish_quantity_list, res):
        while True:
            total_price = []
            j = 0
            while j < len(dish_input_price_list):
                # will append the (dish price x dish quantity) value in the total price list above
                total_price.append(
                    (dish_quantity_list[j])*(dish_input_price_list[j]))
                j += 1
            print("\n")
            print("-"*89)
            print("ITEMS", "\t"*5, "QUANTITY", "\t"*4, "PRICE")
            print("-"*89)
            i = 0
            sr_no = 1
            while i < len(dish_input_food_list):
                print("(", sr_no, ")", " ", dish_input_food_list[i], "\t", "*", "\t"*2, dish_quantity_list[i],
                      "\t"*5, total_price[i], sep="")
                i += 1
                sr_no += 1
            print("-"*89)
            # will display the total of the whole cart amount
            print("TOTAL", "\t"*10, sum(total_price))
            if sum(total_price) >= 1000:
                print("DISCOUNT RECEIVED", "\t"*3, "15%", "\t" *
                      5, "-", (15*(sum(total_price))/100), sep="")
                # created a check if the total cart amount is more than 3500 then it will calculate 15% discount on whole amount
                discount_total_price = float(
                    sum(total_price)) - (15*(sum(total_price))/100)
                print("TOTAL", "\t"*10, (discount_total_price))
            print("-"*89)
            print("(P) PAYMENT", "\t"*8, "(B) BACK TO MENU")
            print("-"*89)
            cart_input = input("PLEASE SELECT YOUR OPERATION: ")
            if cart_input.upper() == "B":
                # take your back to the previous menu
                self.restaurent_Menu(res)
                break
            elif cart_input.upper() == "P":
                self.payment(res)  # take you to the payment option menu
                break
            else:
                print("\n" + "ERROR: Invalid Input (",
                      cart_input, "). Try again!", sep='')

    def payment(self, res):
        while True:
            print("\n")
            print("#"*39, "PAYMENT", "#"*39)
            print("\n")
            # Displays the list of payment modes
            print("SR NO", "\t"*2, "MODES OF PAYMENT")
            print("-"*89)
            print("(1)", "\t"*2, "CREDIT CARD")
            print("(2)", "\t"*2, "DEBIT CARD")
            print("(3)", "\t"*2, "NET BANKING")
            print("(4)", "\t"*2, "UPI PAYMENT")
            print("(5)", "\t"*2, "COD")
            print("-"*89)
            print("(C)", "\t"*2, "CANCEL PAYMENT")
            print("-"*89)
            payment_input = input("PLEASE SELECT YOUR OPERATION: ").upper()
            if payment_input == "C":
                self.restaurent_Menu(res)
                break
            elif payment_input == "1" or payment_input == "2" or payment_input == "3" or payment_input == "4" or payment_input == "5":
                # here the processing capacity count is incremented for the particular restaurant in restaurant_dict
                self.restaurent_dict[res] += 1
                self.payment_Status(res)
                break
            else:
                print("\n" + "ERROR: Invalid Input (",
                      payment_input, "). Try again!", sep='')

                # queue list will maintain list of thread with reference to the restaurent

    def payment_Status(self, res):
        # queue list will maintain list of thread with reference to the restaurent
        self.queueList = []
        while True:
            print("\n")
            print("Your payment is in progress.....")
            print()
            time.sleep(4)
            print("\n")
            print("#"*36, "PAYMENT STATUS", "#"*39)
            print("\n"*3)
            print("\t"*4, "PAYMENT SUCCESSFUL")
            print("\n"*3)
            print("Your Food is preparing......")
            print()

            time.sleep(6)

            print("Your food is ready to deliver. It will reach by you in 15 minutes :)")
            print()
            print("*"*39, "THANK YOU", "*"*39)

            print()
            print("-"*89)
            print("(M)", "\t", "BACK TO MAIN MENU")
            print("-"*89)

            # process of each thread with reference to each restaurant
            def endHotelProcess(res):
                while(self.restaurent_dict[res] != 0):
                    # processing capacity count will decrement after very 30 sec, unless the count = 0
                    time.sleep(1000)
                    self.restaurent_dict[res] -= 1
            # thread created for the process(endHotelProcess)
            t1 = threading.Thread(target=endHotelProcess, args=(res,))
            self.queueList.append(t1)  # appending the thread to queueList
            self.queueList[-1].start()  # starting the thread in the queueList
            payment_Status_input = input(
                "PLEASE SELECT YOUR OPERATION: ").upper()
            if payment_Status_input == "M":
                self.mainMenu()  # getting back to mainMenu
                break
            else:
                print("\n" + "ERROR: Invalid Input (",
                      payment_Status_input, "). Try again!", sep='')

    def joinServices(self):
        while True:
            print("\n")
            print("#"*35, "JOIN OUR SERVICES", "#"*35)
            print("\n")
            print("-"*89)
            print("(1) NEW USER")
            print("(2) EXSISTING USER")
            print("\n"*2)
            print("-"*89)
            print("(M) BACK TO MAIN MENU")
            print("-"*89)
            joinServices_input = input(
                "PLEASE SELECT YOUR OPERATION: ").upper()
            if joinServices_input == "M":
                self.mainMenu()
                break
            elif joinServices_input == "1":
                # will call the new_User function which will ask for registration process
                self.new_User()
                break
            elif joinServices_input == "2":
                # will call exisiting_User function which will ask for authentication
                self.exsisting_User()
                break
            else:
                print("\n" + "ERROR: Invalid Input (",
                      joinServices_input, "). Try again!", sep='')

    def new_User(self):
        while True:
            print("\n")
            print("#"*32, "COMPLETE YOUR REGISTRATION PROCESS", "#"*32)
            print("\n")
            print("-"*89)
            print("(J) BACK TO JOIN SERVICES PAGE")
            print("-"*89)
            new_user_id = input("PLEASE ENTER YOUR USERNAME: ")
            new_user_pwd = int(input("PLEASE ENTER YOUR PASSWORD: "))
            new_user_restaurant = input(
                "PLEASE ENTER NAME OF YOUR RESTAURANT OR OPERATION TO BE PERFORMED: ").upper()
            if new_user_restaurant == "J":
                self.joinServices()  # if user wants to go back to previosu menu
                break
            # will check and proceed only if the entered restaurent already esist in dict
            elif new_user_restaurant not in self.restaurent_dict:
                id_pwd = {}
                id_pwd.setdefault(new_user_id, new_user_pwd)
                # have added new restaurent name along with usename and passwordas its value in auth_Dict
                self.auth[new_user_restaurant] = id_pwd
                self.restaurent_dict[new_user_restaurant] = 0
                dish_price = {}
                while True:                  # this loop will keep on asking user about the dish to be added in menu
                    dish = (
                        input("PLEASE ENTER YOUR DISH NAME TO BE ADDED IN MENU: ").upper())
                    price = int(
                        input("PLEASE ENTER THE AMOUNT FOR THE ABOVE DISH: "))
                    print("-"*89)
                    print("(A) ADD MORE ITEMS", "\t" *
                          7, "(D) DONE ADDING ITEMS")
                    new_user_add_menu = input(
                        "PLEASE SELECT OPERATION TO BE PERFORMED: ").upper()
                    dish_price.setdefault(dish, price)
                    self.menu_restaurent[new_user_restaurant] = dish_price
                    if new_user_add_menu == "D":  # if user is done with adding items, he will be directed to main menu then
                        print("\n"*2)
                        print("\t"*3, "DETAILS ADDED SUCCESSFULLY!!")
                        print("\n"*2)
                        self.mainMenu()
                        break
                    elif new_user_add_menu != "A":  # if any other input other than D or A then it will display error and the loop will run again
                        print("PLEASE ENTER VALID INPUT!!")
            elif new_user_restaurant in self.restaurent_dict:
                print("THE ENTERED RESTAURANT NAME ",
                      new_user_restaurant, " ALREADY EXSIST")
            else:
                print("\n" + "ERROR: Invalid Input (",
                      new_user_restaurant, "). Try again!", sep='')

    def exsisting_User(self):
        while True:
            print("\n"*2)
            print("#"*32, "WELCOME TO SWIGGY SERVICES", "#"*32)
            print("\n"*3)
            print("-"*89)
            print("(T) TRY AGAIN", "\t"*4, "(M) BACK TO MAIN MENU")
            print("-"*89)
            exsisting_user_id = input("PLEASE ENTER USERNAME: ")
            exsisting_user_pwd = int(input("PLEASE ENTER PASSWORD: "))
            # exsisting_user_input = input("PLEASE SELECT OPERATION TO BE PERFORMED: ")
            for k, v in self.auth.items():
                # check if the username and password in auth_dict
                if exsisting_user_id in v and exsisting_user_pwd in v.values():
                    self.update_Menu(k)
                    break
            print(
                "\n" + "ERROR: Incorrect Username or Password entered. Try again!", sep='')
            print("-"*89)
            # if user want to go back hence taking another input
            exsisting_user_input = input(
                "PLEASE SELECT OPERATION TO BE PERFORMED: ").upper()
            if exsisting_user_input == "M":
                self.mainMenu()  # back to main menu
                break
            elif exsisting_user_input == "T":
                continue
            else:
                print("\n" + "ERROR: Invalid Input (",
                      exsisting_user_input, "). Try again!", sep='')

    def update_Menu(self, k):
        while True:
            if k in self.menu_restaurent:
                print("#"*35, "MENU OF", k, "#"*35)
                print("\n")
                print("-"*89)
                print("ITEMS", "\t"*9, "PRICE")
                print("-"*89)
                i = 0
                # itterate over food_name and food_price with reference to restaurant name(k)
                for r, v in self.menu_restaurent[k].items():
                    i += 1
                    # displays menu of restaurant k
                    print("(", i, ")", " ", r, "\t"*7, v, sep="")
                print("-"*89)
                print("(A) ADD NEW DISH", "\t"*2,
                      "(M) BACK TO MAIN MENU", "\t"*2, "(R) REMOVE DISH")
                print("-"*89)
                update_menu_input = input(
                    "PLEASE ENTER DISH NAME TO BE UPDATED OR SELECT ANY OPERATION TO BE PERFORMED: ").upper()
                if update_menu_input in self.menu_restaurent[k]:
                    price = input("PLEASE ENTER THE NEW PRICE: ")
                    # updates the price of the dish which is alreayd present in menu
                    self.menu_restaurent[k][update_menu_input] = price
                elif update_menu_input == "M":
                    self.mainMenu()                              # back to main menu
                    break
                elif update_menu_input == "A":
                    # for adding new dish
                    self.add_Dish(k)
                    break
                elif update_menu_input == "R":
                    # for removing existing dish
                    self.remove_Dish(k)
                    break
                else:
                    print("\n" + "ERROR: Invalid Input (",
                          update_menu_input, "). Try again!", sep='')
            else:
                print(
                    "\n" + "ERROR: Incorrect Username or Password entered. Try again!", sep='')

    def add_Dish(self, k):
        while True:
            print("\n")
            print("#"*20, "PLEASE ENTER DETAILS OF YOUR DISH TO BE ADDED", "#"*20)
            print("\n"*2)
            print("-"*89)
            dish = (
                input("PLEASE ENTER YOUR DISH NAME TO BE ADDED IN MENU: ").upper())
            price = int(input("PLEASE ENTER THE AMOUNT FOR THE ABOVE DISH: "))
            # check if the input dish name is in menu
            if dish not in self.menu_restaurent[k]:
                self.menu_restaurent[k][dish] = price
            print("-"*89)
            print("(A) ADD MORE ITEMS", "\t"*6, "(D) DONE ADDING ITEMS")
            add_dish_input = input(
                "PLEASE SELECT OPERATION TO BE PERFORMED: ").upper()
            # will end the current function loop and take back to main menu once all dishes are added
            if add_dish_input == "D":
                print("\n"*2)
                print("\t"*3, "DETAILS ADDED SUCCESSFULLY!!")
                print("\n"*2)
                self.update_Menu(k)
                break
            # unless user dont select either of valid inputs A or D, the loop will run continously
            elif add_dish_input != "A":
                print("PLEASE ENTER VALID INPUT!!")

    def remove_Dish(self, k):
        while True:
            print("\n")
            print("#"*20, "PLEASE ENTER NAME OF THE DISH TO BE REMOVED", "#"*20)
            print("\n"*2)
            print("-"*89)
            print("(T) TRY AGAIN", "\t"*5, "(B) BACK TO UPDATE MENU PAGE")
            print("-"*89)
            dish = (input("PLEASE ENTER YOUR DISH NAME TO BE REMOVED: ").upper())
            # check if the dish is present in menu
            if dish in self.menu_restaurent[k]:
                # deleted the dish from the menu
                del self.menu_restaurent[k][dish]
                # going back to previous menu
                self.update_Menu(k)
                break
            else:
                print("\n" + "ERROR: (", dish,
                      "). not found in Menu. Try again!", sep='')
            print("-"*89)
            remove_dish_input = input(
                "ENTER OPERATION TO BE PERFORMED: ").upper()
            # if user wishes to go back to previous menu without removing any dish
            if remove_dish_input == "B":
                self.update_Menu(k)
                break
            elif remove_dish_input != "T":
                print("\n" + "ERROR: Invalid Input (",
                      remove_dish_input, "). Try again!", sep='')

    def search_Menu(self):
        long = []
        flag = 0
        while True:
            print("\n")
            print("#"*35, "SEARCH MENU", "#"*35)
            print("\n"*2)
            print("-"*89)
            print("(B) BACK TO ORDER FOOD PAGE")
            print("-"*89)
            dish = (input("PLEASE ENTER DISH NAME : ").upper())
            sr_no = 1
            for i, j in self.menu_restaurent.items():
                for k, v in j.items():  # for dish and price in restaurant
                    if k.startswith(dish):          # if dish starts with user input
                        print("\n")
                        print("-"*89)
                        print("(", sr_no, ")", " ", i, sep="")
                        sr_no += 1
                        flag += 1
                        long.append(i)
                        print("DISH NAME: ", k, "\t"*6, "PRICE: ", v)
                        print("-"*89)
            if flag == 0:
                print("\n" + "ENTERED DISH (", dish,
                      ") NOT FOUND. TRY AGAIN!", sep='')
                continue
            else:
                while True:  # loop will run again until user inputs valid option
                    try:                                  # exceptional error handling for if the input entered is not integer
                        self.search_menu_input = input(
                            "PLEASE SELECT RESTAURANT: ")
                        self.search_menu_input = int(self.search_menu_input)
                        break
                    except ValueError:
                        print("NO VALID INPUT!! PLEASE TRY AGAIN ...")
                if long != []:
                    try:
                        # if list of the search result is not empty, this will call restaurent_Menu function with reference to user defined choice
                        self.restaurent_Menu(long[self.search_menu_input-1])
                        break
                    except IndexError:
                        print("NO VALID INPUT!! PLEASE TRY AGAIN ...")
                        self.search_Menu()
                        break
                else:
                    print("\n" + "ENTERED DISH (", dish,
                          ") NOT FOUND. TRY AGAIN!", sep='')


if __name__ == "__main__":
    s = Spiky()
    s.mainMenu()
