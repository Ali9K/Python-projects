import random

num_of_players = int(input("How many players would you like to play the game with? "))

records = {}
plist = []
a = 1
while num_of_players > 0:
      name = input("Player %i, what's your name? " %a)
      plist.append(name)
      a += 1
      num_of_players -= 1

for player in plist:
      num = random.randint(1000, 10000)
      guess = int(input("\n %s, please guess the 4 digit number: "%player))
      if guess == num:
            print("\tWOW %s! You are MASTERMIND. You win the Game." %player)
            exit()
      else:
            guess_counter = 1
            while guess != num:
                  print(num)
                  print(guess)      
                  correct = "****"
                  digit_counter = 0
                  string_num = str(num)
                  string_guess = str(guess)
                  for i in range(0, 4):
                        if string_num[i] == string_guess[i]:
                              digit_counter += 1
                              correct = correct[0:i] + string_num[i] + correct[i+1:]
                  print("\n\tNot quite the number. But you did get %i digit(s) correct!" %digit_counter)
                  print("\tThe number is %s." %correct)
                  guess = int(input("\nPlayer1, please guess the 4 digit number again: "))
                  guess_counter += 1
            print("\n\tThat's correct. It took you only %i tries." %guess_counter)
            records[player] = guess_counter
mastermind = plist[0]
mastermind_record = records[mastermind]
plist_counter = 0
for i in plist:
      if records[i] < mastermind_record:
            mastermind_record = records[i]
            mastermind = plist[plist_counter]
      plist_counter += 1
print("You win the game %s. Your record is: %i" %(mastermind, mastermind_record))