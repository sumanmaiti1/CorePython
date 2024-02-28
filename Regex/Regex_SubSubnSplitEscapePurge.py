# ---- exporting regular expression library----
import re

text_str = '''My Name is Sri Madhava Sanatani and i was born on 31-12-1999.
I live in India.I work in ABN Amro.My email id is srimadhava1999@gmail.com.
My pin number is 701902. My secondary email is test_email@email.com.
I have 11 years of experience. I work in Python,Pytest,Robot Framework,Selenium,API testing,QTP etc.'''

# We will look for Sub method. It substitutes occurrences of a pattern found in a string.
print(re.sub(r'\bPy', 'Zy', text_str, re.I))
print(re.sub(r'\bpy', 'Zy', text_str, 1, re.I))

# We will look for Subn method. It is same as sub, but also return the number of substitutions made.
print(re.subn(r'\bPy', 'Zy', text_str, re.I))
print(re.subn(r'\bpy', 'Zy', text_str, 1, re.I))

# We will look for Split method. It  splits a string by the occurrences of a pattern.
print(re.split(r'\n', text_str))
print(re.split(r'\s', text_str))

# We will look for Escape method. It Backslash all non-alphanumerics in a string.
print(re.escape(r'https:\\suman_Maiti@yahoomail.com\profile[0-9a-z\?#$^*]'))

# We will look for Purge method. It Clears the regular expression cache.
re.purge()