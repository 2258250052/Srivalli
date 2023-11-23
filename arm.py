Printing 1 to n armstrong numbers using list comprehension


Program:

def ArmstrongNumber(num):
    order = len(str(num))
    return num == sum(int(digit)**order for digit in str(num))
def ArmstrongNumbersUpTon(n):
    return [num for num in range(1, n+1) if ArmstrongNumber(num)]
n = int(input("Enter the value of n: "))
print(f"Armstrong numbers from 1 to {n}: {ArmstrongNumbersUpTon(n)}")

Output:

Enter the value of n: 400
Armstrong numbers from 1 to 400: [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371
