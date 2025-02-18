import os
from colorama import Fore, Style
from random import choice

os.system('cls||clear')

def replacesl(inputlist, what, replacement):
  for i, item in enumerate(inputlist):
    if item == what:
      inputlist[i] = replacement
    elif type(item) == list:
      replacesl(item, what, replacement)
  return inputlist

colors,styles=[Fore.GREEN, Fore.BLUE, Fore.RED, Fore.CYAN, Fore.BLACK, Fore.YELLOW],[Style.BRIGHT, Style.NORMAL]
nums,num = [],1
length = 11

while len(nums)<length:
    nums.append([*range(0,num)])
    num += 1

for num in range(len(nums)):
    multiplier = 2
    while sum(len(str(i)) for i in nums[-1]) > sum(len(str(i)) for i in nums[num]):
        nums[num].append(" ")
    while len(nums[num]) > length:
        del nums[num][-2:]
        nums[num].append(" "*multiplier)
        multiplier += 1
    if sum(len(str(i)) for i in nums[-1]) > sum(len(str(i)) for i in nums[num]) or len(nums[num]) > length:continue


for each in nums[-1]:replacesl(nums, each, f"{choice(colors)}{choice(styles)}{each}{Fore.WHITE}")

for num in range(len(nums)):print(f"{' '.join([str(elem) for elem in nums[num]])} {' '.join([str(elem) for elem in nums[num][::-1]])}")

print(" ")
