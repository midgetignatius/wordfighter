**Word Fighter**

Challenge yourself and your friends to see how fast you can type!
In a digital age world, fast typing is emerging to become an essential skill! The race of AI development depends not just on how
one can think but also how fast one can type! 

HOW TO PLAY
1. Users start off choosing how many players they would like to include in the game 
2. Then 2 game modes of choice will be present. Characters / words. 
	- Characters will pull out random number of strings (note: this is the harder game mode) 
		--> Characters will include upper & lower alphabets and numbers 
	- Words will put out random number of words
		--> Words are random words that will be generated from a text file contain 1000 different words
3. Next, the user can choose how many words/characters that they would like to challenge themselves to type. 
	- Note: the more the number of characters/words, the more accurate their results will be 
4. Random characters/words will be generated.
5. User will be given 3 seconds to read the generated character/word 
6. User then will have to type as fast as possible and hit enter once done 
	- Note: if the input character/word is wrong the user will have to retype the entire line again
		- The timer will only stop when they have inputed the correct input
7. Based on the user's typing speed, different rankings will be given to the user

Typing speed 
<40 words per min / <130 characters per min = Typing Donkey 
>40 words per min / >130 characters per min = Average Man
>45 words per min / >145 characters per min = Fast n Unfurious Man  
>50 words per min / >155 characters per min = Typing Champion 
>60 words per min / >165 characters per min = Typing Hero 
>70 words per min / >170 characters per min = Typing legend 
>80 words per min / >175 characters per min = Type Racer 

8. If the user types in more than 1 player, the fastest typer will emerge as the winner


Code Explanation
Randomiser class : creates either a random string or a random word
	1. random_string function utilises the string module to generate random characters based on the user input
	   of number of characters
		- ascii letters and digits are stored in variable 'letter'
		- It loops through the input number, using the random.choice, it returns random letters or digits from the letter variable and appends to the word

	2. random_sentence function reads a text file with 1000 random words, it generates random number and takes the
	   word from the random number line and loops through based on the user input of number of words
		- Opens the file in read mode and based on the input number loops the number of times it will random word from that list
		- Strips the words so that it doesn't include spacings on the left and right 

Countdown function : creates a countdown timer for the user to read the given words/characters before starting
	- Based on the input number, this uses the time module to countdown
	- time.sleep(1) will wait one second before the loop is repeated
	- When the countdown is over, it will print 'Go!'

User_input_string function : This function when the user types in 'char' in play mode
	- Start time is recorded as the present time the moment the loop is called
	- User has to input the given words/char and the recorded start time will be recorded, the input is stripped too in case the user inputs an additional space
	- If the user input the right answer, it will print 'good job', and the end time will be recorded, the time-taken and the characters per minute will be calculated and displayed 
	- An if/else statement is also used to determine the rank of user's typing speed 
	- If the user inputs the wrong answer, then it will prompt the user to try again and the function will loop through itself

User_input_sentence : This function when the user types in 'words' in play mode
	- It is exactly the same as the string function just different game mode
	- It calculates the words per minute instead of chars per minute

Number_of_characters : This function is to prompt the user to input the number of characters that they want to play
	- It is to give the user some freedom in the gameplay
	- If the input is numeric, it will return the number 
	- If not, the function will loop itself until an integer is received

Number_of_sentences : This function is to prompt the user to input the number of words that they want to play
	- It the same as the number_of_characters function except for sentences input

Finally, theres is a main code that utilises the above functions to generate the game 
	- Prompts the user to input the number of players, play mode and then inputs into the above functions
	- Next, it prompts the user to input the play mode and then goes into an if else loop for the different inputs
	- It will call number_of_characters/sentence function to get the input number of characters/words
	- It then loops through the sequence of number of players
	- It will prompt to check whether the player is ready
	- It prints the random characters/words
	- Calls on countdown function for countdown of 3 seconds
	- Uses the user_input_string/sentence function to allow user to input what they have seen 
	- If the characters/words per minute is higher than the highest_score(which is initialised to 0 at first), then it will record the new highest score and that characters/word per minute and also store the current counter which is the current player
	- If the input players are more than 1, the winner will be displayed in the end
	- If during the play mode selection anything else other than 'word' or 'char' is input, it shows invalid input
