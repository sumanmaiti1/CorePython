# ---- exporting regular expression library----
import re

text_str = '''My Name is Sri Madhava Sanatani and i was born on 31-12-1999.
I live in India.I work in ABN Amro.My email id is srimadhava1999@gmail.com.
My pin number is 701902. My secondary email is test_email@email.com.
I have 11 years of experience. I work in Python,Pytest,Robot Framework,Selenium,API testing,QTP etc.'''

# We will look for compile method. It Compiles a pattern into a Pattern object.
pattern1 = re.compile(r'\bpy.*', re.I)  # ------ Will fetch Python,Pytest,Robot Framework,Selenium,API testing,QTP etc.
pattern2 = re.compile(r'(0[1-9]|3[0-1]|[1-2][0-9]])-(0[1-9]|1[0-2])-([0-9][0-9]{1,3})')  # -- fetches dd-mm-yyyy
print(pattern1.search(text_str).group())  # -- fetches Python,Pytest,Robot Framework,Selenium,API testing,QTP etc.


# We will now see Match Method. It matches a regular expression pattern to the beginning of a string.
match1 = re.match(r'My .*', text_str, re.MULTILINE)  # -- My Name is Sri Madhava Sanatani and I was born on 31-12-1999.
match2 = re.match(pattern1, text_str)  # ---- This will not fetch anything as it starts in between the test string
if match1:
    print(match1.group())
    print(match1.start())
    print(match1.end())
    print(match1.span())
    print(match1.re)
    print(match1.regs)
    print(match1.string)
    print(match1.groups())
else:
    print('No match found...')


if match2:
    print('Match Found')
else:
    print('No Match found')
