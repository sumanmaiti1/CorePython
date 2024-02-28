# url : https://www.w3resource.com/python-exercises/string/#google_vignette

import collections
import itertools
import string,re,textwrap
from collections import Counter
from itertools import permutations
from functools import reduce
import difflib

# 1. Write a Python program to calculate the length of a string.
# print(len('Jay Shree Ram'))

# 2. Write a Python program to count the number of characters (character frequency) in a string.
# print(dict(Counter('google.com')))

# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string
# length is less than 2, return the empty string instead.
def ex_3(test_str):
    if len(test_str) >= 2:
        print(test_str[:2]+test_str[-2:])
    else:
        print('')
# ex_3('w3resource'), ex_3('w3'), ex_3('w')

# 4. 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def ex_4(test_str):
    new_list = list(test_str)
    for item in range(1, len(new_list)):
        if test_str[0] == new_list[item]:
            new_list[item] = '$'
    print(''.join(new_list))

# ex_4('Suman Maiti'), ex_4('restart'), ex_4('achyutam keshavam krishna damodaram')

# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def ex_5(str_1,str_2):
    print(str_2[:2] + str_1[2:] + ' ' + str_1[:2] + str_2[2:])

# ex_5('Raree','Shm')

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string
# already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def ex_6(test_str):
    if len(test_str) < 3:
        print(test_str)
    else:
        if test_str.endswith('ing'): print(test_str+'ly')
        else: print(test_str+'ing')
# ex_6('abc'), ex_6('string'), ex_6('st')

# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
def ex_7(test_str):
    if ' not ' in test_str:
        index_not=test_str.find('not')
        index_poor_after_not = test_str[index_not:].find('poor')
        if ('poor' in test_str) and ( index_poor_after_not > 0):
            print(test_str[:index_not] + 'good' + test_str[(index_not+index_poor_after_not+4):])
    else:
        print(test_str)

# ex_7('The lyrics is not that poor!''The lyrics is poor!')

# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
def ex_8(test_list):
    max_length,max_item=0,0
    for item in range(len(test_list)):
        if (len(test_list[item])> max_length): max_length,max_item= len(test_list[item]),test_list[item]
    print('Longest word: %s \nLength of the longest word: %d' % (max_item,max_length))
#ex_8(['Jay Shree Ram','Suman Maiti','Shree Krishna'])

# 9. Write a Python program to remove the nth index character from a nonempty string.
def ex_9(test_str,index):
    if len(test_str)<=index:print(f"can't remove {index}th character as given string has only {len(test_str)} characters !!!")
    else:
        print(test_str[:index]+test_str[index+1:])

#ex_9('Python', 0), ex_9('Python', 3), ex_9('Python', 5), ex_9('Python', 7)

# 10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
# test_str='may Shree RaJ'
# print(test_str[-1] + test_str[1:-1] + test_str[0])

# 11. Write a Python program to remove characters that have odd index values in a given string.
# test_str='Srimati Isita'
# new_str=''
# for item in range(0,len(test_str),2):
#     new_str=new_str + test_str[item]
# print(new_str)

# 12. Write a Python program to count the occurrences of each word in a given sentence.
# test_str=' Jay Shree Ram Jay Shree krishna Har Har Mahadev'
# test_list=test_str.split()
# print(dict(Counter(test_list)))

# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
# print(input('Enter Your name:').lower(),'\n',input('Enter Your name:').upper())

# 14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
# test_str = 'red, white, black, red, green, black'
# print(sorted(set(test_str.split(', '))))

# 15. Write a Python function to create an HTML string with tags around the word(s).
def ex_15(tag_str,test_str):
    print(f'<{tag_str}>{test_str}</{tag_str}>')
# ex_15('i','Python'), ex_15('b','Working With Strings')


# 16. Write a Python function to insert a string in the middle of a string.
def ex_16(pattern,test_str):
    if len(pattern)%2 != 0:
        print('Something wrong with te pattern, as it\'s incomplete !!')
    else:
        print(pattern[:len(pattern)//2] + test_str + pattern[len(pattern)//2:])
# ex_16('[[]]', 'Python'), ex_16('{{}}', 'PHP'), ex_16('<>', 'html'), ex_16('<<<<','RAM'), ex_16('<<>','Hari')

# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
def ex_17(test_str):
    print('{}'.format(test_str[-2:]*4) if len(test_str)>=2 else 'String length is less than 2 characters !!!')
# ex_17('Python'), ex_18('Exercises'), ex_18('s')

# 18. Write a Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
def ex_18(test_str):
    print('{}'.format(test_str[:3]) if len(test_str)>=3 else 'String:-{} length is less than 3 characters !!!'.format(test_str))
# ex_18('Python'), ex_18('Exercises'), ex_18('iss'), ex_18('ds')

# 19. Write a Python program to get the last part of a string before a specified character.
def ex_19(test_str,specified_chr):
    print('{}'.format(test_str[test_str.rfind(specified_chr)+1:]) if(test_str.find(specified_chr)>-1) else 'Specified character {} doesn\'t exist in the given string {}'.format(specified_chr,test_str) )

# ex_19('https://www.w3resource.com/python-exercises/string','/'), ex_19('https://www.w3resource.com/python-exercises/string','-'), ex_19('https://www.w3resource.com/python-exercises/string','#-')

# 20. Write a Python function to reverse a string if its length is a multiple of 4.
# a='Jay Shi Rama'
# print(''.join(reversed(a)) if len(a)%4 == 0 else 'Test String length is not multiple of 4.' )

# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
# a,search_index,uppercase_count=('Om Namo Bhagwate Basudevay',0,0)
# if len(a)<2:print('The string contains less than 2 characters.')
# elif 2<=len(a)<4: search_index=3
# else: search_index=4
# for character in a[:search_index]:
#     if character.isupper(): uppercase_count+=1
# print(a.upper() if uppercase_count>1 else a)

# 22.Write a Python program to sort a string lexicographically.
# print(tuple(sorted(tuple('*_w3resource!@'))))

# 23. Write a Python program to remove a newline in Python.
# a='''This is first line.\
# This is second line.\n
# This is third line.
# '''
# print(a)
# print(a.replace('\n',' '))

# 24. Write a Python program to check whether a string starts with specified characters.
# print('Jay Shree Ram'.startswith('jay')), print('Jay Shree Ram'.startswith('Jay'))

# 25. Write a Python program to create a Caesar encryption.
def ex_25(test_str):
    new_str, new_character='',''
    for character in test_str:
        if (68<= ord(character) <90) or (100<= ord(character) <122):
            new_character= chr(ord(character)-3)
        elif (65<= ord(character) <68) or (97<= ord(character) <100):
            new_character = chr(ord(character) + 25)
        else:
            new_character=character
        new_str+=new_character
    print(new_str)

# ex_25('Shree Krsihna Govinda Hare Murare , He Naath Narayan Vasudeva')

# 26. Write a Python program to display formatted text (width=50) as output.
test_str='''  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
'''

#print(test_str,'\n',textwrap.fill(test_str,50))

# 27. Write a Python program to remove existing indentation from all of the lines in a given text.
# print(textwrap.dedent(test_str))

# 28. Write a Python program to add prefix text to all of the lines in a string.
# print(textwrap.indent(test_str,'>'))

# 29. Write a Python program to set the indentation of the first line
# print(textwrap.fill(test_str,50,initial_indent='',subsequent_indent='<<>>'))

# 30. Write a Python program to print the following numbers up to 2 decimal places.
# print(' 2 decimal representation is {:.2f}'.format(3.9193))

# 31. Write a Python program to print the following numbers up to 2 decimal places with a sign.
# print(' 2 decimal representation is {:-.2f}'.format(13.9993))

# 32. Write a Python program to print the following positive and negative numbers with no decimal places.
# print(' Zero decimal representation is {:-.2f}'.format(13.9993))

# 33.Write a Python program to print the following integers with zeros to the left of the specified width.
# print('{0:0>+10.4f}'.format(5.123456))

# 34. Write a Python program to print the following integers with '*' to the right of the specified width.
# print('{:*<10d}'.format(12))

# 35. Write a Python program to display a number with a comma separator
# print('{:,d}'.format(1254000012))

# 36. Write a Python program to format a number with a percentage.
# print('{0:.2%}'.format(.12000236))

# 37. Write a Python program to display a number in left, right, and center aligned with a width of 10.
# print('{0:>10.2f}'.format(123.987))
# print('{0:<10.2f}'.format(123.987))
# print('{0:^10.2f}'.format(123.987))

# 38. Write a Python program to count occurrences of a substring in a string
# print('Jay Shree Ram. Jay Shree Krishna. Har Har Mahadev'.count('Jay'))

# 39. Write a Python program to reverse a string.
# print('maR eerhS yaJ'[::-1])    #method_1
# print(''.join(reversed('maR eerhS yaJ')))   #method_2
# print(''.join(sorted(list('maReerhSyaJ'),reverse=True)))
#
# def rev1(test_str='maR eerhS yaJ'):
#     rev_str=''
#     for chr in test_str:
#         rev_str= chr + rev_str
#     print(rev_str)
# def rev2(test_str):
#     if len(test_str)<1:
#         return test_str
#     else:
#         return rev2(test_str[1:]) + test_str[0]
# def rev3(test_str):
#     test_str= [test_str[x] for x in range(len(test_str)-1,-1,-1)]
#     print(''.join(test_str))
# rev1()
# print(rev2('Suman'))
# rev3('vedahaM raH raH')

# 40. Write a Python program to reverse words in a string.
# print(' '.join(reversed('Jay Shree Ram'.split())))

# 41. Write a Python program to strip a set of characters from a string.
# print('-----Jay-#Shree-Ram-----'.strip('-#'))

# 42. Write a Python program to count repeated characters in a string.
# print(Counter('thequickbrownfoxjumpsoverthelazydog'))

# 43. Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder.
# print("The area of the rectangle is {0:.3f}cm\u00b2".format(123.45))
# print("The area of the rectangle is {0:3f}cm\u00b3".format(789.001))

# 44. Write a Python program to print the index of a character in a string.
# a='Jay Shree Ram'
# a=([[a[x],x] for x in range(0,len(a))])
# for x in a: print('{} is present in position {}'.format(x[0],x[1]))

# 45. Write a Python program to check whether a string contains all letters of the alphabet.
# a= 'A quick Brown Fox Jumps over the Lazy Dog'
# b= 'A quick Brown Fox Jumps over the Lazy Dog 123 )(*&'
# flag='True'
# for words in b.split():
#     for chr in words:
#         if chr not in set(string.ascii_letters):
#             flag='False'
#             break
# print(flag)

# 46. Write a Python program to convert a given string into a list of words.
# print('A quick Brown Fox Jumps over the Lazy Dog'.split())

# 47. Write a Python program to lowercase the first n characters in a string.
def lowercase_first_n_character(test_str,n):
    if n<0 : print(f'Can\'t lowercase {n} characters.' )
    elif n>len(test_str): print(f"{n} is greater than length of the string")
    elif len(test_str)<1: print("Can't lowercase an empty string")
    else:print(test_str[0:n].lower() + test_str[n:])

# lowercase_first_n_character('JAY Shree Ram',3)

# 48. Write a Python program to swap commas and dots in a string.
# a='32.054,23'
# mk=a.maketrans(',.','.,')
# print(a.translate(mk))

# 49. Write a Python program to count and display vowels in text.
# a= 'A quick Brown Fox Jumps over the Lazy Dog'
# for i in set(Counter(a).keys()):
#     if i in 'aeiouAEIOU': print(f'{i} is present in the sentence and Count of {i} is {Counter(a)[i]}')

# 50. Write a Python program to split a string on the last occurrence of the delimiter.
# print("100:23:345:0000".rsplit(':',1))

# 51. Write a Python program to find the first non-repeating character in a given string.
# a,flag,repeated_chr='abab',False,set()
# for i in range(len(a)):
#     if (a[i] not in a[i+1:]) and (a[i] not in repeated_chr) :
#         print(f'First Non repeating character is {a[i]}')
#         flag= True
#         break
#     else: repeated_chr.update(a[i])
# if flag == False : print('There\'s is no Non repeating character')

# 52. Write a Python program to print all permutations with a given repetition number of characters of a given string.
# tesr_str= 'Rama'
# print(list((permutations(tesr_str,4))))

# 53. Write a Python program to find the first repeated character in a given string.
# test_str='abcabded'
# print('first repeated character is ',tuple(test_str[i] for i in range(len(test_str)) if test_str[i] in test_str[i+1:])[0])

# 54. Write a Python program to find the first repeated character in a given string where the index of the first occurrence is smallest.
# test_str='xbcabded'
# firts_repeated_character = tuple(test_str[i] for i in range(len(test_str)) if test_str[i] in test_str[i+1:])[0]
# print('first repeated character is ', firts_repeated_character ,f'\nIndex ofd {firts_repeated_character} is {test_str.find(firts_repeated_character)}')

# 55.Write a Python program to find the first repeated word in a given string.
# test_str= 'Jay Shree Krishna Har Har Mahadev Jay Shree Ram'
# test_list = test_str.split()
# if len(test_list)<2:
#     print(f'The sentence has only one word {test_list[0]}')
# else:
#     print(tuple(test_list[i] for i in range(len(test_list)) if test_list[i] in test_list[i+1:])[0])

# using regex
# print(re.search(r'\b(\w+)\b.*\1',test_str).group().split()[0])

# 56. Write a Python program to find the second most repeated word in a given string.
# test_str= 'Jay Shree Krishna Har Har Mahadev Jay Shree Ram Jay Sitaram Jay Shree Gopal'
# print(Counter(test_str.split()).most_common(2)[-1])

# 57.Write a Python program to remove spaces from a given string.
# print('Jay Shree Krishna Har Har Mahadev Jay Shree Ram Jay Sitaram Jay Shree Gopal'.replace(' ',''))

# 58. Write a Python program to move spaces to the front of a given string.
# print(' Jay Shree Krishna Har Har Mahadev Jay Shree Ram Jay Sitaram Jay Shree Gopal            '.lstrip())

# 59. Write a Python program to find the maximum number of characters in a given string.
# print(Counter('Jay Shree Krishna Har Har Mahadev Jay Shree Ram Jay Sitaram Jay Shree Nandalaal').most_common())
# usual method
def ex_59(test_str='Jay Shree Krishna Har Har Mahadev Jay Shree Ram Jay Sitaram Jay Shree Nandalaal'):
    considered_chrs,stats=[],{}
    for i in range(len(test_str)):
        if test_str[i] not in considered_chrs:
            considered_chrs.append(test_str[i])
            stats[test_str[i]] = 1
            for j in range(i+1,len(test_str)):
                if test_str[i] == test_str[j]:
                    stats[test_str[i]] += 1
    print(sorted(stats.items(),key=lambda x: x[1], reverse=True)[0])

# ex_59()

# 60. Write a Python program to capitalize the first and last letters of each word in a given string.
# test_str= 'jay shree krishna har har mahadev jay shree ram jay sitaram jay shree nandalal.'
# test_list,new_list = test_str.split(),[]
# for word in test_list:
#     if len(word) == 1: word = word.upper()
#     else: word = word[0].upper() + word[1:-1] + word[-1].upper()
#     new_list.append(word)
# print(' '.join(new_list))

# 61. Write a Python program to remove duplicate characters from a given string.
# test_str,new_str='python exercises practice solution',''
# a= ''.join(collections.OrderedDict.fromkeys(test_str).keys())
# print(a)
#
# # to remove all duplicate characters
# duplicate_chrs=''.join([x[0] for x in list(filter(lambda x:x[1]>1,list(Counter(test_str).items())))])
# for chr in duplicate_chrs:
#     test_str = test_str.replace(chr,'')
# print( test_str)

# 62. Write a Python program to compute the sum of the digits in a given string.
# test_str,sum='Jay 123Shree321 Kr56ish0n7a',0
# for chr in test_str:
#     if chr.isdigit():
#         sum += int(chr)
# print(sum)

# 63. Write a Python program to remove leading zeros from an IP address
# test_str='002:123:01:030'
# print(':'.join([str(int(x)) for x in test_str.split(':')]))

# 64. Write a Python program to find the maximum length of consecutive 0's in a given binary string.
# test_str,max_len='111000010000011000000',0
# for i in range(len(test_str)):
#     if test_str[i] =='0':
#         length = 1
#         for j in range(i+1,len(test_str)):
#             if test_str[i]==test_str[j]:
#                 length += 1
#                 i=j
#             else : length = 0
#             if length>max_len: max_len=length
# print(max_len)
# # another method
# print(max(list(map(lambda x:len(x) ,test_str.split('1')))))
#
# #another method
# print(len(max(re.findall(r'0+',test_str))))

# 65. Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no similar letters print "No common characters".
# str1,str2,commonletter_list='asdf','qwe',''
# for chr in str1:
#     if chr in str2:
#         commonletter_list+=chr
# print(sorted(list(set(commonletter_list)),reverse=True) if len(commonletter_list)>0 else 'No Common Words')

# 67. Write a Python program to remove all consecutive duplicates of a given string.
# test_str,new_str = 'aabczzzddddddaaaefgxxxxxyyyz',''
# for x in list(itertools.groupby(test_str)):
#     new_str+=x[0]
# print(new_str)


# 68. Write a Python program to generate two strings from a given string. For the first string, use the characters that occur only once, and for the second, use the characters that occur multiple times in the said string.
# test_str = 'aabbcceffgh'
# print(''.join([x for x,y in list(Counter(test_str).items()) if y>1]))
# print(''.join([x for x,y in list(Counter(test_str).items()) if y==1]))


# 70. Write a Python program that concatenates uncommon characters from two strings.
# str1,str2,result = 'abcdpqr','xyzabcd',''
# for chr in str1:
#     if chr not in str2:
#         result+=chr
# for chr in str2:
#     if chr not in str1:
#         result+=chr
# print(result)

# another method
# str1,str2,result = 'abcdpqmrs','xyzabcdmt',''
# str1=set(str1)
# str2=set(str2)
# result=str1.symmetric_difference(str2)
# print(''.join(result))


# 71. Write a Python program to move all spaces to the front of a given string in a single traversal.
# test_str= 'Jay Shree Ram Jay Shree Krishna'
# print(' ' * test_str.count(" ") + ''.join(test_str.split()))

# 72. Write a Python program to remove all characters except a specified character from a given string.
# test_str,remove_str='Python Exercises Practice','Z'
# if remove_str in list(Counter(test_str).elements()): print(remove_str * list(Counter(test_str).elements()).count(remove_str))
# else:print(f'{test_str}')

# 73. Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.
# test_str ='@W3Resource.Com'
# print(f'Number of uppercase Characters: {len([x for x  in test_str if x in string.ascii_uppercase])}')
# print(f'Number of lowercase Characters: {len([x for x  in test_str if x in string.ascii_lowercase])}')
# print(f'Number of digit Characters: {len([x for x  in test_str if x in string.digits])}')
# print(f'Number of special Characters: {len([x for x  in test_str if x in string.punctuation])}')


# 74. Write a Python program to find the minimum window in a given string that will contain all the characters of another given string.
# str1,str2,flag_match,substrings_list='PRWSOERIUSFK ','OSU',True,[]
# for i in range(len(str1)):
#     for j in range(i,len(str1)):
#         flag_match = True
#         for k in str2:
#             if k not in str1[i:j+1]:
#                 flag_match = False
#         if flag_match == True:
#             substrings_list.append(str1[i:j+1])
#
# print(min(substrings_list,key=len))
# print(sorted(substrings_list,key=len)[0])


# 75. Write a Python program to find the smallest window that contains all characters in a given string.
# test_str,flag_match,valid_substrings='addbbad',True,[]
#
# for i in range(len(test_str)):
#     for j in range(i,len(test_str)):
#         flag_match=True
#         for k in set(test_str):
#             if k not in test_str[i:j+1]:
#                 flag_match= False
#                 break
#         if flag_match==True:
#             valid_substrings.append(test_str[i:j+1])
#
# print(valid_substrings)
# print(sorted(valid_substrings,key=len)[0])


# 76. Write a Python program to count the number of substrings from a given string of lowercase alphabets with exactly k
# distinct (given) characters.

# test_str,flag_match,substring_list = 'OmNamoBhagwateBasudevaya',True,[]
# no_of_distinct_chr = int(input('Please provide the number of unique characters : '))
# if no_of_distinct_chr > len(set(test_str)):
#     print(f'{test_str} doesn\'t have {no_of_distinct_chr} unique characters. ')
# else:
#     for i in range(len(test_str)):
#         for j in range(i,len(test_str)):
#             flag_match = True
#             if len(test_str[i:j+1])>=no_of_distinct_chr:
#                 matchcount = 0
#                 for k in test_str[i:j+1]:
#                     if k not in set(test_str):
#                         flag_match = False
#                         break
#                 if flag_match == True and len(set(test_str[i:j+1]))>= no_of_distinct_chr:
#                     substring_list.append(test_str[i:j+1])
#     print(f'answer is :- {substring_list}')


# 77. Write a Python program to count the number of non-empty substrings of a given string.
# test_str = 'Jay'
# print(int((len(test_str) * (len(test_str)+1)/2)))


# 78. Write a Python program to count characters at the same position in a given string (lower and uppercase characters) as in the English alphabet

# test_str,match_count,chr_dict = 'AbCd123h#isdfegpzrStUavWx.Z',0,{}
# for i in range(len(test_str)):
#     if 64<ord(test_str[i])<91:
#         position = ord(test_str[i]) - 65
#     elif 96<ord(test_str[i])<123:
#         position = ord(test_str[i]) - 97
#
#     if position == i :
#         match_count +=1
#         chr_dict[test_str[i]]= i+1
# print(f'No of characters at the same position is {match_count} \nCharacters with their position is {chr_dict}')


# 79. Write a Python program to find the smallest and largest words in a given string.
# test_str = 'Om Namo Bhagwate Basudevaya. Jay Shree Krishna. Ab'
# test_list = sorted(test_str.split(),key=len)
# print(f'smallest word is- {test_list[0]} , largest word is- {test_list[-1]}')
# print(test_list)


# 80. Write a Python program to count the number of substrings with the same first and last characters in a given string.
# test_str,substring_list= 'achyutamkeshavamkrishnadamodaram',[]
# for i in range(len(test_str)):
#     for j in range(i,len(test_str)):
#         if test_str[i:j+1][0] ==test_str[i:j+1][-1]:
#             substring_list.append(test_str[i:j+1])
# print(len(substring_list))


# 81. Write a Python program to determine the index of a given string at which a certain substring starts. If the substring is not found in the given string return 'Not found'.
# test_str='Om Nami Bhagwate Basudevaya'
# substr = 'Basudev'
# print(test_str.find(substr) if test_str.find(substr)>-1 else 'Not Found')


# 82. Write a Python program to wrap a given string into a paragraph with a given width.
# str = 'The quick brown fox jumps over a lazy dog'
# print(textwrap.fill(str,10))


# 83. Write a Python program to print four integer values - decimal, octal, hexadecimal (capitalized), binary - in a single line.
# strinput = 25
# print(f'decimal:{float(strinput)} , Octal:{oct(strinput)} , hexadecimal:{hex(strinput)} , binary:{bin(strinput)}')

# 84. Write a Python program to swap cases in a given string.
# print('hAR hAR mAHADEV'.swapcase())


# 85. Write a Python program to convert a given Bytearray to a Hexadecimal string.
# a=[111, 12, 45, 67, 109]
# print(''.join([hex(i)[2:] for i in a]))


# 86. Write a Python program to delete all occurrences of a specified character in a given string.
# test_str,chr = 'The man who sold the world','o'
# print(test_str.replace(chr,'') if chr in test_str else f'The character {chr} is not present in "{test_str}"')


# 87. Write a Python program to find the common values that appear in two given strings.
# str1,str2,strlist,new_list = 'RRR' , 'RRRRa',[],[]
# if len(str1) < len(str2) :
#     str1,str2 = str2, str1
# for i in range(len(str1)):
#     for j in range(i,len(str1)):
#         if (str1[i:j+1] in str2) and (str1[i:j+1] not in strlist):
#             strlist.append(str1[i:j + 1])
#
# for i in range(len(strlist)):
#     flag = True
#     for j in range(i):
#         if strlist[i] in strlist[j]:
#             flag= False
#     for k in range(i+1,len(strlist)):
#         if strlist[i] in strlist[k]:
#             flag = False
#     if flag == True:
#         new_list.append(strlist[i])
# print(strlist)
# print(new_list)


# 88. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.
# test_str = 'Har Har Mahadev 1008'
# print( 'There\'s a uppercase letter in the String'  if any(ch.isupper() for ch in test_str) ==True else 'Invalid String. There\'s not any capital letter in the String')
# print( 'There\'s a lowercase letter in the String'  if any(ch.islower() for ch in test_str) ==True else 'Invalid String. There\'s not any lower letter in the String')
# print( 'There\'s a digit in the String'  if any(ch.isdigit() for ch in test_str) ==True else 'Invalid String. There\'s not any digit letter in the String')
# print( 'String Validation Passed'  if len(test_str)>=3 else 'Invalid String. Letgth is less than 3')


# 89. Write a Python program to remove unwanted characters from a given string.
# test_str,new_str = 'Pyth*^on Exercis^es',''
# for ch in test_str:
#     if ch not in string.punctuation:
#         new_str += ch
# print(new_str)


# 90. Write a Python program to remove duplicate words from a given string.
# test_list='Python Exercises Practice Solution Exercises'.split()
# print(' '.join([i for i,j in list(Counter(test_list).items()) if j==1]))


# 91. Write a Python program to convert a given heterogeneous list of scalars into a string.
# test_list,test_str = ['Red', 100, -50, 'green', 'w,3,r', 12.12, False],''
# for item in test_list:
#     test_str += str(item) + ','
# print(test_str[:-1])


# 92. Write a Python program to find string similarity between two given strings.
#
# str1,str2,diff_count='Krishna','ram',0
# print(difflib.SequenceMatcher(None,str1.lower(),str2.lower()).ratio())
#
# difference_list = list(difflib.ndiff(str1,str2))
# for i in difference_list:
#     if i.startswith('-'):
#         diff_count+=1
# print(1-(diff_count/len(difference_list)))


# 93. Write a Python program to extract numbers from a given string.
# print(re.findall(r'\d+','red 12 black 45 green1234'))

# 94. Write a Python program to convert a hexadecimal color code to a tuple of integers corresponding to its RGB components.
# hexcode = 'FFA501'
# print([int(hexcode[i:i+2],16) for i in range(0,len(hexcode),2)])


# 95. Write a Python program to convert the values of RGB components to a hexadecimal color code.
# rgb = (255, 255, 105)
# print(''.join([hex(i)[2:].upper() for i in rgb]))


# 96. Write a Python program to convert a given string to Camelcase.
# test_str = '---+$@Jay shree -RAm'
# print(re.sub(r'\W','',test_str.title())[0].lower() + re.sub(r'\W','',test_str.title())[1:])


# 97. Write a Python program to convert a given string to Snake case.
# test_str = '---+$@jay shree -RAm'
# camelcase= re.sub(r'\W','',test_str.title())[0].lower() + re.sub(r'\W','',test_str.title())[1:]
# print(re.sub(r'([a-z])([A-Z])',r'\1_\2',camelcase).lower())


# 98. Write a Python program to decapitalize the first letter of a given string.
# test_str = 'Python 3.x'
# print(test_str[0].lower() + test_str[1:])


# 99. Write a Python program to split a multi-line string into a list of lines.
# test_str='''I am the man who walks alone.
# When i'm walking a dark Road.
# A little anxious when it's dark.
# Fear of the dark'''
# print(test_str.split('\n'))


# 100. Write a Python program to check whether any word in a given string contains duplicate characters or not.
# test_str,duplicate_flag = 'Sri Ram.',False
# for word in test_str.split():
#     print(Counter(word))
#     for x,y in Counter(word).items():
#         if y>1:
#             duplicate_flag=True
#             break
# print('String contains word which has duplicate characters' if duplicate_flag==True else 'String does not contains word which has duplicate characters')