# Tien Phan
# censor dispenser - Python String Practice


# These are the emails you will be censoring. The open() function is opening the text file that the emails are
# contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

testString = "Test String"

def censorString(file, string):
    newString = ""
    for i in range(len(string)):
        newString += "*"
    return file.replace(string, newString)

def censor_multiple_strings(file, string):
    for i in string:
        newString = i
        censor = ""
        # print(i)
        for j in range(len(i)):
            censor += "*"
        # print(censor)
        file = file.replace(newString, censor)
    return file



# tester
# print(censorString(email_one, "learning algorithms"))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]
print(censor_multiple_strings(email_two, proprietary_terms))
