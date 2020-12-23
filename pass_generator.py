import datetime
import sys
import argparse
import hashlib
import random
import string

class PasswordGenerator:
    """ 
    Attributes
        [name of object] ([insert type]): [insert what it does]
    """
    # Implement attribute that shows how is used_password() going to know if a particular password has been used before
    
    def __init__(self, username):
        self.username = username
        self.start_day = datetime.datetime.now() 
        self.hints = {}
    
    def generate_password(self, length = 8, minAlphabets = 5, minDigits = 5):
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

    def user_input(self, username):
        """
        Purpose
            prompt user with questions to integrate memorable password segments, 
            save username, and save hint question and answer
        Args
            username (str): user's login name
        Returns
            username (str): indicates who the password is created for
        Raises
            ValueError if none of the questions are answered
        Side Effects
            if no questions are answered, return "select a question" statement
            stores values for question responses in list to use when generating 
            password
            stores values for hintquestion and hintanswer in dict to use in 
            "reset password" method
        """
        print("PasswordGenerator, the internet's most secure password generator.")

        self.username = input("Username: ")
        while True:
            print(f"\nHi {username}, what would you like to do?")
            selection = input("(1/2/3/4/5)")
            print("1) Generate password")
            print("2) Reset password")
            print("3) Check if password has been used before")
            print("4) Check if my password is common")
            print("5) How days until you need to change your password")
            print("6) Exit program")
            
            if selection == "6":
                print("Enjoy your password!")
                break
            elif selection == "1":
                #redirect to method 'input1to5'

    # if user selects options 1 through 5
    def input1to5():
        print(PasswordGenerator.generate_password(self, 8,3,3)) #says name is undefined 
        print("Which questions would you like to use to help create your password?")
        print("1) What's your favorite planet?
        print("2) What is your favorite hobby?"
        print("3) What's at the top of your bucket list?")
                
        key = input("\nType the corresponding number here: ").strip()

        options = [ 
                    "What is your favorite planet?", 
                    "What is your favorite hobby?", 
                    "What's at the top of your bucket list?"
                ]

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
            return responses
                    
        print("\nGreat!")
        print("These responses will make it easier for you to remember your password.")
        print("What would you like your password hint question to be?")
        hintAccessQ = input("Ex. What was the first song that I wrote?\n")
        print("What do you want to be the answer that grants access to a password hint?")
        hintAccessAns = input("Ex. Summer Song\n")
                
        # dict of user's hint question and its answer to use for resetting password
        hints = {}
        hints[hintAccessQ] = hintAccessAns
                
        # list of user's responses to password generator questions
        password_hint = responses
        print("Would you like to return to the home screen?")
        if input("Press \'n\' to exit program, input any other key to return. ") == "n":
            break
                
        #return responses
             
        elif selection == "2":
            PasswordGenerator.reset_password(self)
            #print(f"your new password is: {PasswordGenerator.generate_password(self, 8,3,3)}")
                 
        elif selection == "3": 
            PasswordGenerator.used_password(self)
            break
        elif selection == "4":
            print("Coming soon.")
            break
        elif selection == "5":
            PasswordGenerator.recent_password(self)
=======
        self.username = username
        while True:
            print(f"Hi {username}, what would you like to do?")
            print("1) Generate password")
            print("2) Password hint")
            print("3) Reset password")
            print("4) Check if password has been used before")
            print("5) Check if my password is common")
            print("6) Check how days until I need to change my password")
            print("7) Exit program")
            selection = input("(1/2/3/4/5/6/7) ")
            
            if selection == "7":
                print("Enjoy your password!")
                break
            elif selection == "1":
                self.selection1()
            elif selection == "2":
                self.password_hint()
            elif selection == "3":
                self.reset_password()
            elif selection == "4": 
                self.used_password()
            elif selection == "5":
                self.common_password()
            elif selection == "6":
                self.recent_password()
            else:
                print("Invalid input.")

    # if user selects option 1
    def selection1(self):
        print(self.generate_password(8,3,3)) 
        print("Which questions would you like to use to help create your password?")
        print("1) What's your favorite planet?")
        print("2) What is your favorite hobby?")
        print("3) What's at the top of your bucket list?")   

        key = input("Type the corresponding number here: ").strip()

        options = [ 
                    "What is your favorite planet?", 
                    "What is your favorite hobby?", 
                    "What's at the top of your bucket list?"
                ]
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
            quit()
>>>>>>> 50b4c3424dae0dbfc6f60109778d928f333d88c5

        print("Great!")
        print("These responses will make it easier for you to remember your password.")
        print("What would you like your password hint question to be?")
        hintAccessQ = input("Ex. What was the first song that I wrote?\n")
        print("What do you want to be the answer that grants access to a password hint?")
        hintAccessAns = input("Ex. Summer Song\n")
        # list of user's responses to questions
        
        responses = []
        for key in QnA.keys(): 
            responses.append(QnA[key])
            self.responses = responses
            #return responses
        # dict of user's hint question and its answer to use for resetting password
        #hints = {}
        
        self.hints[hintAccessQ] = hintAccessAns
                
        print("Would you like to return to the home screen?")
        if input("Press \'n\' to exit program, input any other key to return. ") == "n":
            quit()
        return self.responses
                
    def password_hint(self):
        """
        Purpose
            Prompts user to ask for a hint when they forget their password. 
            Gives them password hint if input matches hintAccessAns.
        Returns
            if input matches hintAccessAns, return password hint (the value of answer1, answer2, or answer3)
            if input differs from hintAccessAns, return "try again, n attempts remaining" statement
        Raises
            ValueError if input differs from hintAccessAns
        Side Effects
<<<<<<< HEAD
            decrease attempts each time user inputs value different from expected_hint_response
        # partial code
        user_forgot("Forgot password?\nType "hint" to access your password hint question.\nType "reset" to reset your password.")
        if "1" in user_forgot:
            hint_request = input(")
=======
            decrease attempts each time user inputs value different from hintAccessAns
>>>>>>> 50b4c3424dae0dbfc6f60109778d928f333d88c5
        """
        user_forgot = input("Forgot password\nEnter 1 to access your password hint question.\nEnter 2 to try again")
        attempts= 0
        if "1" in user_forgot:
            while attempts < 3:
                hint = input("hintAccessAns")
                #return self.hints
                if hint in self.hints:
                    print ("hint matches") 
                    break
                else:
                    attempts += 1
                    print (f"try again, {3 - attempts} attempts remaining")
        print("Attempt exceeded")
            
        

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
        """ 
        expire_day = self.start_day + datetime.timedelta(90)
        days_left = expire_day - datetime.datetime.now()
       # while self.current_day != expire_day:
           # self.current_day+=datetime.timedelta(1)
            #days_left -=datetime.timedelta(1)
        if self.start_day == expire_day:
            print("you have to generate a new password today!")
        else:
            print(f"you have {abs(days_left)} until you will need a new password")
            
        
    def reset_password(self):
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
    
        answer1 = input("Enter your answer to your password hint question ")
        if answer1 == self.responses[0]:
            print("your new password is: ", self.generate_password(8,3,3))
        else:
            raise ValueError ("One or more of your answers were incorrect please try again")
            
     
     
     
    
    def used_password(self):  
        """
    Checks to see if the generated password has been used before by reading the created file into a list
    ran through an if statement.
    
    Return:
    If password has been used before will return "Password has been used before", and if not it 
    will return "Password has not been used before.
     
    Side Effect: 
    Passwords in the file and the generated password have been hashed.
        """
         
        password_list = open("password_file").readlines()
        gen_password = input("Input generated password here.")
        new_password = hashlib.sha256(gen_password.encode("utf-8"))
        new_hash = new_password.hexdigest()
        if new_hash in password_list: 
            print ("Password has been used before.")
        else:
            print("Password has not been used before.")
    

    def common_password(self,filename):
        """
    Checks to see if the password generated is common by reading a 
    txt file of the most common passwords into a list. It will prompt 
    the user to input the generated password and run through each password 
    in the list.
    
    Args:
        filename (str): indicates the path to a file to be read in.
    
    Returns:
        Will return Password is Common if the inputed password matches in the list 
        and Password is not Common if it does not match.
        
    Side Effect: 
        Will record password if password has not been used yet. 
        """
        #with open('password_file.txt') as commonPasswords:
        #    filename = commonPasswords.read()
        with open (filename, "r", encoding = "utf-8", errors="ignore") as f:
            content = f.read()
            content_list = content.split(",")
            gen_password = input("Input generated password here.")
            if gen_password in content_list:
                print("password is common")
            else: 
                print("password is not common")
                content_list.append(gen_password)

    
def parse_args(arglist):
    """ This function parses the command-line arguements"""
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help = "enter your username")
    args = parser.parse_args(arglist)
    return args

def main(username):
    trial = PasswordGenerator(username)
    print(trial.user_input(username))


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args.username)
	#passwordGenerator = PasswordGenerator(username)
	#password = passwordGenerator.generate_password()
	#print (password)
 
def security_questions(self):
	"""
	Purpose
		This function will prompt user with choice of recovering the password using security questions.
	Raises
		ValueError 	if reponse to prompt is out of acceptable string (Y/N)
					or if user answers incorrectly
	Side Effects
		User does not get to choose the new password
	"""



def used_password(self,password):
    """ 
    Purpose:
        Checks to see if password has been used by the user before. 
        
    Args: 
         password (str): password that was generated by password_gen.
         
    Return: 
        String if password has been used before or not.
        
    Side Effect: 
        Records password if not used before. 
 """
def common_password(self,filename,password):
    """ 
    Purpose: 
        Reads a file to check how common the password is based on the password requirements. 
        
    Args: 
        filename (str): indicates the path to a file to be read in.
        password (str): password that was generated by password_gen.
        
    Returns: 
       String if password is common or not common. 
       
    Side Effect: 
        Records password if not common.
    """ 
