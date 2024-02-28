import re
from collections import Counter
# url: https://www.geeksforgeeks.org/python-programming-examples/?ref=shm
# This file contains the practise problem given in GeeksForGeeks (url is mentioned above)

# 1. Python Program to Check if String Contain Only Defined Characters using Regex
def ex_1(test_str, allowed_characters):
    pattern = re.compile(r'^[%s]+$' % allowed_characters, re.I)
    print('Valid String' if pattern.search(test_str) else 'Invalid String!!!')

# 2. Python program to Count Uppercase, Lowercase, special character and numeric values using Regex
def ex_2(test_str):
    print('No. of uppercase characters:', len(re.findall(r'[A-Z]', test_str)))
    print('No. of lowercase characters:', len(re.findall(r'[a-z]', test_str)))
    print('No. of numeric characters:', len(re.findall(r'\d', test_str)))
    print('No. of numeric characters:', len(re.findall(r'\W', test_str)))

# 3. Python Program to find the most occurring number in a string using Regex
def ex_3(test_str):
    counter1 = Counter(re.findall(r'\d+', test_str))
    print('Most occuring number:', max(counter1, key=counter1.get))

# 4. Python Regex to extract maximum numeric value from a string
def ex_4(test_str):
    print('Maximum numeric value is:', max(re.findall(r'\d+', test_str)))

# 5. Python Program to put spaces between words starting with capital letters using Regex
def ex_5(test_str):
    print(re.sub(r'([a-z])?([A-Z])', r'\1 \2', test_str).lower())

# 6. Python – Check whether a string starts and ends with the same character or not
def ex_6(test_str):
    print('String starts and ends with the same character' if re.search(r'^([\w\W])$|^([\w\W]).*\2$', test_str) else '''String Doesn't start and end with the same character''')

# 7. Python regex to find sequences of one upper case letter followed by lower case letters
def ex_7(test_str):
    print('Sequence pattern found' if re.search(r'[A-Z][a-z]', test_str) else 'Sequence pattern is NOT found !!!')

# 8. Python Program to Remove duplicate words from Sentence
def ex_8(test_str):
    print(re.sub(r'\b(\w+)\b.+\1', r'\1', test_str, 0, re.I))

# 9. Python | Remove all characters except letters and numbers
def ex_9(test_str):
    print(re.sub(r'[\W_]+', '', test_str))

# 10. Python Regex | Program to accept string ending with alphanumeric character
def ex_10(test_str):
    print('Accept' if re.search(r'\w+$', test_str) else 'Discard')

# 11.Python Regex – Program to accept string starting with vowel
def ex_11(test_str):
    print('Accept' if re.search(r'^[aeiou]+', test_str, re.I) else 'Discard')

# 12. Python Program to check if a string starts with a substring using regex
def ex_12(test_str, substring):
    print('Substring Exists' if re.search(substring, test_str, re.I) else 'Substring Does Not Exist')

# 13. Python Program to Check if an URL is valid or not using Regular Expression
def ex_13(test_str):
    print('Valid Url' if re.search(r'^https*://w{3}.\w{2,256}.\w+/?$', test_str) else 'Invalid URL !!!')

# 14. Parsing and Processing URL using Python – Regex
def ex_14(test_str):
    print(re.match(r'(?P<Protocol>https?)(://www.)(?P<Hostname>\w{2,256})(..*)', test_str).groupdict())

# 15. Python Program to validate an IP address using ReGex
def ex_15(test_str):
    print('Valid IPV4' if re.search(r'^([1-9]|([1-9][0-9]{1,2}))\.([1-9]|([1-9][0-9]{1,2}))\.([1-9]|([1-9][0-9]{1,2}))\.([1-9]|([1-9][0-9]{1,2}))$', test_str) else 'Invalid IP')

# 16. Python Program to Check if email address valid or not
def ex_16(test_str):
    print('Valid email' if re.search(r'^[\w.]*@[\w.-]+.[a-z]{2,}$', test_str) else 'Invalid email !!!')

# 17. Python program to find files having a particular extension using RegEx
def ex_17(test_list=['abc.txt','12tesre.xlsx','hello.py','test.accdb']):
    for item in test_list:
        search= re.search(r'\b(\w+)(.\w+)\b', item)
        print(f'File:{item} , File Name:{search.group(1)} , File Extension:{search.group(2)}')

# 18. Python program to extract IP address from file
# This is repeating. Already have written regular expression for IP address. in EX_15

# 19. Python program to check the validity of a Password
# Primary conditions for password validation:
# Minimum 8 characters.
# The alphabet must be between [a-z]
# At least one alphabet should be of Upper Case [A-Z]
# At least 1 number or digit between [0-9].
# At least 1 character from [ _ or @ or $ ].

def ex_19(test_str):
    str_flag = 'False'
    if len(test_str)>=8:
        if re.search(r'[a-z]',test_str):
            if re.search(r'[A-Z]',test_str):
                if re.search(r'[0-9]', test_str):
                    if re.search(r'[_@$]',test_str):
                        str_flag= 'True'
                    else:
                        print(r'_ or @ or $ is not present in the password')
                else:
                    print('Digit is not present in the password')
            else:
                print('Uppercase leter is not present in the password')
        else:
            print('Lowercase leter is not present in the password')
    else:
        print('Passwprd is Less than 8 characters.')

    print('Valid Password' if str_flag=='True' else 'Invalid Password')

# 20. Categorize Password as Strong or Weak using Regex in Python
# Conditions to be fulfilled are:
# Minimum 9 characters and maximum 20 characters.
# Cannot be a newline or a space
# There should not be three or more repeating characters in a row.
# The same string pattern(minimum of two character length) should not be repeating.
def ex_20(test_str):
    str_flag = 'False'
    if 9 <=len(test_str)< 21:
        if not re.search(r'[\n\s]',test_str):
            if not re.search(r'(\w)\1\1',test_str):
                if not re.search(r'(\w\w).+?\1', test_str):
                    str_flag = 'True'
                else:
                    print('Same string pattern(minimum of two character length) repeating in the password')
            else:
                print('Three or more repeating characters in a row in the password')
        else:
            print('A newline or a space in the password')
    else:
        print('Password is not between 9-20 characters.')

    print('Valid Password' if str_flag=='True' else 'Invalid Password')

# ex_20('Qggf!@ghf3'), ex_20('aaabnil1gu'), ex_20('Geeksforgeeks'), ex_20('Aasd!feasnm'), ex_20('772*hdf77'), ex_20(' ')
# ex_19('R@m@_f0rtu9e$'), ex_19('Rama_fortune$'), ex_19('Rama#fortu9e')
# ex_17(["gfg.html", "geeks.xml", "computer.txt", "geeksforgeeks.jpg", 'test.accdb', 'Xl123.xlsx'] )
# ex_16('ankitrai326@gmail.com'), ex_16('my.ownsite@our-earth.org'), ex_16('ankitrai326.com'),
# ex_15('203.120.223.13'), ex_15('000.12.234.23.23'), ex_15('2F33:12a0:3Ea0:0302'), ex_15('I.Am.not.an.ip')
# ex_14('https://www.geeksforgeeks.org/courses'), ex_14('http://www.google.co.in')
# ex_13('https://www.geeksforgeeks.org/'), ex_13('https:// www.geeksforgeeks.org/')
# ex_12('Jay Shree Ram','ram'), ex_12('Jay Shree Ram','Krishna')
# ex_11('animal'), ex_11('zebra'), ex_11('Om namo Bhagwate Basudevaya')
# ex_10('ankitrai326'), ex_10('ankirai@')
# ex_9('  abcjw:, .@! eiw')
# ex_8('Good Good bye bye world world'), ex_8('Ram went went to to his home'), ex_8('Hello hello world world')
# ex_7('Jay Shree Ram'), ex_7('har har mahadev'), ex_7('jayshreeKrishna'), ex_7('Geeks')
# ex_6('blob'), ex_6('tail'), ex_6('5'), ex_6('0tild0'), ex_6('amal is in insta'), ex_6('Jay Shree Ram')
# ex_5('BruceWayneIsBatman'), ex_5('GeeksForGeeks')
# ex_4('100klh564abc365bg'), ex_4('abchsd0sdhs')
# ex_3('geek55of55geeks4abc3dr2'), ex_3('abcd1def2high2bnasvd3vjhd44')
# ex_2('ThisIsGeeksforGeeks!, 123')
# ex_1('Jay Shree Ram 123_%', 'aehjmrsy123_ %'), ex_1('Jay Shree Q Ram 123_%', 'aehjmrsy123_ %'),
