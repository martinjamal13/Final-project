import datetime
import sys
import argparse
import hashlib
import random
import string
import builtins
from unittest import mock 
from pass_generator.py import PasswordGenerator

# Happy path
self.user_input("johndoe1")
    # Generate password
    print("1")
    # Password hint
    print("2")
    # Reset password
    print("3")
    # Check if password has been used before
    print("4")
    # Check if my password is common
    print("5")
    # Check how days until I need to change my password
    print("6")
    # Exit program
    print("7")

# Unhappy path
self.user_input(nonstring)
    print("letter")
    print("#$%")
    print("8")

# Happy path
self.selection1()
    print("1")
    print("mars")
    print("what's my dog's name?")
    print("rowdy")
    print("n")

    print("12")
    print("mars")
    print("skateboarding")
    print("what's my cat's name?")
    print("whisk")
    print(" ")

    print("123")
    print("mars")
    print("skateboarding")
    print("diving")
    print("who's there?")
    print("me")
    print("n")

    print("2")
    print("skateboarding")
    print("where's waldo?")
    print("here")
    print("p")

    print("21")
    print("mars")
    print("skateboarding")
    print("favorite color?")
    print("bloo")
    print("n")

    print("213")
    print("mars")
    print("skateboarding")
    print("diving")
    print("favorite beach?")
    print("sunny")
    print("$")

    print("3")
    print("diving")
    print("maiden name?")
    print("jacobson")
    print(")")

    print("31")
    print("mars")
    print("diving")
    print("vacation spot?")
    print("honolulu&hilo")
    print("n")

    print("321")
    print("mars")
    print("skateboarding")
    print("diving")
    print("best friend?")
    print("skylar")
    print("w")

# Unhappy path
self.selection1()
    print("q")
self.selection1()
    print("4")
self.selection1()
    print(" ")
self.selection1()
    print("$")


def test_used_password (capsys):
    #Happy Path
    with mock.patch('builtins.input',side_effect = ["w3g5h7j8"]):
        used_password("password_file")
        captured = capsys.readouterr()
        assert captured.out == ("987654321.\n")
    #Unhappy Path
    with mock.patch('builtins.input',side_effect = ["jennifer"]):
        used_password("password_file")
        captured = capsys.readouterr()
        assert captured.out == ("Password has been used before.\n")
    
def test_valid_password_generator():
    pwdGen = PasswordGenerator
    with pytest.raises(ValueError):
        password = pwdGen.generate_password(8, 2, 2)
        assert len(password) == 8
    

def test_valid_password_generator_minimum_limits():
    pwdGen = PasswordGenerator
    with pytest.raises(ValueError):
        password= pwdGen.generate_password(8, 2, 3)
        digitCount = 0
        alphabetCount = 0
        for s in password:
            if s.isdigit():
                digitCount += 1
            else:
                alphabetCount += 1
    
        assert len(password) == 8
        assert digitCount >= 2
        assert alphabetCount >= 3
    

def test_valid_password_generator_invalid_length():
    pwdGen = PasswordGenerator
    with pytest.raises(ValueError):
        pwdGen.generate_password(0, 2, 3)

def test_valid_password_generator_invalid_minDigits():
    pwdGen = PasswordGenerator
    with pytest.raises(ValueError):
        pwdGen.generate_password(8, 0, 3)

def test_valid_password_generator_invalid_minAlphabets():
    pwdGen = PasswordGenerator
    with pytest.raises(ValueError):
        pwdGen.generate_password(8, 3, 0)

def test_valid_password_generator_invalid_Args():
    pwdGen = PasswordGenerator
    with pytest.raises(ValueError):
        pwdGen.generate_password(8, 12, 8)

def test_valid_password_generator_invalid_total_args():
    pwdGen = PasswordGenerator
    with pytest.raises(ValueError):
        pwdGen.generate_password(8, 6, 6)

         
