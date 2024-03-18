import sys
def sum(list):
  '''Given a list of numbers return the total sum'''
  sum = 0

  for num in list:
    sum += num

  return sum # Return sum to be compared with maxSum

def longestSum(nums):
  '''Given a list of numbers, will return the indices of largestSum left and right'''
  # Input assumes non-empty vector of n integers
  if len(nums) == 1: return nums[0] # Return number if list is size 1

  # Declaring essential variables for exhaustive search
  n = len(nums)
  maxSum = -sys.maxsize # Lowest possible int to compare for largest sum
  left, right = 0, 1 #Initial indices

  for i in range(n - 1):
    for j in range(i + 1, n):
      if sum(nums[i:j]) > maxSum: 
        # Sum of current list of strings is greater than previous maxSum
        maxSum = sum(nums[i:j])
        left, right = i, j

  return left, right # Return left and right indices of the list.

list = [] # Empyt list for user input

# Ask for user input to create a list one numbe at a time.
print("Hello user! Please input individual integers to add to your list..")

while(True):
  #Continue to add integers until user "quits"
  user_input = (input("Input(q to finish):"))
  if user_input == 'q': break
  list.append(int(user_input))
  
# Returns index of the longest sum in list
left, right = longestSum(list)

# Prints results of the algorithm
print("The longest sum is from index {0} to index {1} of the list.".format(left, right))
print("Result: {0}".format(list[left:right]))


print("\nTrying out sample inputs from txt file.\n")
input_list = []

with open('input.txt', 'r') as file:
  for line in file.readlines():
    input_list.append(line.rstrip('\n').split(","))
  for x in range(len(input_list)):
    for y in range(len(input_list[x])):
      input_list[x][y] = int(input_list[x][y])
    
    print("Testing this list:\n"
          "{0}".format(input_list[x]))
    # Returns index of the longest sum in list
    left, right = longestSum(input_list[x])

    # Prints results of the algorithm
    print("The longest sum is from index {0} to index {1} of the list.".format(left, right))
    print("Result: {0}\n".format(input_list[x][left:right]))
