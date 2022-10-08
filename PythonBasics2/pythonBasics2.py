# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  # YOUR CODE HERE
  # Part A (count_threes) now needs to return the multiple of three that occurs the most in a string.
  # For ex, 0939639 would return 9 since it appeared 3 times while the other multiple of 3 appeared less than that.
  # You only need to worry about single digit multiples of 3 (3, 6, 9).
  # You must use a dictionary to accomplish this.
  # creating empty dictionary
  dict = {}
  # iterating through each number from example
  for i in n:
    # counter
    if i in dict:
      dict[i] += 1
    else:
      dict[i] = 1
  result = max(dict, key=dict.get)
  # return result
  return int(result)


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE
  # variables for the dictionary, count, and character
  dictionary = {}
  count = 0
  char = ''

  # iterate through the letters
  for i in s:
    if i == char:
      #if the character is the same, increase the count
      count += 1
      if dictionary.__contains__(i):
        # if the count is bigger than the index in the dictionary, set it to the count of the char
        if count > dictionary[i]:
          dictionary[i] = count
    else:
      # update the count
      count = 1
      dictionary.update({i: count})
      char = i
  # not sure where to go on but i did not know how to remove the dict_keys()
  return dictionary.keys()


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE
  # Set isPalindrome to bool value false
  isPalindrome = False
  # Lowercase everything
  s = s.lower()
  # Remove spaces from the string
  s = s.replace(" ", "")
  # Check if str is the same backward as forward
  # if yes then set palindrome to true
  if s[::-1] == s:
    isPalindrome = True
  # Return true or false
  return isPalindrome
