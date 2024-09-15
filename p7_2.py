# queue
try:
    queue=[]
    while True:
        print("MENU\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
        ch=int(input("Enter your choice : "))
        if ch==1:
            n=int(input("Enter number that need to be pushed : "))
            queue.append(n)
        elif ch==2:
            if(len(queue)==0):
                print("UNDEFLOW")
            else:
                n=queue.pop(0)
                print("Dequeued element =",n)
        elif ch==3:
            if(len(queue)==0):
                print("Queue is Empty")
            else:
                print("Displaying queue from front to rear : ",end="")
                for i in range(len(queue)):
                    print(queue[i], end=", " if i < len(queue) - 1 else "\n")
                print()
        elif ch==4:
            print("END OF PROGRAM")
            break
        else:
            print("INVALID INPUT")
except ValueError:
    print("Error. Only Integer number accepted")