import random 
import string 
import time 
import sys

#Randomiser class creates either a random string or a random sentence
class Randomiser:
    #Generating random stirng of specific length
    def random_string(length):
        letter = string.ascii_letters + string.digits
        word = ''
        for i in range (length):
            word += random.choice(letter)
        return word 
    #Generating random sentence of specific # of words
    def random_sentence(length):
        file = open ('words.txt','r')
        sentence = ''
        line = file.readlines()
        for i in range(length): 
            x = random.randrange(1,500)
            word = line[x]
            new_word = word[:-1]
            sentence += new_word + ' '
        file.close()
        return sentence.strip() 
    
#Creating a countdown for the user to read the word before typing in their answer
def countdown(timing):
    while timing>0: 
        print ('Starting in ... ' + str(timing) )
        time.sleep(1) #wait for 1 second 
        timing -= 1 
        
    if timing == 0: 
        print ('Go!')


#<<CHAR PLAY>> User input of the answer 
def user_input_string():
    start = time.time()
    x = input()
    p = x.strip()
    if p == printedword: 
        print ("Good Job!")
        end = time.time()
        timetaken = round((end-start),2)
        print('Time Taken : ' + str(timetaken) + ' secs') 
        cpm = (chars/timetaken)*60
        print ('Characters per minute : ' + str(round(cpm,2)))
        if cpm < 130: 
            rank = 'Typing Donkey!'
        elif cpm >= 130 and cpm <145: 
            rank = 'Average Man!'
        elif cpm >= 145 and cpm <155:
            rank = 'Fast n Unfurious Man!'
        elif cpm >= 155 and cpm <165: 
            rank = "Typing Champion!"
        elif cpm >= 165 and cpm <170: 
            rank = 'Typing Hero!'
        elif cpm >= 170 and cpm <175:
            rank = 'Typing Legend!'
        elif cpm >= 175: 
            rank = 'Type Racer!'
    
        print ('You are  ... ' + '\033[0;32;40m{}'.format(rank) )
        print('\033[0m') # reset the colours
        
    else: 
        print ("Try Again!")
        a = user_input_string()
        return a 
    return cpm 
        
#<<SENTENCE PLAY>> User input of the answer 
def user_input_sentence():
    start = time.time()
    x = input()
    p = x.strip()
    if p == printed_sentence: 
        print ("Good Job!")
        end = time.time()
        timetaken = round((end-start),2)
        print('Time Taken : ' + str(timetaken) + ' secs') 
        wpm = (words/timetaken)*60
        print ('Words per minute : ' + str(round(wpm,2)))
        if wpm < 40: 
            rank = 'Typing Donkey!'
        elif wpm >= 40 and wpm <45: 
            rank = 'Average Man!'
        elif wpm >= 45 and wpm <50:
            rank = 'Fast n Unfurious Man!'
        elif wpm >= 50 and wpm <55: 
            rank = "Typing Champion!"
        elif wpm >= 55 and wpm <60: 
            rank = 'Typing Hero!'
        elif wpm >= 60 and wpm <65:
            rank = 'Typing Legend!'
        elif wpm >= 65: 
            rank = 'Type Racer!'
    
        print ('You are  ... ' + '\033[0;32;40m{}'.format(rank) )
        print('\033[0m') # reset the colours
        
    else: 
        print ("Try Again!")
        a = user_input_sentence()
        return a
    return wpm 

#User to input how many CHARACTERS they will want to type         
def number_of_characters():
    print('How many characters ? <<Please input integers only>>')
    z = input()
    if z.isnumeric() == True:
        return int (z)
    else:
        print ('Invalid Input. Please try again!')
        a = number_of_characters()
        return int(a)
    
#User to input how many WORDS they will want to type
def number_of_sentences():
    print ('How many words ? <<Please input intergers only>>')
    z = input()
    if z.isnumeric() == True:
        return int(z)
    else:
        print ('Invalid Input. Please try again!')
        a = number_of_sentences()
        return int(a)


#main code to run the functions for the game 
print('Number of players?') 
players = input()
print("Play Mode: word/char ?")
y = input()
highest_score = 0
counter = 1
if y.lower () == 'char':  #User input of number of characters 
    chars = number_of_characters()
    while counter <= int(players):
        print('Player {} ready? Type Anything'.format(counter))
        z = input()
        print("Player {}'s turn".format(counter))
        printedword = Randomiser.random_string(chars) #Generation of random no. of characters
        print ('Your character(s) is :  ' + '\033[0;35;40m{}'.format(printedword)) 
        print('\033[0m') #reset the colours
        countdown(3)
        char_pm = user_input_string()
        if char_pm > highest_score:
            highest_score = char_pm
            t_player = counter 

        counter += 1 
    if int(players) > 1: 
        print ("The winner is : PLAYER {}".format(t_player))
    elif int(players) == 0:
        print ('Error. Cannot have 0 Players!')

elif y.lower() == 'word':
    words = number_of_sentences()
    while counter <= int(players):
        print('Player {} ready? Type Anything'.format(counter))
        z = input()
        print("Player {}'s turn".format(counter))
        printed_sentence = Randomiser.random_sentence(words)
        print ('Your word(s) is :  ' + '\033[0;35;40m{}'.format(printed_sentence)) 
        print('\033[0m') #reset the colours
        countdown(3)
        words_pm = user_input_sentence()
        if words_pm > highest_score: 
            highest_score = words_pm
            t_player = counter

        counter += 1 
    if int(players) > 1: 
        print ("The winner is : PLAYER {}".format(t_player))
    elif int(players) == 0:
        print ('Error. Cannot have 0 Players!')

else: 
    print ('Invalid input!')
        

#\033 --> Escape code 
# 1 --> Style(Normal)
# 32--> text colour(Green, easier to read)
# 40m--> background colour (black, contrast against the green well) 
 

    