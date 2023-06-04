import mysql.connector as sqlct

import random
def createdb():
    global mycn
    global mycur
    
    mycn=sqlct.connect(host="localhost",user="root",password="asritha@@2002",database="sriram")
    if mycn.is_connected():
        print("\t\t\t\t WELCOME TO TRAINBOOKING .")
    mycur=mycn.cursor()
    query1 = "create table if not exists Train(sno int(100)  primary key,Name varchar(100),from1 varchar(100),TO1 varchar(100),TRAIN_NO varchar(200),TRAIN_NAME varchar(200),train_time varchar(100), SEATS_AVALIABLE varchar(200),cost int(100))"
    mycur.execute(query1)
createdb()
def display_ACSeats():
    
    print("====================================================================================================================")
    print("| DESTINATION PLACE  ARRIVAL PLACE  TRAIN NO   TRAIN NAME           TRAIN TIMINGS       TICKET PRICE  SEATS AVALIABLE|")
    print("====================================================================================================================")

    print("       CHENNAI       VIJAYAWADA      13352    PuneExpress              12:55am-5:15am          400rs           200       ")
    print("       HYDERABAD     GUNTUR          17254    KrishnaExpress           5:15am-9:30pm           500rs           250       ")
    print("       TIRUPATI      CHENNAICENTRAL  16054    ChennaiCentralExpress    10:10am-1:40pm          600rs           150       ")
    print("       NELLORE       BANGALORE       12296    PinakiniExpress          7:20am-3:54pm           700rs           400       ")
    print("       MUMBAI        VISAKHAPATNAM   20895    BhubaneswarExpress       8:40am-10:55am          800rs           350       ")
    print("==================================================================================================================")

def AC_passangers():
    
    query2 = "select * from Train"
    mycur.execute(query2)
    a2 = mycur.fetchall()
    
    print("====================================================================================================================")
    print("|SNO NAME DESTINATION PLACE  ARRIVAL PLACE  TRAIN NO   TRAIN NAME      TRAIN TIMINGS   SEATS  cost|")
    print("====================================================================================================================")

    for i in range(len(a2)): # i = 1
        print("| ",end="")
        print(str(a2[i][0]).ljust(15," "),end="") #r2[i] = r2[1][0]
        print(a2[i][1].ljust(17," "),end="|") #r2[1][1] 
        print(a2[i][2].ljust(18," "),end="|")                  
        print(a2[i][3].ljust(14," "),end="|")               
        print(str(a2[i][4]).ljust(15," "),end="|")
        print(a2[i][5].ljust(16," "),end=" ")
        print(a2[i][6].ljust(10," "),end=" |")
        print(str(a2[i][7]).ljust(5," "),end="|")
        print(str(a2[i][8]).ljust(5," "),end="|") #200 |
        print()

    print("==================================================================================================================")

cost1,cost2,cost3,cost4,cost5=400,500,600,700,800

def Book_ACSeats():
    global Seats
    global cost
    global name
    sno = int(input("Enter the id: "))
    name = input("Enter the name of the passenger: ")
    DestinationPlace=input("Enter the Destination Place: ")               
    ArrivalPlace=input("Enter the Arrival Place: ")                       
    TrainNumber=int(input("Enter the Train Number: "))
    print("PuneExpress,KrishnaExpress,ChennaiCentralExpress,BhubaneswarExpress,PinakiniExpress")
    TrainName=input("Enter the Train Name: ")
    if TrainName == "PuneExpress":
        cost = cost1
        print(cost," Rs per ticket")
        
    elif TrainName == "KrishnaExpress":
        cost = cost2
        print(cost," Rs per ticket")
        
    elif TrainName == "ChennaiCentralExpress":
        print(cost3," Rs per ticket")
        cost = cost3
    elif TrainName == "BhubaneswarExpress":
        print(cost5," Rs per ticket")
        cost =cost5
    elif TrainName == "PinakiniExpress":
        print(cost4," Rs per ticket")
        cost =cost4
    else:
        print("please select the train in given list.")
    Timings=str(input("Enter the Train Timings: "))   #7:30                  
    #Price=int(input("Enter the Ticket Price: "))
    Seats=int(input("Enter the no.of Seats: "))
    query3= "insert into Train values ('"+str(sno)+"','"+name+"','"+DestinationPlace+"','"+ArrivalPlace+"','"+str(TrainNumber)+"','"+TrainName+"','"+str(Timings)+"','"+str(Seats)+"','"+str(cost)+"')"
    mycur.execute(query3)
    print("Record has been added successfully")

def AC_Bill():
  query4 = "select * from Train"
  mycur.execute(query4)
  a3 = mycur.fetchall() 
  print("Your bill")
  name_1 = input("Enter the name of the passenger: ") #iswarya
  for i in range(len(a3)): #i =2
      a = a3[i][1] #r3[2][1]
      if name_1 == a: #i=2
          seat = int(a3[i][7])# i =2 r3[2][7]
          price = int(a3[i][8]) #r3[2][8]
          print("Total number of seats you booked: ",a3[i][7])
          print("your seat numbers are: ")
          
          for i in range(seat): #5 i=0 -250,i=1,i=2,i= 
              print(random.randrange(1,1000),end = ",")
          print(" ")
          total_amount = price * seat
          print("Total Amount = ",total_amount)

def display_GENERALSeats():
    
    print("====================================================================================================================")
    print("| DESTINATION PLACE  ARRIVAL PLACE  TRAIN NO   TRAIN NAME           TRAIN TIMINGS       TICKET PRICE  SEATS AVALIABLE|")
    print("====================================================================================================================")
    print("       CHENNAI       VIJAYAWADA      13352    PuneExpress              12:55am-5:15am          200rs           240       ")
    print("       HYDERABAD     GUNTUR          17254    KrishnaExpress           5:15am-9:30pm           250rs           550       ")
    print("       TIRUPATI      CHENNAICENTRAL  16054    ChennaiCentralExpress    10:10am-1:40pm          300rs           180       ")
    print("       NELLORE       BANGALORE       12296    PinakiniExpress          7:20am-3:54pm           350rs           480       ")
    print("       MUMBAI        VISAKHAPATNAM   20895    BhubaneswarExpress       8:40am-10:55am          400rs           390       ")
    print("==================================================================================================================")

def gen_passengers():
    
    query5 = "select * from Train"
    mycur.execute(query5)
    a4= mycur.fetchall()
    
    print("====================================================================================================================")
    print("|SNO NAME DESTINATION PLACE  ARRIVAL PLACE  TRAIN NO   TRAIN NAME      TRAIN TIMINGS   SEATS  cost|")
    print("====================================================================================================================")

    for i in range(len(a4)):
        print("| ",end="")
        print(str(a4[i][0]).ljust(19," "),end="") 
        print(a4[i][1].ljust(19," "),end=" ") 
        print(a4[i][2].ljust(20," "),end=" ")                  
        print(a4[i][3].ljust(16," "),end=" ")               
        print(str(a4[i][4]).ljust(15," "),end=" ")
        print(a4[i][5].ljust(10," "),end=" ")
        print(a4[i][6].ljust(16," "),end=" ")
        print(str(a4[i][7]).ljust(9," "),end=" ")
        print(str(a4[i][8]).ljust(6," "),end=" ") 
        print()

    print("==================================================================================================================")
cost6,cost7,cost8,cost9,cost10=200,250,300,350,400
def Book_genSeats():
    global Seats
    global cost
    global name
    sno = int(input("Enter the id: "))
    name = input("Enter the name of the passenger: ")
    DestinationPlace=input("Enter the Destination Place: ")               
    ArrivalPlace=input("Enter the Arrival Place: ")                       
    TrainNumber=int(input("Enter the Train Number: "))
    print("PuneExpress,KrishnaExpress,ChennaiCentralExpress,BhubaneswarExpress,PinakiniExpress")
    TrainName=input("Enter the Train Name: ")
    if TrainName == "PuneExpress":
        cost = cost6
        print(cost," Rs per ticket")
        
    elif TrainName == "KrishnaExpress":
        cost = cost7
        print(cost," Rs per ticket")
        
    elif TrainName == "ChennaiCentralExpress":
        print(cost8," Rs per ticket")
        cost = cost8
    elif TrainName == "PinakiniExpress":
        print(cost9," Rs per ticket")
        cost= cost9
    elif TrainName == "BhubaneswarExpress":
        print(cost10," Rs per ticket")
        cost= cost10
    else:
        print("please select the train in given list.")
    Timings=str(input("Enter the Train Timings: "))                 
    Seats=int(input("Enter the no.of Seats: "))
    query5 = "insert into Train values ('"+str(sno)+"','"+name+"','"+DestinationPlace+"','"+ArrivalPlace+"','"+str(TrainNumber)+"','"+TrainName+"','"+str(Timings)+"','"+str(Seats)+"','"+str(cost)+"')"
    mycur.execute(query5)
    print("Record has been added successfully")

def GEN_Bill():
     query6 = "select * from Train"
     mycur.execute(query6)
     a5 = mycur.fetchall() 
     print("Your bill")
     name_1 = input("Enter the name of the passenger: ")
     for i in range(len(a5)): 
        a = a5[i][1] 
        if name_1 == a: 
          seat = int(a5[i][7])
          price = int(a5[i][8]) 
          print("Total number of seats you booked: ",a5[i][7])
          print("your seat numbers are: ")
          for i in range(seat): 
              print(random.randrange(1,2000),end = ",")
          print(" ")
          total_amount = price * seat
          print("Total Amount = ",total_amount)




while True:
    print("\n\n-------------DETAILS--------------------")
    print("(1)ACSeats (2)GENERALSeats  (3)Exit")
    choice=int(input("Please enter your choice:")) # 1
    if(choice==1):
        while True:
            print("(1)display_ACSeats (2)Book_ACSeats (3)passenger_details (4)AC_Bill  (5)Exit")
            choice1=int(input("Please enter your choice:")) #2
            if(choice1==1):
                display_ACSeats()

            elif(choice1==2):
                Book_ACSeats()
            elif(choice1==4):
                AC_Bill()
            elif(choice1==3):
                AC_passangers()
            elif(choice1==5):
                break
    elif(choice==2):
        while True:
            print("(1)display_GENSeats (2)Book_GENSeats (3)passenger_details (4)GEN_Bill  (5)Exit")
            choice2=int(input("Please enter your choice:"))
            if(choice2==1):
                display_GENERALSeats()
            elif(choice2==2):
                Book_genSeats()
            elif(choice2==4):
                GEN_Bill()
            elif(choice2==3):
                gen_passengers()
            elif(choice2==5):
                break
            


    else:
        mycn.commit()
        break
