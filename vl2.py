#print("Hi There! Welcome To This Virtual Learner")
import pyttsx3
engine = pyttsx3.init()
""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hi there Welcome to this virtual learner, please note that speech recognition is only available for test")
engine.say("what is your name")
engine.runAndWait()
name =input("please enter your name ")
engine.say("welcome"+ str(name))
engine.say("what would you like to do")
a = "register questions"
b = "take test"
c = 'update a set'
engine.say(str(a)+"or"+str(b)+"or"+str(c))
engine.runAndWait()
job = input()
global q
global an
#q = input('please register question')
#an = input('register answer')
class Queset:
    quesCount = 0
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer
        Queset.quesCount += 1
        #one = question(q,a,)
    def __str__(self):
        return '{}'.format(
            #self.__class__.__name__,
            self.question)
            #self.answer)
    def displayCount(self):
        print("Total Questions Registered %d" % Queset.quesCount)

    def displayQuestion(self):
        print ("question: ", self.question, ", answer: ",self.answer)
question_list =[]

if job == a:
    for _ in range(2):
        ques = input('register question')
        ans = input('register answer')
        y = Queset(ques, ans)
        question_list.append(y)
        y.displayQuestion()
        print("Total Questions Registered %d" % Queset.quesCount)   
#print([str(x) for x in question_list])
engine.say('what else would you like to do')
engine.runAndWait()
job = input()
if job == b:
    #engine.say([str(x)for x in question_list])
    #engine.runAndWait()
    for m in question_list:
        print([str(x.question)for x in question_list])
        
    #engine.
'''  anss = input()
    if ans == an:
        engine.say("you are correct")
        engine.runAndWait()
    else:
        engine.say("That is incorrect")
        engine.runAndWait

    print(one.answer)'''

#else:
    #engine.say("I'm sorry. Other options are not available at the moment")
    #engine.runAndWait()
