# Amy's section of code
class PasswordGenerator:
    """ 
    Purpose
        Generates a strong password using user input
    """
    print("Welcome to PasswordMaker!")
    
    def user_input(self, username, answer1, answer2, hintquestion, hintanswer):
        """
        Purpose
            prompt user with questions to create keywords in password
            prompt user for their username
            prompt user for hint question and answer
        Parameters
        Attributes
        Returns
        Side Effects
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
    
    def password_hint():
        """
        Purpose
            Prompts user to ask for a hint when they forget their password and gives them a hint
        Parameters
        Attributes
        Returns
            A userful segment of string from a security question
        Side Effects
        """ 
