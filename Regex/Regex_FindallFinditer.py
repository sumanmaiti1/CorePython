# ---- exporting regular expression library----
import re

text_str = '''My Name is Sri Madhava Sanatani and i was born on 31-12-1999.
I live in India.I work in ABN Amro.My email id is srimadhava1999@gmail.com.
My pin number is 701902. My secondary email is test_email@email.com.
I started working on 01-01-2013. 
I have 11 years of experience. I work in Python,Pytest,Robot Framework,Selenium,API testing,QTP etc.'''

# we will see the FindAll method here. It finds all occurrences of a pattern in a List.
pattern = r'([\w@.]+com)'  # this will fetch al the email ids and return a list
search1 = re.findall(pattern, text_str)
if len(search1) > 0:
    print(search1)
else:
    print('No Match found')

# we will see the FindIter method here. it returns an iterator yielding a Match object for each match
#pattern1 = r'(?<=\D)\d{4}'
pattern1 = r'\b[1-9][0-9]{3}\b'  # --- This is the regular expression for 1000 to 9999
iter1 = re.finditer(pattern1, text_str)
print(iter1)
for i in iter1:
    print(i.group())
