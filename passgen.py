import random
import string
import pyperclip

def passwordInfo():
    mypassword = ''
    input_type = ''
    input_length = 0
    chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    chars_U = string.ascii_uppercase
    chars_L = string.ascii_lowercase
    chars_N = string.digits
    chars_A = string.ascii_letters
    chars_S = "!@#$%^&*()?"   
    while True:
        print("password type: (strong/medium/weak/vweak/pin)")
        input_type = str(input()).lower()
        if input_type not in ["strong", "medium", "weak", "vweak", "pin"]:
            print('Incorrect input')
            continue
        else:
            break
    while True:
        if input_type == "strong":
            print("password length: (min 8)")
            input_length = int(input())
            if input_length >= 8:
                randomSource = chars
                mypassword = random.choice(string.ascii_lowercase)
                mypassword += random.choice(string.ascii_uppercase)
                mypassword += random.choice(string.digits)
                mypassword += random.choice("!@#$%^&*()?")
                for i in range(input_length - 4):
                    mypassword += random.choice(randomSource)
                passwordList = list(mypassword)
                random.SystemRandom().shuffle(passwordList)
                mypassword = ''.join(passwordList)
                return mypassword
            else:
                print("must be an int >= 8")
                continue
        elif input_type == "medium":
            print("password length: (min 8)")
            input_length = int(input())
            if input_length >= 8:
                randomSource = chars_U + chars_L + chars_N
                mypassword = random.choice(string.ascii_lowercase)
                mypassword += random.choice(string.ascii_uppercase)
                mypassword += random.choice(string.digits)
                for i in range(input_length - 3):
                    mypassword += random.choice(randomSource)
                passwordList = list(mypassword)
                random.SystemRandom().shuffle(passwordList)
                mypassword = ''.join(passwordList)
                return mypassword
            else:
                print("must be an int >= 8")
                continue
        elif input_type == "weak":
            print("password length: (min 6)")
            input_length = int(input())
            if input_length >= 6:
                randomSource = chars_A
                mypassword = random.choice(string.ascii_lowercase)
                mypassword += random.choice(string.ascii_uppercase)
                for i in range(input_length - 2):
                    mypassword += random.choice(randomSource)
                passwordList = list(mypassword)
                random.SystemRandom().shuffle(passwordList)
                mypassword = ''.join(passwordList)
                return mypassword
            else:
                print("must be an int >= 6")
                continue
        elif input_type == "vweak":
            print("password length: (min 1)")
            input_length = int(input())
            if input_length >= 1:
                mypassword = (''.join([random.choice(list(chars_L))for i in range (input_length)]))
                return mypassword
            else:
                print("must be an int >= 1")
                continue
        elif input_type == "pin":
            print("pin length: (min 3)")
            input_length = int(input())
            if input_length >= 3:
                mypassword = (''.join([random.choice(list(chars_N))for i in range (input_length)]))
                return mypassword
            else:
                print("must be an int >= 3")
                continue

pw = passwordInfo()
print(f'Password: {pw} \nCopied to clipboard')
pyperclip.copy(pw)
