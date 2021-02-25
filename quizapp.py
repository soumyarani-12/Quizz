from tkinter import *           # importing required modules tkinter for creating GUI
import random                   # importing random for randomizing questions for each participant
import json                     # importing json module for performing operations on json files


root = Tk()
root.geometry("800x500")        #creating main window 
root.title("Quiz")
with open('quiz.json') as f:                        # loading required objects from jason file
    obj = json.load(f)
z = random.randint(0,9)#random number generator in order to randomize questions answers and options with respect to this number 
q = (obj['ques'])
random.Random(z).shuffle(q)# randomizing questions with respect to already generated random number
options = (obj['options'])
random.Random(z).shuffle(options)
a = (obj['ans'])            
random.Random(z).shuffle(a) # randomizing Answers  with respect to already generated random number
rightanswerss= (obj['rightans']) # randomizing Answers in text form  with respect to already generated random number
random.Random(z).shuffle(rightanswerss)

one2ten=["1","2","3","4","5","6","7","8","9","10"] # this list is created to append with randomized questions

c=[]
i=0
while(i<len(one2ten)):              # this is the logic for append question number with randomized questions
    c.append(one2ten[i]+q[i])
    i+=1
q=c



class Quiz:
    def __init__(self):
        self.qn = 0                         #'qn'= question number
        self.ques = self.question(self.qn)  #  the qn label will return to this by calling question method or function
        self.opt_selected = IntVar()        # initially declaring the datatype default value is zero'0'
        self.opts = self.radiobtns()        # the b list will return to this by calling radiobtns function
        self.display_options(self.qn)       # calling display options function
        self.buttons()                      # calling buttons function
        self.correct = 0                    # initially correct answers value is zero '0'
        self.wrongAnsweredquestions = []    # created this list to store wrong answered questions
        
        self.rightAns=[]                    # created this list to store actual answers in words 
        
        
        
        

    def question(self, qn): # this is the method for displaying questions from the json file
        t = Label(root, text="Quiz in Python Programming", width=50, bg="blue", fg="white", font=("times", 20, "bold")) # created lable to show the title
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], width=60, font=("times", 16, "bold"), anchor="w") # created lable to show questions one by one further depends on buttons function
        qn.place(x=70, y=100)
        return qn                           # return qn to the calling function

    def radiobtns(self): # this is the method for placing the empty radio buttons one by one 
        val = 0
        b = []
        yp = 150
        while val < 4: # logic for placing four unchecked radio buttons vertically
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn): # this is the method for displaying options from the json file
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn] # logic for placing the options in right position
        for op in options[qn]:
              self.opts[val]['text'] = op
              val += 1

    def buttons(self):              # method for buttons
        nbutton = Button(root, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("times",16,"bold"))
        nbutton.place(x=200,y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy,width=10,bg="red",fg="white", font=("times",16,"bold"))
        quitbutton.place(x=380,y=380)

    def checkans(self, qn):         # method to check the selected options are right or wrong
        if self.opt_selected.get() == a[qn]:
             return True
        else:
            
                self.wrongAnsweredquestions.append(q[qn]) # this is where the wrong answered questions are get stored

                
                self.rightAns.append(rightanswerss[qn]) # this is where the right answers are stored if the selected options are wronganswer               
                
                
        
    def nextbtn(self):  # method for next button to display question one by one
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.display_options(self.qn)       
        

    def display_result(self): # this method will display results by opening new window
        
        if(len(self.wrongAnsweredquestions)==0):
            self.opennewwindow2()
        else:
            self.opennewwindow()

    def opennewwindow(self): # this window is open if atleast one wrong answered questions are there
        new_window=Toplevel(root)
        new_window.geometry("1200x1200")
        score = int(self.correct / len(q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        
        lb1 = Label(new_window, text="The right answers are",width=50, bg="blue", fg="white", font=("times", 20, "bold"))
        lb1.pack()
        
        pn = Label(new_window, text="\n".join(self.wrongAnsweredquestions), width=60, font=("times", 16, "bold"), justify=LEFT)
        pn.place(x=70, y=100)
       

        pn1 = Label(new_window, text="\n".join(self.rightAns), width=60, fg="Green",font=("times", 16, "bold"), justify=LEFT)
        pn1.place(x=800, y=100)
        
        
        
        pn2 = Label(new_window, text="Result is", width=60,fg="Red", font=("times", 16, "bold"), justify=LEFT)
        pn2.place(x=250, y=570)
        
       
        
        
        pn3 = Label(new_window, text="\n".join([result, correct, wrong ]), width=60, font=("times", 16, "bold"), justify=LEFT)
        pn3.place(x=250, y=600)
        
       
        
        
    def opennewwindow2(self):# this window is open when all answers are correct
        new_window2=Toplevel(root)
        new_window2.geometry("500x500")
        score = int(self.correct / len(q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        
        lb2 = Label(new_window2, text="Congrats! All Answers are right",width=50, bg="Green", fg="White", font=("times", 20, "bold"))
        lb2.pack()
        
        pn4 = Label(new_window2, text="Result is", width=60, fg="Red", font=("times", 16, "bold"), justify=LEFT)
        pn4.place(x=10, y=120)
        pn4.pack()       
        pn5 = Label(new_window2, text="\n".join([result, correct, wrong ]), width=60, font=("times", 16, "bold"), justify=LEFT)
        pn5.place(x=10, y=150)
        pn5.pack()
 
quiz=Quiz()
root.mainloop()










