def fsm_parser(input_string):
      alphabet = ['a', 'b']
      state = 'S0'
      for char in input_string:
            if char not in alphabet:
                  return False
            if state == 'S0':
                  if char == 'a':
                        state = 'S1' 