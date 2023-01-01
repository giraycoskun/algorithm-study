#Euler Project
#Problem 1 // 04.07.2019

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
n = 1000

print("Sum of all the multiples of 3 or 5 below n")
n = input("Please enter n: ")


if n.isdigit() and int(n)>0:
    print("\nn is valid a number\nCalculations:\n")
    n = int(n)

    n = n-1

    num_3 = n//3
    print("num_3 is ", num_3)
    num_5 = n//5
    print("num_5 is ", num_5)
    num_15 = n//15
    print("num_15 is ", num_15)

    sum_multiples_3 = (((num_3+1)*num_3)/2)*3
    sum_multiples_5 = (((num_5+1)*num_5)/2)*5
    sum_multiples_15 = (((num_15+1)*num_15)/2)*15

    sum_3or5_multiples = sum_multiples_3 + sum_multiples_5 - sum_multiples_15

    print("Sum of all the multiples of 3 or 5 below %d" %(sum_3or5_multiples))


else:
    print("Invalid input\bBye Bye")

input()

#Giray Coskun
