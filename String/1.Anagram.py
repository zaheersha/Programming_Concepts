'''
Given two strings a and b consisting of lowercase characters. The task is to check
whether two given strings are an anagram of each other or not. An anagram of a
string is another string that contains the same characters, only the order of characters
can be different. For example, “act” and “tac” are an anagram of each other.

Input:
a = allergy, b = allergic
Output: NO
Explanation:Characters in both the strings
are not same, so they are not anagrams.

Step 1: Take an array of size 26, which will contain the count of characters of first string.
Step 2: Traverse through each character of first string and increment the count of character
in the array taken in step 1.
Step 3: Now, traverse the second string and decrement the count of characters in the same
array, taken in step 1.
Step 4: At last, just traverse the array and check if there is any value other than 0.
If it exists, this means there are some characters which are not in both the string.
This is because we have first incremented the count using first string and then
decremented the same for the second string.
Step 5: If any of the value is not equal to 0, return NO, else return YES.

'''



def isAnagram(a,b):

    mp={}
    for i in a:
        if i in mp.keys():
            mp[i]+=1
        else:
            mp[i]=1

    for i in b:
        if i not in mp.keys():
            return "NO"
        else:
            mp[i] -=1

    for i in mp.keys():
        if mp[i] !=0:
            return "NO"

    return "YES"

# print(isAnagram('martiny',"yrtinma"))







