smiley = "\U0001f600"

nums = range(1, 11)

for num in nums:
  print(smiley * num)

num = 0
while num < 11:
  num += 1
  print(smiley * num)

for num in nums: 
  count = 0 
  smileys = ""
  while count <= num:
    smileys += smiley 
    count += 1
    print(smileys)