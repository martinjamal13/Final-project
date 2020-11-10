# Amy's section of code
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
