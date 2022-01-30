from ast import Str
from glob import glob
from tkinter import *
import random
import time

def clearGame():
    
    global word
    global label_text
    global spelled_word
    global fresh_dashes
    global count

    count = 5
    randomWord = random.randrange(0,len(wordList),1) #Picking random words
    word = wordList[randomWord] #Picking the word from the word list  
    lenWord = len(word) #Count how long is the word

    spelled_word = ''
    
    fresh_dashes = encryptWord(word)
    
    title_text.set('Guess the ' + str(lenWord) + ' letter word')
    encypt_text.set(fresh_dashes)
    history_text.set('letter used')
    count_text.set(count)

def disable_input(box):
    box.delete(0,'end')
    box.config(state='disabled')
    box.unbind('<Return>')

def encryptWord(word):
    #Making the blank lines
    dashes = ''
    for x in word:
        if x == ' ':
            dashes += ' '
            continue
        dashes += '_'
    return dashes 
def singleInput(event):
    guessedLetter  = entry_box.get()
    if len(guessedLetter) > 1:
        title_text.set('Big')
        entry_box.delete(0,'end')
    else:
        checker(event)

def checker(event):
    global spelled_word
    global fresh_dashes 
    global count

    guessedLetter  = entry_box.get()

    letterHistory.append(guessedLetter)
    history_text.set(letterHistory)
    
    if word.lower().find(guessedLetter) == -1:
        count -= 1
        count_text.set(count)

    if entry_box.get() in word:
        #Find the index of the word with the letter inputed, It also find index of duliputed words
        index = [i for i, x in enumerate(word.lower()) if x == guessedLetter] 
        #Replaces the '_' with the corrected guessed letter,
        for i in index: 
            if i != -1:
                listSpace =list(fresh_dashes)
                listSpace[i]=word[i]
                spelled_word = ''.join(listSpace)
                fresh_dashes  = spelled_word

        encypt_text.set(spelled_word)
    else:
        encypt_text.set(fresh_dashes)

    if spelled_word == word:
        title_text.set('won')
        disable_input(entry_box)
    
    if count == 0:
        title_text.set('Game Over, The word was ' + word)
        disable_input(entry_box)
        

    entry_box.delete(0,'end')


if __name__ == "__main__":

    root = Tk()
    root.title("Hang Man")
    
    
    #global count
    count = 5
    letterHistory = []
    wordList = ['hello']  #Word List
    randomWord = random.randrange(0,len(wordList),1) #Picking random words
    word = wordList[randomWord] #Picking the word from the word list  
    lenWord = len(word) #Count how long is the word

    fresh_dashes = encryptWord(word)
    
    spelled_word = ''
    
    title_text = StringVar()
    title_text.set('Guess the ' + str(lenWord) + ' letter word')

    label_title = Label(root, textvariable=title_text, width= 50)
    label_title.grid(row=0,column=0)

    history_text = StringVar()
    history_text.set('letter used')
    label_history = Label(root, textvariable=history_text, width= 50)
    label_history.grid(row=4,column=0)

    encypt_text = StringVar()
    encypt_text.set(fresh_dashes)
    
    label_word = Label(root, textvariable=encypt_text, width= 10)
    label_word.grid(row=1,column=0)
    
    btn = Button(root,text="rest", command = clearGame)
    btn.grid(row=1,column= 1,rowspan=2)

    count_text = StringVar()
    count_text.set(count)

    label_count = Label(root, textvariable=count_text, width= 10)
    label_count.grid(row=3,column=0)

    entry_box = Entry(root, width = 20)
    entry_box.grid(row=2,column=0)
    entry_box.bind('<Return>', singleInput)


    root.mainloop()


       