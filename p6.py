def squareoflist(lst):
    for i in range(len(lst)):
        lst[i]**=2
        print("Modified list =",lst)

a=[4,3,5,1,2]
print("Original list before passing to a function =",a)
squareoflist(a)
print("Original list after passing to a function =",a)