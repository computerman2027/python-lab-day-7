#stack
try:
    stack=[]
    while True:
        print("MENU\n1. PUSH\n2. POP\n3. PEEK\n4. DISPLAY\n5. EXIT")
        ch=int(input("Enter your choice : "))
        if(ch==1):
            n=int(input("Enter number that need to be pushed : "))
            stack.append(n)
        elif(ch==2):
            if(len(stack)==0):
                print("UNDEFLOW")
            else:
                n=stack.pop()
                print("Popped element =",n)
        elif(ch==3):
            if(len(stack)==0):
                print("Stack is Empty")
            else:
                print("Peek =",stack[-1])
        elif(ch==4):
            if(len(stack)==0):
                print("Stack is Empty")
            else:
                print("Displaying stack from bottom to top : ",end="")
                for i in range(len(stack)):
                    print(stack[i], end=", " if i < len(stack) - 1 else "\n")
                print()
        elif(ch==5):
            print("END OF PROGRAM")
            break
        else:
            print("INVALID INPUT")
except ValueError:
    print("Error. Only Integer number accepted")