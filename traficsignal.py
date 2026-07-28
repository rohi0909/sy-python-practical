print("****Trafic Signal Rule****")

signal=input("Enter the signal colour:")

if signal =="red":
    print("action: stop")          
    
elif signal =="yellow":
    print("action: wait")
    
elif signal =="green":
    print("action: go")    
    
else:
    print("invalid signal colour")     