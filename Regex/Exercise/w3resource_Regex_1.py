import re

# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z,
# A-Z and 0-9).
def ex_1(test_str):
    if re.search(r'[^a-zA-Z0-9 ]', test_str):
        print('string contains certain set of characters apart from a-z,A-Zand 0-9')
    else:
        print('string contains only a certain set of characters')

# 2. Write a Python program that matches a string that has an 'a' followed by zero or more b's
def ex_2(test_str):
    print('Pass' if re.search(r'ab*$', test_str) else 'Fail')

# 3. Write a Python program that matches a string that has an 'a' followed by one or more b's.
def ex_3(test_str):
    print('Pass' if re.search(r'ab+$', test_str) else 'Fail')

# 4. Write a Python program that matches a string that has an 'a' followed by zero or one 'b'
def ex_4(test_str):
    print('Pass' if re.search(r'ab?$', test_str) else 'Fail')

# 5. Write a Python program that matches a string that has an 'a' followed by three 'b'.
def ex_5(test_str):
    print('Pass' if re.search(r'ab{3}$', test_str) else 'Fail')

# 6. Write a Python program that matches a string that has an 'a' followed by two to three 'b'
def ex_6(test_str):
    print('Pass' if re.search(r'ab{2,3}$', test_str) else 'Fail')

# 7. Write a Python program to find sequences of lowercase letters joined by an underscore.
def ex_7(test_str):
    print('Found a Match' if len(re.findall(r'^[a-z]+_[a-z]+$', test_str)) > 0 else 'Not Matched.')

# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def ex_8(test_str):
    print('Found a Match' if re.search(r'[A-Z][a-z]+', test_str) else 'Not matched!')

# 9. Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.
def ex_9(test_str):
    print('Found a Match' if re.search(r'a.*b$', test_str) else 'Not matched!')

# 10. Write a Python program that matches a word at the beginning of a string.
def ex_10(test_str):
    print('Found a Match' if re.search(r'^[a-zA-Z]+\b', test_str) else 'Not matched!')

# 11. Write a Python program that matches a word at the end of a string, with optional punctuation.
def ex_11(test_str):
    print('Found a Match' if re.search(r'[a-zA-Z]+\.?$', test_str) else 'Not matched!')

# 12. Write a Python program that matches a word containing 'z'.
def ex_12(test_str):
    print('Found a Match' if re.search(r'\b[\w]*z+[\w]*\b', test_str) else 'Not matched!')

# 13. Write a Python program that matches a word containing 'z', not the start or end of the word.
def ex_13(test_str):
    print('Found a Match' if re.search(r'\Bz\B', test_str) else 'Not matched!')

# 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
def ex_14(test_str):
    print('Not matched!' if re.search(r'[^a-zA-Z0-9_]+', test_str) else 'Found a Match!')

# 15. Write a Python program that starts each string with a specific number.
def ex_15(test_str):
    print('Found a Match' if re.search(r'^1.*', test_str) else 'Not matched!')

# 16. Write a Python program to remove leading zeros from an IP address.
def ex_16(test_str):
    print(re.sub(r'\.$', '.0', re.sub(r'\.\.', '.0.', re.sub(r'000', '0', re.sub(r'\.0*', '.', test_str)))))

# 17. Write a Python program to check for a number at the end of a string.
def ex_17(test_str):
    print('Found a Match' if re.search(r'.*\d$', test_str) else 'Not matched!')

# 18. Write a Python program to search for numbers (0-9) of length between 1 and 3 in a given string.
# "Exercises number 1, 12, 13, and 345 are important"
def ex_18(test_str):
    print(re.findall(r'\d{1,3}', test_str))

# 19. Write a Python program to search for literal strings within a string.
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
def ex_19(search_str, test_str='The quick brown fox jumps over the lazy dog'):
    print('Found a Match' if re.search(search_str, test_str) else 'Not matched!')

# 20. Write a Python program to search for a literal string in a string and also find the location within the original string where the pattern occurs.
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
def ex_20(search_str, test_str='The quick brown fox jumps over the lazy dog'):
    print(f'Start Position: {re.search(search_str, test_str).start()} , End Position: {re.search(search_str, test_str).end()}' if re.search(search_str, test_str) else 'Search String is not present !')

# 21. Write a Python program to find the substrings within a string.
# Sample text :'Python exercises, PHP exercises, C# exercises'
# Pattern :'exercises'
def ex_21(test_str, search_str):
    print(f'Found {[search_str]} srting {len(re.findall(search_str, test_str))} times in {[test_str]}' if re.findall(search_str, test_str) else 'Not matched!')

# 22. Write a Python program to find the occurrence and position of substrings within a string.
def ex_22(test_str, search_str):
    if re.finditer(search_str, test_str):
        for item in re.finditer(search_str, test_str):
            print(f'Start position:{item.start()} , End Position:{item.end()}, Span:{item.span()}')
    else:
        print(f'{[test_str]} Not found in {[search_str]}')

# 23. Write a Python program to replace whitespaces with an underscore and vice versa.
def ex_23(test_str):
    print(re.sub(r'>>>', ' ', re.sub(' ', '_', re.sub(r'_', '>>>', test_str))))

# 24. Write a Python program to extract year, month and date from an URL.
def ex_24(test_str):
    print(re.search(r'\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])', test_str).group() if re.search(r'\d{4}/(0[1-9]|1[0-2])/(0[1-9]|[1-2][0-9]|3[0-1])', test_str) else 'Not Found !!!')

# 25. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format
def ex_25(test_str):
    match = re.search(r'(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])', test_str)
    if match:
        print('Retrieved date in YYYY-MM-DD format is {}'.format(match.group()))
        print(f'Retrieved date in DD-MM-YYYY format is {match.group(3)}-{match.group(2)}-{match.group(1)}')
    else:
        print('Date Not Found in String!!!')

# 26. Write a Python program to match if two words from a list of words start with the letter 'P'.
def ex_26(test_list):
    for item in test_list:
        print(item if re.search(r'\b[P].*\b[P].*', item) else '')

# 27. Write a Python program to separate and print the numbers in a given string
def ex_27(test_str):
    print('\n'.join(re.findall(r'\d+', test_str)))

# 28. Write a Python program to find all words starting with 'a' or 'e' in a given string.
def ex_28(test_str):
    print(re.findall(r'(?<=\s)[a|e]\w+', test_str))

# 29. Write a Python program to separate and print the numbers and their position in a given string.
def ex_29(test_str):
    if re.finditer(r'\d+', test_str):
        for item in re.finditer(r'\d+', test_str):
            print(f' Number is:{item.group()} and Starting Position:{item.start()}')

# 30. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
def ex_30(test_str):
    print(re.sub(r'Road','Rd.', test_str))

# 31. Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
def ex_31(test_str):
    print(re.sub(r'[ ,\.]', ':', test_str))

# 32. Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.
def ex_32(test_str):
    print(re.sub(r'[ ,\.]', ':', test_str, 2))

# 33. Write a Python program to find all five-character words in a string.
def ex_33(test_str):
    print(re.findall(r'\b[a-zA-Z0-9]{5}\b', test_str) if re.findall(r'\b[a-zA-Z0-9]{5}\b', test_str) else 'No five-character words found in a string.')

# 34. Write a Python program to find all three, four, and five character words in a string.
def ex_34(test_str):
    print(re.findall(r'\b[a-zA-Z0-9]{3,5}\b', test_str) if re.findall(r'\b[a-zA-Z0-9]{3,5}\b', test_str) else 'No three, four or five-character words found in a string.')

# 35. Write a Python program to find all words that are at least 4 characters long in a string.
def ex_35(test_str):
    print(re.findall(r'\b[a-zA-Z0-9]{4,}\b', test_str) if re.findall(r'\b[a-zA-Z0-9]{4,}\b', test_str) else 'All characters are less than 4 characters in the string.')

# 36. Write a Python program to convert a camel-case string to a snake-case string.
def ex_36(test_str):
    print(re.sub(r'^_?', '', re.sub(r'([A-Z])', r'_\1', test_str)).lower())

# 37. Write a python program to convert snake-case string to camel-case string.
def ex_37(test_str):
    test_list=[]
    for item in re.split(r'_', test_str):
        test_list.append(item.title())
    print(''.join(test_list))

# 38. Write a Python program to extract values between quotation marks of a string.
def ex_38(test_str):
    print(re.findall(r'"(.*?)"', test_str))

# 39. Write a Python program to remove multiple spaces from a string.
def ex_39(test_str):
    print(re.sub(r' +', ' ', test_str))

# 40. Write a Python program to remove all whitespaces from a string.
def ex_40(test_str):
    print(re.sub(r'\s+', '_', test_str))

# 41. Write a Python program to remove everything except alphanumeric characters from a string.
def ex_41(test_str):
    print(re.sub(r'\W', ' ', test_str))

#  42. Write a Python program to find URLs in a string.
def ex_42(test_str):
    print(re.findall(r'https?:\/\/.*?\.com', test_str))

# 43. Write a Python program to split a string into uppercase letters.
def ex_43(test_str):
    ucase_list=re.findall(r'[A-Z]', test_str)
    ucase_str=''
    if len(ucase_list)>0:
        ucase_str=''.join(list(set(ucase_list)))
        pattern=re.compile('([' + ucase_str + '])')
        print(pattern.split(test_str))
    else:
        print('Provided String Does not Contain any uppercase characters')

# 44. Write a Python program to do case-insensitive string replacement.
def ex_44(test_str):
    print(re.sub(r'py', 'PY', test_str, 0, re.I))

# 45. Write a Python program to remove ANSI escape sequences from a string.
# Not sure what is an ANSI escape sequence.

# 46. Write a Python program to find all adverbs and their positions in a given sentence
# not sure how to identify adverb logic. just searchng for word ending with 'ly' is not solution.
# many adverbs are there which don't have 'ly' in it. like too, here, far, soon, there etc.

# 47. Write a Python program to split a string with multiple delimiters.
# this is already achieved in Ex_43

# 48. Write a Python program to check a decimal with a precision of 2.
def ex_48(test_str):
    print('Valid Decimel. Upto 2 digit.' if re.search(r'^\d+(\.\d{0,2})?$', test_str) else 'Not a Valid Decimal of 2 digits')

# 49. Write a Python program to remove words from a string of length between 1 and a given number.
def ex_49(test_str,start_len, end_len):
    a=r'\b\w{%s,%s}\b'%(start_len, end_len)
    pattern = re.compile(a)
    print(pattern.sub('', test_str))

# 50. Write a Python program to remove the parenthesis area in a string.
# Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
# Expected Output: example w3resource github stackoverflow

def ex_50(test_list):
    new_list=[]
    for item in test_list:
        new_list.append(re.sub(r'\(.*?\)', '', item))
    print(new_list)

# 51. Write a Python program to insert spaces between words starting with capital letters.
def ex_51(test_str):
     print(re.sub(r'([a-z])([A-Z])', r'\1 \2', test_str))

# 52. Write a Python program that reads a given expression and evaluates it.
# this can be done easily without regular expression.
def ex_52(test_str):
    print(eval(test_str))

# 53. Write a Python program to remove lowercase substrings from a given string.
def ex_53(test_str):
    print(re.sub(r'[a-z]', '', test_str))

# 54. Write a Python program to concatenate the consecutive numbers in a given string.
def ex_54(test_str):
    print(re.sub(r'(\d+) (\d+)', r'\1\2', test_str))

# 55. Write a Python program to convert a given string to snake case.
# this is kind of done already

# 56. Write a Python program that takes any number of iterable objects or objects with a length property and returns the longest one.
# it doesn't need regular expression

# 57. Write a Python program that checks whether a word starts and ends with a vowel in a given string. Return true if a word matches the condition; otherwise, return false.
def ex_57(test_str):
    print(True if re.search(r'\b[aeiou]\w*[aeiou]\b', test_str) else False)

# 58. Write a Python program that takes a string with some words. For two consecutive words in the said string,
# check whether the first word ends with a vowel and the next word begins with a vowel. If the program meets
# the condition, return true, otherwise false. Only one space is allowed between the words.
def ex_58(test_str):
    print(True if re.search(r'\b\w*[aeiou] [aeiou]\w*\b', test_str) else False)


# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
#                   individual functions are called below
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# ex_58('These exercises can be used for practice'), ex_58('Following exercises should be removed for practice'), ex_58('i use these stories in my classroom')
# ex_57('Red orange White'), ex_57('Red White Black'), ex_57('abcd dkise eosksu')
# ex_54('Enter at 31 20 Kearny Street. The security desk can direct you to floor 1 12. Please have your identification ready.')
# ex_53('KDeoALOklOOHserfLoAJSIskdsf')
# ex_52('4-3*2/4')
# ex_51('JayShreeRam HarHarMahadev')
# ex_50(["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"])
# ex_49('Jana Gana Mana Adhinayaka jaya he. Bharata Bhagya vidhata',3,5)
# ex_48('123.11'), ex_48('123.1'), ex_48('123'), ex_48('0.21'), ex_48('123.1243'), ex_48('3.1183'), ex_48('A4334.56')
# ex_44('I am doing pYthon programming Exercise')
# ex_43('ShreeRamJiKiJay'), ex_43('Har Har Mahadev'), ex_43('@    Om Namo Bhagvate Basudevaya')
# ex_42('<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>')
# ex_41('I am #$ doing  Python  ^&!   Exercises         and tihs is problem No_40.')
# ex_40('I am  doing  Python     Exercises         .')
# ex_39('I am  doing  Python     Exercises         .')
# ex_38('"what is your name?" "Suman Maiti"'), ex_38('"Python", "PHP", "Java"')
# ex_37('jay_shree_ram'), ex_37('python_exercises')
# ex_36('JayShreeRam'), ex_36('PythonExercises')
# ex_35('The quick brown fox jumps over the lazy dog and falls from the building.'), ex_35('Jay Sri Ram')
# ex_34('The quick brown fox jumps over the lazy dog and falls from the building.'), ex_34('He naaath Narayan Basudev')
# ex_33('The quick brown fox jumps over the lazy dog and falls from the building.'), ex_33('Har Har Mahadev')
# ex_32('Jay Shree Ram . Jay Shree Krishna, Har Har Mahadev'), ex_32('Python Exercises, PHP exercises.')
# ex_31('Jay Shree Ram . Jay Shree Krishna, Har Har Mahadev')
# ex_30('21 Ramkrishna Road'), ex_30('21 Ramkrishna Rd.'), ex_30('Jay Shree Krishna')
# ex_29('The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly.')
# ex_28('The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly.')
# ex_27('Ten 10, Twenty 20, Thirty 30 Fourty40')
# ex_26(["Python PHP", "Java JavaScript", "c c++"])
# ex_25('i was born on 1999-01-31')
# ex_24('https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author')
# ex_23('My name is Suman_Maiti')
# ex_22('Python exercises, PHP exercises, C# exercises','exercises')
# ex_21('Python exercises, PHP exercises, C# exercises','exercises')
# ex_20('fox'),ex_20('dog'),ex_20('horse')
# ex_19('fox'),ex_19('dog'),ex_19('horse')
# ex_18('Exercises number 1, 12, 13, and 345 are important')
# ex_17('2'), ex_17(' 3'), ex_17('Test 3'), ex_17('Test3'), ex_17('Test@'), ex_17('Test3 @')
# ex_16('192.115.223.369'), ex_16('000.110.023.369'), ex_16('192.000.300.000')
# ex_15('1. Test zmez'), ex_15('aszr1'), ex_15('2zase_12')
# ex_14('Test zmez'), ex_14('aszr1'), ex_14('zase_12'), ex_14('bazX '), ex_14('bazX%')
# ex_13('test zmez'), ex_13('aszr'), ex_13('zase'), ex_13('baz')
# ex_12('The quick brown fox jumps over the lazy dog.'), ex_12('Python Exercises')
# ex_11('The quick brown fox jumps over the lazy dog.'), ex_11(' The quick brown fox jumps over the lazy dog. '), ex_11(' The quick brown fox jumps over the lazy dog ')
# ex_10('The quick brown fox jumps over the lazy dog.'), ex_10(' The quick brown fox jumps over the lazy dog.')
# ex_9('aabbbbd'), ex_9('aabAbbbc'), ex_9('accddb#bjjjb')
# ex_8('AaBbGg'), ex_8('Python'), ex_8('python'), ex_8('PYTHON'), ex_8('aA'), ex_8('Aa')
# ex_7('aab_cbbbc'), ex_7('aab_cbbbc'), ex_7('aab_Abbbc'), ex_7('Aaab_abbbc'), ex_7('aaAab_abbbZc')
# ex_6('a'), ex_6('ab'), ex_6('abb'), ex_6('abbb'), ex_6('abbbc'), ex_6('cbabbbb')
# ex_5('a'), ex_5('ab'), ex_5('abb'), ex_5('abbb'), ex_5('abbbc'), ex_5('cbabbb')
# ex_4('a'), ex_4('ab'), ex_4('abb'), ex_4('abc'), ex_4('bc')
# ex_3('a'), ex_3('ab'), ex_3('abb'), ex_3('abc'), ex_3('bc')
# ex_2('a'), ex_2('ab'), ex_2('abb'), ex_2('abc'), ex_2('bc')
# ex_1('Jay Shree Ram 1234567890#'), ex_1('JayShreeRam1234567890')
