def fsm_parser(input_string):
      alphabet = ['a', 'b']
      state = 'S0'
      for char in input_string:
            if char not in alphabet:
                  print("Syntax Error! Invalid character found.")
                  return False
            if state == 'S0':
                  if char == 'a':
                        state = 'S1' 
            elif state == 'S1':
                  if char == 'b':
                        state = 'S2'
            elif state == 'S2':
                  if char == 'b':
                        state = 'S3'
                  elif char == 'a':
                        state = 'S1'
            elif state == 'S3':
                  if char == 'a':
                        state = 'S1'
                  elif char == 'b':
                        state = 'S0'
      if state == 'S3':
            return True
      else:
            print("Syntax Error! Input does not end with 'abb'.")
            return False
      

test_string = input("Enter a string(alphabet: 'a' and 'b'): ")
if fsm_parser(test_string):
    print(f'The string "{test_string}" is accepted.')
else:
    print(f'The string "{test_string}" is rejected.')
