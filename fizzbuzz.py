for i in range (1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#fizzbuzzsum
n = int(input())

fizzbuzz_sum = 0

for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        fizzbuzz_sum += i

print(fizzbuzz_sum)
