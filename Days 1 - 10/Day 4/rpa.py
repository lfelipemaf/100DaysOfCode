import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock,paper,scissors]
player = input("Chose a number: 0 rock 🪨 , 1 paper 📄  and 2 scissors ✂️: \n")
cpu = random.randint(0,2)

print(choices[int(player)])

print("CPU choose:\n")
print(choices[cpu])

if int(player) == 0 and cpu == 2:
  print("You won! 🏆 ")
elif int(player) == 1 and cpu == 0:
  print("You won! 🏆 ")
elif int(player) == 2 and cpu == 1:
  print("You won! 🏆 ")
elif int(player) == cpu:
  print("It’s a draw")
else:
  print("You lose!")