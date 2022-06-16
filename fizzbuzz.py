def fizzbuzz(i):
    return "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i)
  
      if i % 15 == 0:
         return "FizzBuzz"
      elif i % 3 == 0:
         return "Fizz"
      elif i % 5 == 0:
         return "Buzz"
      else:
        return str(i)
      
    outputs = [fizzbuzz(i) for i in range(1, 101)]
    print(outputs)
