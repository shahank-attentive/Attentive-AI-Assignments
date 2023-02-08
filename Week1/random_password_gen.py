import string
import random


# Function to get a list of random characters of length 'length' and from a specific rule at a time
def funct(rule_string, length):
    ans_calc = []
    if length > len(
        rule_string
    ):  # When length we want is greater that whole rule length
        while length:
            if length > len(rule_string):
                ans_calc.extend(random.sample(rule_string, len(rule_string)))
                length -= len(rule_string)
            else:
                ans_calc.extend(random.sample(rule_string, length))
                length = 0
    else:
        ans_calc.extend(random.sample(rule_string, length))

    return ans_calc


# Rules for password
option1 = "Contains Uppercase Character"
option2 = "Contains Lowercase Character"
option3 = "Contains Number"
option4 = "Contains Special characters(only @, #, - and $)"


rules_dict = {1: option1, 2: option2, 3: option3, 4: option4}

# Printing the rules for user
for key, value in rules_dict.items():
    print(key, value)

# Dictionary of values of rules
dict = {
    1: string.ascii_uppercase,
    2: string.ascii_lowercase,
    3: string.digits,
    4: "@#-$",
}

print(
    '\n Specify the rule no. you want for your password /you can select multiple rules..\n (Write rules seperated by space)\nor Enter "No rules" if you want no rules'
)
stringOfRules = input()

list_of_rule_no = []  # This list contains the rule no that user wants in his password
if stringOfRules == "No rules":  # If user selects no  rules then all rules should apply
    list_of_rule_no = [1, 2, 3, 4]
else:
    list_of_rule_no = stringOfRules.split()

length = int(
    input(
        "Enter the length of password you want: \n (Enter length between 5 to 100 for a good password)\n"
    )
)
while not (5 <= length <= 100):
    length = int(input("Enter the valid length :"))

size = len(list_of_rule_no)
listModified = []  # List that contains final password characters
# Including every rules is must so I included equal length from all the rules
k = length // size  # k is the length of random words we want from each rules
for i, a in enumerate(list_of_rule_no):
    if i == (len(list_of_rule_no) - 1):  # To get the remaining length in last iteration
        to_merge = funct(dict[int(a)], length)
    else:
        to_merge = funct(dict[int(a)], k)
        length -= k  # Substracting k each time to take note of remaining length

    listModified.extend(to_merge)

listModified = random.sample(
    listModified, len(listModified)
)  # again randomizing the whole list
ans = "".join(listModified)  # converting list to string
print(ans)
