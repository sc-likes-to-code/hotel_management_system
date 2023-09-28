
import mysql.connector
# GLOBAL VARIABLES DECLARATION
myConnnection =""
cursor=""
userName=""
password =""
roomrent =0
restaurantbill=0
gamingbill=0
fashionbill=0
totalAmount=0
cid=""
#MODULE TO CHECK MYSQL CONNECTIVITY
def MYSQLconnectionCheck ():
    global myConnection
    global userName
    global password
    userName = input("\n ENTER MYSQL SERVER'S USERNAME : ")
    password = input("\n ENTER MYSQL SERVER'S PASSWORD : ")
    myConnection=mysql.connector.connect(host="localhost",user=userName,passwd=password ,
    auth_plugin='mysql_native_password' )
    if myConnection:
        print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED !")
        cursor=myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS HMS")
        cursor.execute("COMMIT")
        cursor.close()
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")

#MODULE TO ESTABLISH MYSQL CONNECTION
def MYSQLconnection ():
    global userName
    global password
    global myConnection
    global cid
    myConnection=mysql.connector.connect(host="localhost", user=userName, passwd=password, database="HMS", auth_plugin='mysql_native_password' )
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
    myConnection.close()

#MODULE TO INSERT CUSTOMER DETAILS INTO TABLE C_Details
def userEntry():
    global cid
    if myConnection:
        createTable ="""CREATE TABLE IF NOT EXISTS C_DETAILS(CID VARCHAR(20) PRIMARY KEY,C_NAME VARCHAR(30),C_ADDRESS VARCHAR(30),C_AGE VARCHAR(30), C_COUNTRY VARCHAR(30) ,P_NO VARCHAR(30),C_EMAIL VARCHAR(30))"""
        cursor=myConnection.cursor()
        cursor.execute(createTable)
        cid = input("Enter Customer Identification Number : ")
        name = input("Enter Customer Name : ")
        address = input("Enter Customer Address : ")
        age= input("Enter Customer Age : ")
        nationality = input("Enter Customer Country : ")
        phoneno= input("Enter Customer Contact Number : ")
        email = input("Enter Customer Email : ")
        sql = "INSERT INTO C_Details VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values= (cid,name,address,age,nationality,phoneno,email)
        cursor.execute(sql,values)
        cursor.execute("COMMIT")
        print("\nNew Customer Entered In The System Successfully !")
        cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")

#MODULE TO INSERT CUSTOMER BOOKING RECORDS INTO TABLE BOOKING_RECORD
def bookingRecord():
    global cid
    customer=searchCustomer()
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS BOOKING_RECORD(CID VARCHAR(20) PRIMARY KEY,CHECK_IN DATE ,CHECK_OUT DATE)"
            cursor.execute(createTable)
            checkin=input("\n Enter Customer CheckIN Date [ YYYY-MM-DD ] : ")
            checkout=input("\n Enter Customer CheckOUT Date [ YYYY-MM-DD ] : ")
            sql= "INSERT INTO BOOKING_RECORD VALUES(%s,%s,%s)"
            values= (cid,checkin,checkout)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("\nCHECK-IN AND CHECK-OUT ENTRY MADE SUCCESSFULLY !")
            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

#MODULE TO INSERT ROOM CHOICE, NO. OF DAYS, ROOM NO., ROOM RENT AMOUNT INTO TABLE ROOM_RENT ACCORDING TO CUSTOMER ID
def roomRent():
    global cid
    customer=searchCustomer()
    if customer:
        global roomrent
        if myConnection:
            cursor=myConnection.cursor()
            createTable ="""CREATE TABLE IF NOT EXISTS ROOM_RENT(CID VARCHAR(20) PRIMARY KEY,ROOM_CHOICE INT,NO_OF_DAYS INT,ROOMNO INT ,ROOMRENT INT)"""
            cursor.execute(createTable)
            print ("\n ##### We have The Following Rooms For You #####")
            print (" 1. Ultra Royal ----> 10000 Rs.")
            print (" 2. Royal ----> 5000 Rs. ")
            print (" 3. Elite ----> 3500 Rs. ")
            print (" 4. Budget ----> 2500 Rs. ")
            roomchoice =int(input("Enter Your Option : "))
            roomno=int(input("Enter Customer Room No : "))
            noofdays=int(input("Enter No. Of Days : "))
            if roomchoice==1:
                roomrent = noofdays * 10000
                print("\nUltra Royal Room Rent : ",roomrent)
            elif roomchoice==2:
                roomrent = noofdays * 5000
                print("\nRoyal Room Rent : ",roomrent)
            elif roomchoice==3:
                roomrent = noofdays * 3500
                print("\nElite Royal Room Rent : ",roomrent)
            elif roomchoice==4:
                roomrent = noofdays * 2500
                print("\nBudget Room Rent : ",roomrent)
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                return
            sql= "INSERT INTO ROOM_RENT VALUES(%s,%s,%s,%s,%s)"
            values= (cid,roomchoice,noofdays,roomno,roomrent,)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("Thank You , Your Room Has Been Booked For : ",noofdays , "Days" )
            print("Your Total Room Rent is : Rs. ",roomrent)
            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

#MODULE TO CALCULATE RESTAURANT BILL AND INSERT DATA INTO TABLE RESTAURANT
def Restaurant():
    global cid
    customer=searchCustomer()
    if customer:
        global restaurantbill
        if myConnection:
            cursor=myConnection.cursor()
            createTable ="""CREATE TABLE IF NOT EXISTS RESTAURANT(CID VARCHAR(20) PRIMARY KEY,CUISINE VARCHAR(30),QUANTITY VARCHAR(30),BILL VARCHAR(30)) """
            cursor.execute(createTable)
            print("1. Vegetarian Combo -----> 300 Rs.")
            print("2. Non-Vegetarian Combo -----> 500 Rs.")
            print("3. Vegetarian & Non-Vegetarian Combo -----> 750 Rs.")
            choice_dish = int(input("Enter Your Cuisine : "))
            quantity=int(input("Enter Quantity : "))
            if choice_dish==1:
                print("\nSO YOU HAVE ORDER: Vegetarian Combo ")
                restaurantbill = quantity * 300
            elif choice_dish==2:
                print("\nSO YOU HAVE ORDER: Non-Vegetarian Combo ")
                restaurantbill = quantity * 500
            elif choice_dish==3:
                print("\nSO YOU HAVE ORDER: Vegetarian & Non-Vegetarian Combo ")
                restaurantbill= quantity * 750
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                return
            sql= "INSERT INTO RESTAURANT VALUES(%s,%s,%s,%s)"
            values= (cid,choice_dish,quantity,restaurantbill)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("Your Total Bill Amount Is : Rs. ",restaurantbill)
            print("\n\n**** WE HOPE YOU WILL ENJOY YOUR MEAL ****\n\n" )
            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

#MODULE TO CALCULATE GAMING BILL AND INSERT DATA INTO TABLE GAMING
def Gaming():
    global cid
    customer=searchCustomer()
    if customer:
        global gamingbill
        if myConnection:
            cursor=myConnection.cursor()
            createTable ="""CREATE TABLE IF NOT EXISTS GAMING(CID VARCHAR(20) PRIMARY KEY,GAMES VARCHAR(30),HOURS VARCHAR(30),GAMING_BILL VARCHAR(30))"""
            cursor.execute(createTable)
            print("""
            1. Table Tennis -----> 150 Rs./HR
            2. Bowling -----> 100 Rs./HR
            3. Snooker -----> 250 Rs./HR
            4. VR World Gaming -----> 400 Rs./HR
            5. Video Games -----> 300 Rs./HR
            6. Swimming Pool Games -----> 350 Rs./HR
            7. Exit
            """)
            game=int(input("Enter What Game You Want To Play : "))
            hour=int(input("Enter No Of Hours You Want To Play : "))
            print("\n\n#################################################")
            if game==1:
                print("YOU HAVE SELECTED TO PLAY : Table Tennis")
                gamingbill = hour * 150
            elif game==2:
                print("YOU HAVE SELECTED TO PLAY : Bowling")
                gamingbill = hour * 100
            elif game==3:
                print("YOU HAVE SELECTED TO PLAY : Snooker")
                gamingbill = hour * 250
            elif game==4:
                print("YOU HAVE SELECTED TO PLAY : VR World Gaming")
                gamingbill = hour * 400
            elif game==5:
                print("YOU HAVE SELECTED TO PLAY : Video Games")
                gamingbill = hour * 300
            elif game ==6:
                print("YOU HAVE SELECTED TO PLAY : Swimming Pool Games")
                gamingbill = hour * 350
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                return
            sql= "INSERT INTO GAMING VALUES(%s,%s,%s,%s)"
            values= (cid,game,hour,gamingbill)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("Your Total Gaming Bill Is : Rs. ",gamingbill)
            print("FOR : ",hour," HOURS","\n *** WE HOPE YOU WILL ENJOY YOUR GAME ***")
            print("\n\n#################################################")
            cursor.close()
        else:
            print("ERROR ESTABLISHING MYSQL CONNECTION !")

#MODULE TO CALCULATE FASHION BILL AND INSERT DATA INTO TABLE FASHION
def Fashion():
    global cid
    customer=searchCustomer()
    if customer:
        global fashionbill
        if myConnection:
            cursor=myConnection.cursor()
            createTable ="""CREATE TABLE IF NOT EXISTS FASHION(CID VARCHAR(20) PRIMARY KEY,DRESS VARCHAR(30),AMOUNT VARCHAR(30),BILL VARCHAR(30))"""
            cursor.execute(createTable)
            print("""
            1. Shirts -----> Rs. 3500
            2. T-Shirts -----> Rs. 2500
            3. Pants -----> Rs. 2200
            4. Jeans -----> Rs. 3500
            5. Tassel top -----> Rs. 1200
            6. Gown -----> Rs. 3500
            7. Western dress -----> Rs. 4500
            8. Skirts -----> Rs. 2000
            9. Trousers -----> Rs. 2100
            10. InnerWear -----> Rs. 800
            """)

            dress=int(input("Enter the your Choice wear: "))
            quantity=int(input("How many you want to buy: "))
            if dress==1:
                print("\nShirts")
                fashionbill = quantity * 3500
            elif dress==2:
                print("\nT-Shirts")
                fashionbill = quantity * 2500
            elif dress==3:
                print("\nPants")
                fashionbill = quantity * 2200
            elif dress==4:
                print("\nJeans")
                fashionbill = quantity * 3500
            elif dress==5:
                print("\nTassel top")
                fashionbill = quantity * 1200
            elif dress==6:
                print("\nGown")
                fashionbill = quantity * 3500
            elif dress==7:
                print("\nWestern dress")
                fashionbill = quantity * 4500
            elif dress==8:
                print("\nSkirts")
                fashionbill = quantity * 2000
            elif dress==9:
                print("\nTrousers")
                fashionbill = quantity * 2100
            elif dress==10:
                print("\nInnerWear")
                fashionbill = quantity * 800
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
                return
            sql= "INSERT INTO FASHION VALUES(%s,%s,%s,%s)"
            values= (cid,dress,quantity,fashionbill)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            print("\n\n#################################################")
            print("\nYOU SELECT ITEM NO : ",dress,"\nYOUR QUANTITY IS : ",quantity," ITEMS","\nTHANK YOU FOR SHOPPING VISIT AGAIN!!!" )
            print("\nYour Total Bill Is : ",fashionbill)
            print("\n\n#################################################")
            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

#MODULE TO CALCULATE TOTAL BILL AND INSERT DATA INTO TABLE TOTAL
def totalAmount():
    global cid
    customer=searchCustomer()
    if customer:
        global grandTotal
        global roomrent
        global restaurantbill
        global fashionbill
        global gamingbill
        if myConnection:
            cursor=myConnection.cursor()
            createTable ="""CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20) PRIMARY KEY,C_NAME VARCHAR(30),ROOMRENT INT ,RESTAURENTBILL INT ,GAMINGBILL INT,FASHIONBILL INT,TOTALAMOUNT INT)"""
            cursor.execute(createTable)
            sql= "INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s,%s,%s)"
            name = input("Enter Customer Name : ")
            grandTotal=roomrent + restaurantbill + fashionbill + gamingbill
            values= (cid,name,roomrent,restaurantbill , gamingbill,fashionbill,grandTotal)
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            cursor.close()
            print("\n **** Barsa Boutique Hotel, Topsia, Kolkata **** CUSTOMER BILLING ****")
            print("\n CUSTOMER NAME : " ,name)
            print("\nROOM RENT : Rs. ",roomrent)
            print("\nRESTAURENT BILL : Rs. ",restaurantbill)
            print("\nFASHION BILL : Rs. ",fashionbill)
            print("\nGAMING BILL : Rs. ",gamingbill)
            print("___________________________________________________")
            print("\nTOTAL AMOUNT : Rs. ",grandTotal)
            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")

#MODULE TO GENERATE OLD BILL
def searchOldBill():
    global cid
    customer=searchCustomer()
    if customer:
        if myConnection:
            cursor=myConnection.cursor()
            sql="SELECT * FROM TOTAL WHERE CID= %s"
            cursor.execute(sql,(cid,))
            data=cursor.fetchall()
            if data:
                print(data)
            else:
                print("Record Not Found Try Again !")
            cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

#MODULE TO SEARCH FOR CUSTOMER DETAILS IN TABLE C_DETAILS ACCORDING TO CUSTOMER ID
def searchCustomer():
    global cid
    if myConnection:
        cursor=myConnection.cursor()
        cid=input("ENTER CUSTOMER ID : ")
        sql="SELECT * FROM C_DETAILS WHERE CID= %s"
        cursor.execute(sql,(cid,))
        data=cursor.fetchall()
        if data:
            print(data)
            return True
        else:
            print("Record Not Found Try Again !")
            return False
        cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")



#__main__
print("""
#****************************** HOTEL MANAGEMENT SYSTEM ******************************#
############################## Barsa Boutique Hotel, Topsia, Kolkata ##############################
#*******Designed and Maintained By :
#*******SHOURJYA CHAKRABORTY - CLASS XII S4 - ROLL NO - 34 [ 2022-2023 ]
#*******PROTYASHA  SAHA - CLASS XII S4 - ROLL NO - 23 [ 2022-2023 ]
""")
myConnection = MYSQLconnectionCheck ()
if myConnection:
    MYSQLconnection()
    while(True):
        print("""
        1--->Enter Customer Details
        2--->Booking Record
        3--->Calculate Room Rent
        4--->Calculate Restaurant Bill
        5--->Calculate Gaming Bill
        6--->Calculate Fashion store Bill
        7--->Display Customer Details
        8--->GENERATE TOTAL BILL AMOUNT
        9--->GENERATE OLD BILL
        10--->EXIT """)
        choice = int(input("Enter Your Choice"))#ACCEPTING INPUT FROM USER AND PERFORMING ACTIONS AS PER USER'S REQUEST
        if choice == 1:
            userEntry()
        elif choice ==2:
            bookingRecord()
        elif choice ==3:
            roomRent()
        elif choice ==4:
            Restaurant()
        elif choice ==5:
            Gaming()
        elif choice ==6:
            Fashion()
        elif choice ==7:
            searchCustomer()
        elif choice ==8:
            totalAmount()
        elif choice ==9:
            searchOldBill()
        elif choice ==10:
            break
        else:
            print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
else:
    print("\nERROR ESTABLISHING MYSQL CONNECTION !")
# END OF PROJECT
