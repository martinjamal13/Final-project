# Amy docstrings
class PasswordGenerator:
    """ 
    Purpose
        Generates a strong password using user input and a mix of various types of characters.
    Attributes
        welcome_message (str): displays an introductory message including the name of the program.
    """
    welcome_message = "Welcome to PasswordMaker!"
    print(welcome_message)
    
    def user_input(self, username, answer1 = None, answer2 = None, answer3 = None, hint_access_question, hint_access_answer):
        """
        Purpose
            prompt user with questions to integrate memorable password segments, save username, and save hint question and answer
        Args
            username (str): user's login name
            answer1 (str): user's answer to the first question, defaults to None if the user doesn't choose this question
            answer2 (str): user's answer to the second question, defaults to None if the user doesn't choose this question
            answer3 (str): user's answer to the third question, defaults to None if the user doesn't choose this question
            hint_access_question (str): any question that user wants to display when they request a password hint
            hint_access_answer (str): value that user should input in order to gain password hint. Password hint is answer1, answer2, or answer3.
            password_hint (str): value is equivalent to answer1, answer2, or answer3, depending on which question is chosen for hint
        Returns
            username (str): indicates who the password is created for
        Raises
            ValueError if none of the questions are answered
        Side Effects
            if no questions are answered, return "select a question" statement
            stores values for answer1, answer2, answer3 in dictionary to use when generating password
            stores values for hintquestion and hintanswer in dictionary to use in "reset password" method
        """
        questions = {
            '1':'What\'s your favorite planet?',
            '2':'What is your favorite hobby?',
            '3':'What\'s at the top of your bucket list?'
            }
        self.username = input("What is your username?")
        print("These are the question you can choose from to create your password:")
        print("1. What's your favorite planet? \n2. What is your favorite hobby? \n3. What's at the top of your bucket list?")
        questionsChosen = input("Type the number of which questions you'd like. \nFor example, if you want questions 2 and 3, type \"23\"")
        # only question 1 is chosen
        if questionsChosen == 1:
            # only question 2 is chosen
            if questionsChosen == 2:
                # only question 3 is chosen
                if questionsChosen == 3:
                    # questions 1 & 2 are chosen
                    if questionsChosen == 12 or 21:  
                        # questions 1 & 3 are chosen
                        if questionsChosen == 13 or 31:
                            # questions 2 & 3 are chosen
                            if questionsChosen == 23 or 32:
                                # all questions are chosen
                                if questionsChosen == 123 or 132 or 213 or 231 or 321 or 312:
                                    return questions.get(questionsChosen)
        if # no questions are chosen, return:
            print("Select at least one question to answer.")
            
    def password_hint(self, hint_request, expected_hint_response):
        """
        Purpose
            Prompts user to ask for a hint when they forget their password. 
            Gives them password hint if input matches hint_access_answer.
        Args
            hint_resquest (str): user should input "hint" or "help" in order to access hint process
            expected_hint_response (str): value that user input should match in order to receive password hint
        Returns
            if input matches hint_response, return password hint (the value of answer1, answer2, or answer3)
            if input differs from expected_hint_response, return "try again, n attempts remaining" statement
        Raises
            ValueError if input differs from expected_hint_response
        Side Effects
            decrease attempts each time user inputs value different from expected_hint_response
        """

    def recent_password(self, start_date = 90):
        """
        Purpose
            This function will count down the days until a new password will need to be generated and give an update everyday    
        Args
            start_date (int): This will be a default value of 90 which represents 90 days.
        Returns
            an f string that tells the user how many days they have left until they will have to generate a new password.
            returns the new date so that it continously decreases by one each day. 
        Side effects
            User has no input here and consequently have no control over how often the password will expire.
        
        """
        
    def reset_password(self, username, answer1, answer2, answer3):
        """
        Purpose
            This function will allow the user to reset their password if the forgot it.
            
        Args
            username (str): user's login name
            answer1 (str): user's answer to the first question, defaults to None if the user doesn't choose this question
            answer2 (str): user's answer to the second question, defaults to None if the user doesn't choose this question
            answer3 (str): user's answer to the third question, defaults to None if the user doesn't choose this question
        
        Returns
            This will return a str with the newly generated password.
            
        Raises
            ValueError if one or more answers does equal the answer we have on file.
            
        Side Effects
            User doesnt not choose their password. They will have to go through the entire process of reanswering questions to reset
        """
    
     #Aroge Akhtar

def generate_password(self, length, minAlphabets, minDigits):
	"""
	Purpose
		This function will generate a random password of given length with a combination of alphabets and numbers

	Args
		length (int) - length of password
		minAlphabet (int) - minimum number of alphabets required in the password
		minDigits (int) - minimun number of digits required in the password

	Returns
		This will return a string of given length and minimum occurence of alphabets and digits.

	Raises
		ValueError 	if length is smaller than the sum of minAlphabets and minDigits 
					or if any of the argument is <= 0
	"""

	        if length <= 0 or minAlphabets <= 0 or minDigits <= 0 or (minAlphabets + minDigits) >= length:
			    raise ValueError("Invalid Arguments")
		letters = string.ascii_letters
		digits = [str(digit) for digit in range(0,10)]
		alphabetComponent = ''.join(random.choice(letters) for i in range(minAlphabets))
		numericComponent = ''.join(str(random.choice(digits)) for i in range(minDigits))
		password = list(alphabetComponent + numericComponent)
		random.shuffle(password)
		password = ''.join(password)
		remainingComponent = list(letters) + list(digits)
		password += ''.join(random.choice(remainingComponent) for i in range(length - (minAlphabets+minDigits)))
		return password


if __name__ == '__main__':
	passwordGenerator = PasswordGenerator()
	password = passwordGenerator.generate_password(8, 3, 3)
	print (password)
 
 def security_questions(self):
	"""
	Purpose
		This function will prompt user with choice of recovering the password using security questions.

	Returns
		The newly generated password

	Raises
		ValueError 	if reponse to prompt is out of acceptable string (Y/N)
					or if user answers incorrectly
	"""