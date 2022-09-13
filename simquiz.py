
# #————————————————————————————
# from pickle import FALSE, TRUE


# def new_game():
#     guesses = []
#     corret_guess = 0
#     question_num = 0
#     for key in question:
#         print("————————————————————————————")
#         print(key)
#         for i in option[question_num]:
#             print(i)
#         question_num+=1
#         guess = input("Your answer is:")
#         guess = guess.upper()
#         guesses.append(guess)
#         corret_guess+=check_answer(question.get(key),guess)
#     display_scroe(corret_guess,guesses)
# #————————————————————————————
# def display_scroe(scroe,guesses):
#     print("————————————————————————————")
#     print("RESULT:")
#     print("————————————————————————————")
#     print("The right answer is:",end = "")
#     for i in question:
#         print(question.get(i),end = " ")
#     print()
#     print("Your anwser is:",end = "")
#     for i in guesses:
#         print(i,end = " ")
#     print()
#     final_scroe = int(scroe/len(question)*100)
#     print("Your score is "+str(final_scroe)+"%")
# #————————————————————————————
# def check_answer(anwser,guess):
#     if guess == anwser:
#         print("Correct!!")
#         return 1
#     else:
#         print("Wrong!!")
#         return 0
# #————————————————————————————
# def play_again():
#     response = input("Do you wanna play again?(yes or no):")
#     response = response.upper()
#     if response == "YES":
#         return 1
#     else:
#         return 0
# #————————————————————————————
# question = {
#     "who created Python?:":"A",
#     "what year was Python created?:":"B",
#     "Python is tributed to which comedy group?:":"C",
#     "Is the Earth round?:":"A"
# }

# option =[["Guide van Rossum","Elon Musk","Bill Gates","Mark Zuckerburg"],
#         ["1989","1991","2000","2010"],
#         ["Lonely Island","Smosh","Monty Python","SNL"],
#         ["True","False","sometimes","What's Earth?"]]

# new_game()

# while play_again():
#     new_game()
# print("Byeeeeeeee")