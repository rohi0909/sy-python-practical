marks=[]

while True:
    print("------student mark managemet system--------")
    print("1.insertion")
    print("2.display")
    print("3.upadate")
    print("4.delete")
    print("5.Exit")

    choice=int(input("Enter your choice:"))
    #insertion
    if choice==1:
        
        mark=int(input("Enter your marks:"))
        marks.append(mark)
        print("Marks inserted successfully.")


     #Traversal 
    elif choice==2:
        if len(marks) ==0:
            print("No marks available.")  
        else:
            print("student marks:")
            for i in range(len(marks)):
                print("student",i+1,":",marks[i])
    # updation 
    elif choice==3:
        student=int(input("Enter student number to update:"))
        if 1<= student<= len(marks):
            new_mark=int(input("Enter new marks:"))
            marks[student - 1] = new_mark   
            print("Marks updated successfully.")
        else:
            print("Invalid student number.")    
    #deletion
    elif choice==4:
        student=int(input("Enter student number to delete:"))  
        if 1<= student <=len(marks):
            marks.pop(student-1)
            print("marks deleted successfully.")
        else:
            print("Invalid student number")           
    #Exit
    elif choice==5:
        print("program ended.")
        break
    else:
        print("Invalid choice.")                   

     