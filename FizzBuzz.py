i = 0
while i in range(100):
      print(i)
      if (i % 15) == 0:
            print("FizzBuzz")
      elif (i % 5) == 0:
            print("Buzz")
      elif (i % 3) == 0:
            print("Fizz")
      i += 1