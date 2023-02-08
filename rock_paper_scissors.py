import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """"
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
user_input = input("What do you chose: Rock, Paper, or scissors?\n")
lst = [rock, paper, scissors]
random_value = random.choice(lst)
if user_input.lower() == 'rock':
    print(f"You chose rock:{rock}")
    if random_value == rock:
        print(f"The computer chose:{random_value}\nNo one wins.")
    elif random_value == paper:
         print(f"The computer chose:{random_value}\n Computer wins")
         print(""" 
                  %%% %%%%%%%             |#|=##
                %%%% %%%%%%%%%%%          |#|####
                %%%%% %         %%%       |#|=#####
                %%%%% %   @    @   %%     | | ==####
                %%%%%%%% (_  ()  )  %%    | |    ===##
                %%%%%%%%%  \_    | %%     | |       =##
                %%%%%%%%% %  u^uuu %%     | |         ==#
                %%%%%%%%%%%%%%%%%%%%      | |           V
         """)
                           
    elif random_value == scissors:
         print(f"The computer chose:{random_value}\n You win")
         print(""" 
         ,.,
        (~ ~)
       q:0 0:p
        ((_))
         'u'
         """)
if  user_input.lower() == 'paper':
    print(f"You chose paper:{paper}")
    if random_value == rock:
        print(f"The computer chose:{random_value}\n You win")
        print("""
         ,.,
        (~ ~)
       q:0 0:p
        ((_))
         'u' """)
    elif random_value == paper:
         print(f"The computer chose:{random_value}\nNo one wins.")
    elif random_value == scissors:
         print(f"The computer chose:{random_value}\n Computer wins")
         print(""" 
                  %%% %%%%%%%             |#|=##
                %%%% %%%%%%%%%%%          |#|####
                %%%%% %         %%%       |#|=#####
                %%%%% %   @    @   %%     | | ==####
                %%%%%%%% (_  ()  )  %%    | |    ===##
                %%%%%%%%%  \_    | %%     | |       =##
                %%%%%%%%% %  u^uuu %%     | |         ==#
                %%%%%%%%%%%%%%%%%%%%      | |           V

         """)
if user_input.lower == 'scissors':
    print(f"You chose scissors{scissors}")
    if random_value == paper:
        print(f"The computer chose:{random_value}\n You win")
        print("""
         ,.,
        (~ ~)
       q:0 0:p
        ((_))
         'u' """)
    elif random_value == rock:
         print(f"The computer chose:{random_value}\nComputer wins")
         print("""                        
                  %%% %%%%%%%             |#|=##
                %%%% %%%%%%%%%%%          |#|####
                %%%%% %         %%%       |#|=#####
                %%%%% %   @    @   %%     | | ==####
                %%%%%%%% (_  ()  )  %%    | |    ===##
                %%%%%%%%%  \_    | %%     | |       =##
                %%%%%%%%% %  u^uuu %%     | |         ==#
                %%%%%%%%%%%%%%%%%%%%      | |           V
         """)
    elif random_value == scissors:
         print(f"The computer chose:{random_value}\nNo one wins.")
   



