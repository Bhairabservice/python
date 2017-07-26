def location():
    lalitpur=["Bungamati","Khokana","Bhainsepati","Nakhu","Ekantakuna","Jawalakhel","Pulchowk","Kupondole","Tripureshwor","Dharahara"]
    drivers=["Driver 1","Driver 2","Driver 3","Driver 4","Driver 5"]
    i=0
    for j in lalitpur:
        print(i+1,j)
        i+=1
    loc=input("Select the source location")
    for k in lalitpur:
        count=0
        drivercount=0
        if loc=='1':
            print("Source-->",lalitpur[count])
            for drive in drivers:
                print(drivercount+1,drive)
                drivercount+=1
            drv=input("Choose your driver")
            if drv=='1':
                print(drivers[count])
            
            break
        elif loc=='2':
            print("Source-->",lalitpur[count+1])
            break
        elif loc=='3':
            print("Source-->",lalitpur[count+2])
            break
        elif loc=='4':
            print("Source-->",lalitpur[count+3])
            break
        elif loc=='5':
            print("Source-->",lalitpur[count+4])
            break
        elif loc=='6':
            print("Source-->",lalitpur[count+5])
            break
        elif loc=='7':
            print("Source-->",lalitpur[count+6])
            break
        elif loc=='8':
            print("Source-->",lalitpur[count+7])
            break
        elif loc=='9':
            print("Source-->",lalitpur[count+8])
            break
        elif loc=='10':
            print("Source-->",lalitpur[count+9])
            break
        else:
            print("Please Choose Again")
            location()
        
    loc1=input("Select the Destination location")
    for k in lalitpur:
        count=0
        if loc1=='1':
            print("Destination",lalitpur[count])
            break
        elif loc1=='2':
            print("Destination",lalitpur[count+1])
            break
        elif loc1=='3':
            print("Destination",lalitpur[count+2])
            break
        elif loc1=='4':
            print("Destination",lalitpur[count+3])
            break
        elif loc1=='5':
            print("Destination",lalitpur[count+4])
            break
        elif loc1=='6':
            print("Destination",lalitpur[count+5])
            break
        elif loc1=='7':
            print("Destination",lalitpur[count+6])
            break
        elif loc1=='8':
            print("Destination",lalitpur[count+7])
            break
        elif loc1=='9':
            print("Destination",lalitpur[count+8])
            break
        elif loc1=='10':
            print("Destination",lalitpur[count+9])
            break
        else:
            print("Please Choose Again")
            location()
            
def guestinfo():
    firstname=input("Enter your Name ---> ")
    mobileno=input("Enter your mobile no--->")
    source=input("Enter the pick up location--->")
def rdetail():
        Dname=input("Enter the name of Driver")
        Dnum=input("Enter the mobile number")
        num=Dnum
        Dloc=input("Enter the location")
        Cname=input("Enter your guest name--->")
        print("--------------Driver's Detail----------------")
        print("Driver's Name:","\t",Dname)
        print("Driver's Cell no :","\t",Dnum)
        print("Driver's location:","\t",Dloc)
        print("Welcome","Mr",Cname,"to hellotaxi services","Visit our online site ---","www.hellotaxi.com","-----")
        return num

    
    
def newline():
    print("\n")
    print("\n")
    
class cabbook:
    guestcount=0
    def __init__(self,autono,driver,source="Bhainsepati",dest="Tribhuwan International Airport",time="20"):
        self.autono=autono
        self.driver=driver
        self.source=source
        self.dest=dest
        self.time=time
    
        
        
    def message(self):
        rdetail()
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        print("|","Your Ride from",self.source,"===>",self.dest,"has been booked")
        print("|","Pick Up Location     --->",self.source,"|")
        print("|","Destination Location --->",self.dest,"\t"," ","|")
        print("|","Estimated Ride Time  --->",self.time,"minutes")
        print("-------------------------------------------------------------------------------")
        print("!!!Pay fares using esewa and get 20% off on every rides (Hellotaxi)!!!")
      
#guest1=cabbook("Ba 2 cha-08-177","Bhairab Traders")

#guest1.message()
location()


