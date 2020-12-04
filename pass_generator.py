# Amy doc strings
import datetime
import sys
import argparse

class PasswordGenerator:
    """ 
    Attributes
        [name of object] ([insert type]): [insert what it does]
    """
    # Implement attribute that shows how is used_password() going to know if a particular password has been used before
    
    def __init__(self, username):
        self.username = username
    

    def user_input(self, username):
        """
        Purpose
            prompt user with questions to integrate memorable password segments, save username, and save hint question and answer
        Args
            username (str): user's login name
        Returns
            username (str): indicates who the password is created for
        Raises
            ValueError if none of the questions are answered
        Side Effects
            if no questions are answered, return "select a question" statement
            stores values for question responses in list to use when generating password
            stores values for hintquestion and hintanswer in dict to use in "reset password" method
        """
        #self.username = input("PasswordGenerator, the internet's most secure password generator.\nUsername: ")
        while True:
            print(f"\nHi {username}, what would you like to do? (1/2/3/4/5)")
            selection = input("1) Generate password\n2) Reset password\n3) Check if password has been used before\n4) Check if my password is common\n5) Exit program\n")
            if selection == "5":
                print("Enjoy your password!")
                break
            elif selection == "2" or "3" or "4":
                print("Coming soon.")
                break
            elif selection == "1":
                print("\nWhich questions would you like to use to help create your password?")
                print("1) What's your favorite planet?\n2) What is your favorite hobby?\n3) What's at the top of your bucket list?")

                key = input("\nType the corresponding number here: ").strip()

                options = ["What is your favorite planet?", "What is your favorite hobby?", "What's at the top of your bucket list?"]

                # dict of user's questions and responses 
                QnA = {}  
                
                if "1" in key:
                    response1 = input("What is your favorite planet? ")
                    QnA[options[0]] = response1
                elif "2" in key:
                    response2 = input("What is your favorite hobby? ")
                    QnA[options[1]] = response2 
                elif "3" in key:
                    response3 = input("What's at the top of your bucket list? ")
                    QnA[options[2]] = response3
                else:
                    print("Invalid input.")
                    break
                    
                # list of user's responses to questions
                responses = []
                
                for key in QnA.keys(): 
                    responses.append(QnA[key])
                    
                print("\nGreat! These responses will make it easier for you to remember your password.\n")
                hint_access_question = input("What would you like your password hint question to be? (Ex. What was the first song that I wrote?)\n")
                hint_access_answer = input("What do you want to be the answer that grants access to a password hint? (Ex. Green Grass)\n")
                
                # dict of user's hint question and its answer to use for resetting password
                hints = {}
                hints[hint_access_question] = hint_access_answer
                
                # list of user's responses to password generator questions
                password_hint = responses
                if input("Would you like to return to the home screen? Press \'n\' to exit program, input any other key to return. ") == "n":
                    break
            
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
# Jamal doc strings
    def recent_password(self):
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
            
        expire_day = datetime.date.today() + datetime.timedelta(90)
        days_left = expire_day - current_day
        while current_day != expire_day:
            current_day+=datetime.timedelta(1)
            days_left -=datetime.timedelta(1)
            if current_day == expire_day:
                print("you have to generate a new password today!")
            else:
                print(f"you have {abs(days_left)} until you will need a new password")
                break
        
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

    def reset_password(self):
        answer1 = input(" Enter your answer to your first question ")
        answer2 = input(" Enter your answer to your second question ")
        answer3 = input(" Enter your answer to you third question ")
        if answer1.lower == responses[0].lower & answer2.lower == responses[1].lower & answer3.lower == responses[2].lower:
            generate_password()
        else:
            raise ValueError ("One or more of your answers were incorrect please try again")
     
     
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


def parse_args(arglist):
    """ This function parses the command-line arguements"""
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help = "enter your username")
    args = parser.parse_args(arglist)
    return args

def main(username):
    trial = PasswordGenerator(username)
    return trial

if __name__ == '__main__':
	#passwordGenerator = PasswordGenerator()
	#password = passwordGenerator.generate_password(8, 3, 3)
    args = parse_args(sys.argv[1:])
    print(main(args.username))
	#print (password)
 
