# ---- exporting regular expression library----
import re

text_str = '''My Name is Sri Madhava Sanatani and i was born on 31-12-1999.
I live in India.I work in ABN Amro.My email id is srimadhava1999@gmail.com.
My pin number is 701902. My secondary email is test_email@email.com.
I started working on 01-01-2013. 
I have 11 years of experience. I work in Python,Pytest,Robot Framework,Selenium,API testing,QTP etc.'''

# we will see the search method here. Search a string for the presence of a pattern and return first match.
pattern = r'((0[1-9]|[1-2][0-9]|3[0-1])-(0[1-9]|1[0-2])-([0-9][0-9]{1,3}))'
search1 = re.search(pattern, text_str)
print(search1.group())

# we will see the FullMatch method here. it Matches a regular expression pattern to all of a string.
text_str = 'My Name is Sri Madhava Sanatani and i was born on 31-12-1999.'
pattern1 = r'My[\w\d\s].*'
fullmatch1 = re.fullmatch(pattern1, text_str, re.IGNORECASE)
print(fullmatch1.group())
