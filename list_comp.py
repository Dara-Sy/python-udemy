names = ["Ellie", "Tim", "Matt"]
answer = [name[0] for name in names]
print(answer)

# this solution didn't work

# nums = [1,2,3,4,5,6]
# answer2 = [nums.append(x) if x % 2 == 0 else nums.remove(x) for x in nums]

# what does work
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
print(answer2)


# this solution didn't work
# first = [1,2,3,4] 
# second = [3,4,5,6]
# answer = [x for x in first + second if x in first or if x in second]
# print(answer)

# what does work
answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]


nums = list(range(1,101))
answer =  [x for x in nums if x % 12 == 0]

split(x for x in 'amazing' if x in ['a', 'e', 'i', 'o', 'u'])

# answer = [x for x in range(len('amazing')) if x is not in ['a', 'e', 'i', 'o', 'u']]
# answer = split(x for x in 'amazing' if x in ['a', 'e', 'i', 'o', 'u'])

answer = [char for char in "amazing" if char not in "aeiou"] 

# Using a list:

answer = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]] 