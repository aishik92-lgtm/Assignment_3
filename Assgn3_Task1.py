#factorial using recursion without while loop:::
def fact_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n-1)

num = int(input("Enter a number: "))
result = fact_rec(num)
print(f"The factorial of {num} is {result}")
