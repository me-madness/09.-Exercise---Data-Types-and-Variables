# num = int(input("Enter the number: "))
num = int(input())
is_prime =True

if num > 1:
    for divisor in range(2, num):
        if (num % divisor) == 0:
            is_prime = False
            break
    if is_prime:
        print("True")
    else:
        print("False")              
else:
    print("False")   
    
    
# def is_prime(num):
#     for i in range(2,num):
#         if (num % i) == 0:
#             print("False") 
#     print("True")

# is_prime(num)     
