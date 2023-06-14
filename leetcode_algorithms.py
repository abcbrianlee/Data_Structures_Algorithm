# TWO SUMS
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#Example. input: nums = [2,7,11,15] and target =9
# Output: [0,1] because nums[0] + nums[1] =9

def twoSum(nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return[num_map[complement], i]
            else:
                num_map[num] = i
        return []
list = [15, 11, 7, 2]
print("Two Sums: ", twoSum(list, 9))

#Longest Substring without repeating characters
#Given a string (s), find and return the length of the longest substring without repeating characters.
#Input: s = "abcabcbb". Output = 3, because "abc" is the longest string that does not repeat characters.
def length_of_longest_substring(s):
    if not s:
        return 0
    max_length = 0
    start = 0
    char_map = {}
    for end in range(len(s)):
        if s[end] in char_map:
            start = max(start, char_map[s[end]] + 1)
        char_map[s[end]] = end
        max_length = max(max_length, end - start + 1)
    return max_length

string = "abcabcbb"
print("Length of longest substring: ", length_of_longest_substring(string))

#Valid Parenthesis
#Given a string (s) that contains either ( , ) ,{ , } ,[ and ], determine if input is valid or not.
#Input is valid if : open brackets must be closed by the same type of bracket. They must be closed in same order.
#s = [ '{, (, [ , {, } , ] , ), } '], is True. Even though there are nested brackets, they are closed in the same order.
#This uses a stack. When an opening bracket is entered, it is added to stack. When a closing bracket is added, it will pop the opening bracket that coorresponds with it. If it doesn't, returns False
def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping:
        #Checks if char is in key position. Not value position. Therefore, it checks if it is a closing bracket.
            if not stack or stack.pop() != mapping[char]:
                #Checks if the stack is empty or if top of stack (last opening bracket encountered) does not match the corresponding opening bracket for the current closing bracket.
                return False
        else:
            #If it is an opening bracket, gets pushed onto stack.
            stack.append(char)
    return not stack

string1 = ['[','{','(',')','}',']']
string2 = ['[','{','(',')',']','}']
print("String 1 is: ", is_valid(string1), "String 2 is : ", is_valid(string2))

#Return True if there is duplicates, return false if every item is unique.
#Ex. list1 = [1,2,3,4,5] is False and list2 = [1,2,3,4,5,1] is True.
def containsDuplicate(nums):
    my_dict = {}
    for num in nums:
        if num in my_dict:
            return True
        else:
            my_dict[num] = True
    return False

list1 = [1,2,3,4,5]
list2 = [1, 2, 3, 4, 5, 6, 2]

print("Does list 1 have duplicate?:", containsDuplicate(list1), "    Does list 2 have duplicate?:", containsDuplicate(list2))

#Maximize by choosing a single day and choosing a future day to sell stock
#Ex. input1 = [7,1,5,3,6,4], output = 5, because 6-1  = 5
#Ex input2 = [7, 6, 4, 2, 1], output = 0, because no profit can be made
def maxProfit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            #Sets min price if found
            min_price = price
        else:
            #finds the max profit by comparing to what current price - min price is.
            max_profit = max(max_profit, price - min_price)

    return max_profit
list1 = [ 7, 1, 5, 3, 6, 4]
print("Max profit is: ", maxProfit(list1))

#Longest Common Prefix, takes a list of strings and returns the longest common prefix of all the strings. If none, return ""
#Ex. Input = ["flower", "flow", "flight"]. Output = "fl.
#Ex.2 input=["dog", "racecar", "car"]. Output = ""

def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]  # Initialize prefix with the first string

    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            # The .find() will return the index of which the word is found. flow.find("fl) will return 0, escape.find("cape) will return 1, trtrtrt.find("ab") will retirn -1 bc it is not found
            # and pencil.find("cil") will return 2.
            # Since we are looking for prefixes, we only want returns where it is at 0 index.
            prefix = prefix[:-1]  # Remove last character from prefix
            if not prefix:# Will execute if statement once prefix is empty, meaning no match is made.
                return ""  # No common prefix found

    return prefix

list1 = ["flower", "floor", "flock"]
list2= ["Dog", "cat", "moose"]

print("Longest string prefix in list1:", longestCommonPrefix(list1), "Longest string prefix in list2:", longestCommonPrefix(list2))

#Given an integer x, return True if its reverse is the same (or a palindrome)
#Ex. input = 121. Output = True   Ex. input = 142. Output = False
#Slicing mechanism: 1st parameter starting(inclusive), 2nd parameter ending(exclusive) and third parameter is step. 2 = every other, -1= reverse, -2= reverse and every other

def isPalindrome(x):
    s = str(x)
    if s == s[::-1]:
        return True
    return False

int1 = 15551
int2 = 1240

print("Is Int1 a palindrome?:",isPalindrome(int1), "Is int2 a palindrome?:",isPalindrome(int2))

#Given two strings t and s, return True if they are anagrams or false is not
#An anagram is a word that can be rearranged to form another word.
def isAnagram(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    if sorted_s == sorted_t:
        return True
    else:
        return False
string1 = "anagram"
string2 = "nagaram"

string3 = "Laptop"
string4 = "Labtop"

print("Is first word an anagram?:",isAnagram(string1,string2),"Is second word an anagram?:", isAnagram(string3,string4))

#Remove duplicates from SORTED array
#Given integer array (nums) sorted in increasing order, remove duplicates in place so that each element is unique.Return the number of elements in nums
#Ex. input = [1,1,2]. Output: 2, nums=[1,2]
#ex. input = [0,0,1,1,1,2,2,3,3,4]. Output: 5, nums[0,1,2,3,4]

def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    k = 1  # Initialize unique elements count
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
        #If nums[i] is not equal to previous nums [i], meaning that we have a new unique integer
            nums[k] = nums[i]
            #We are setting the old repeating nums to the new unique nums
            k += 1
    return k

list1 = [1,1,2,2,3,3,4,4,5]
print("Output: ",removeDuplicates(list1))