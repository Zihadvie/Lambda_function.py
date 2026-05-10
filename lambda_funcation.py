from concurrent.interpreters import list_all
add=lambda a,b:a+b                                     #addition use lambda
print(add(70,30))

Multiplication=lambda m:m*3                            #Multiplication use lambda
print(Multiplication(3))

a=int(input("enter first number : "))
b=int(input("enter second number : "))                   #user input take than maxi number print
mix=lambda a,b:a if a>b else b
print("Your max value is :",mix(a,b))

k=[5,100,90,10,30,50,20,40,60,80,70]
min=list(filter(lambda x:x<=50,k))                   #list to min number use lambda
min.sort()
print(min)

n=[10,30,50,20,40,60,80,70]
doub=list(map(lambda m: m*2,n))                     #lambda use multiply
doub.sort()
print (doub)




