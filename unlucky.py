nums = range(1, 21)

for num in nums:
  if num == 4 or num == 13: 
    state = "unlucky"
  elif num % 2 == 0:
    state = "even"
  else:
    state = "odd"
  print("{} is {}".format(num, state))
