#str1 = "anagram"
#str2 = "manarag"
if str1
def is_anagram(str1, str2):
list1 = list(str1)
list1.sort()
list2 = list(str2)
list2.sort()

return (list1 == list2)

print(is_anagram('anagram' , 'manarag' ))
print(is_anagram('cat' , 'hat '))

