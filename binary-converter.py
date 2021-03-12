# Converts a number from base 10 to base 2
def bin_converter():
  n = int(input("Enter a #: "))
  
  # stores the original input for later
  og_n = n

  # initialized variables
  arr = []
  binary_num = ""

  # while n is positive, add the mod of n/2 to the front of a list which is the first digit in binary form. Then divide n by 2, repeating the process until the binary form is reached.
  while n > 0:
    mod = n % 2
    arr = [mod] + arr
    n = int(n/2)

  # Converts the array into a string, which is the binary form of n
  for i in arr:
    binary_num = binary_num + str(i)
  print("The binary form of", og_n, "is", binary_num)

  # The next part finds the greatest occurrence of consecutive 1's in the binary form and then prints the result. [ex. n = 11 -> 1011, '11' is the greatest occurrence so it prints 2]

  # basically making a copy of binary_num so that I can keep num as is while turning bin_string into a list in case I want to do anything else in the future.
  bin_string = str(binary_num) 
  # turns bin_string into a list split at 0 to identify the consecutive 1's
  bin_string = bin_string.split('0')
  # print(bin_string)
  max_len  = 0
  for seq in bin_string:
    if len(seq) > max_len:
      max_len = len(seq)
      longest = seq
  print("The greatest occurrence of consecutive 1's is", len(longest))



bin_converter()
