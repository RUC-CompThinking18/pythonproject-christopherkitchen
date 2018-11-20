import time #this allows us to, quite literally, use time.
import sys #this allows us to use sys.stdout, which works with printing things to the terminal.

#import schedule #this allows the next question to be asked after a certain amount of time

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
        sys.stdout.flush() #this will write everything in the buffer to the terminal
        time.sleep(1)
    sys.stdout.write(" you died")

# run_timer(120) #this timer should run while the questions are prompted, and is
               #the main asset of the game
raw_input("Climate change is a real problem we are facing, and our everyday decisions could make a big difference. There isn't much time left. (Press ENTER to make a difference.)")
#this prompts the user with the issue, being climate change. then, they will see the questions.

class Question: #this class houses the instances of the questions, and prompts them
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_question(self):
        print self.question
        your_answer = raw_input("answer: ")

        if your_answer == self.answer:
            print "correct!"

        else:
            print "incorrect!"

        #run_timer(120) #once the first question is answered, a timer starts. this is symbolic of the lack of time.

question1 = Question("You're at the supermarket buying groceries. The cashier asks if you would like a plastic bag for your products. Do you say yes or no?", "no")
#run_timer(120)
question2 = Question("You're brushing your teeth. Do you leave the water on while brushing?", "no")
question3 = Question("Do you buy water bottles?", "no")
# these questions all have relevance to climate change

question1.ask_question() #this calls the questions into the terminal
question2.ask_question()
question3.ask_question()

#schedule.every(10).seconds.do(question1)
