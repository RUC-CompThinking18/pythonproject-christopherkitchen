import time
import sys

def run_timer(seconds):
    for remaining in range(seconds, 0, -1):
        sys.stdout.write("\r")
        minutes = 0
        seconds = remaining
        if remaining > 60:
            minutes = int(seconds/60)
            seconds = int(seconds%60)
        else:
            seconds = remaining
        sys.stdout.write("{:2d} minutes {:2d} seconds remaining.".format(minutes,seconds))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write(" you died")

run_timer(120) #this timer should run while the questions are prompted, and is
               #the main asset of the game

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_question(self):
        print self.question
        your_answer = raw_input("answer: ")

        if your_answer = self.answer:
            print "correct!"

        else:
            print "incorrect!"

question1 = Question("You're at the supermarket buying groceries. The cashier asks if you would like a plastic bag for your products. Do you say yes or no?", "no")
question2 = Question("You're brushing your teeth. Do you leave the water on while brishing?", "no")
question3 = Question("Do you buy water bottles?", "no")
# these questions all have relevance to climate change
question1.ask_question() #this calls the questions into the terminal

#def Game_Questions(): #would i define each question, or define a class of questions?
#    print "You're at the supermarket buying groceries. The cashier asks if you would like a plastic bag for your products. Do you say yes or no?"

#    your_answer = raw_input("answer: ")

#    if your_answer == "yes":
#		print "You're helping better the enviorment, you've added 30 seconds!"

#	elif your_answer == "no":
#		print "You're speeding up the end of mankind, you've subtracted 30 seconds."

#    else:
#        print "Please type 'yes' or 'no'."

#i want to add a function that adds/minuses time from the timer based on correct
#or incorrect answers
