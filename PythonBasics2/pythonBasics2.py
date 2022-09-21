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
  # Divide n by 3 and round down to get the number of multiples
  return int(n/3)


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE
  # Initialize the repeating character count
  repeatingCharacter = 0
  # Initialize the character to first the letter
  # of the string
  theCharacter = s[0]
  # Set length to lengthof string s
  length = len(s);
  # Loop for the length of the string
  for i in range(length):
    # Set the character count to 1
    currentCharacter = 1
    # Loop next char over and check if they're
    # The same if not breaks loop and goes to next char in str
    for j in range(i + 1, length):
      if (s[i] != s[j]):
        break
        # If the character match add to currentCharacter counter
      currentCharacter = currentCharacter + 1
      # If the current count is bigger than the
      # Previous count update it
    if currentCharacter > repeatingCharacter:
      repeatingCharacter = currentCharacter
      # Set the character to the largest consecutive character
      theCharacter = s[i]
  # Return the largest character
  return theCharacter


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE

  return
