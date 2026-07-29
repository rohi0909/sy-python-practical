print( "==========Grocery shop========")
total=0
#iteam1
n=int(input("Enter your iteam:"))
name =str(input("Enter your iteam name:"))
price=float(input("Enter your price:"))
quantity=float(input("Enter you quantity kg:"))
amount1=price*quantity
total+=amount1
#iteam2
n=int(input("Enter your iteam:"))
name=str(input("Enter your iteam name"))
price=float(input("Enetr your price"))
quantity=float(input("Enter your quantity:"))
amount2=price*quantity
total+=amount2
amount=amount1+amount2
print("----------Bil--------")
print("total price:₹",amount)
print("total quantity:",quantity)
if amount>=300:
    discount=total*0.50
    print("discount:50% discount")
elif amount>=200:
    discount=total*0.30
    print("discount:30% discount")
elif amount>=100:
    discount=total*0.10
    print("discount:10% discount")
else:
    discount=amount*0.05
    ("print:discount:no discount")   
    
final_amount=total-discount


print("-----------------")
print("total amount:₹",final_amount)
print("-------thank you------!visit again-------🙏")