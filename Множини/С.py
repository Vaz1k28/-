def text(list1, list2):

  result = []
  hashset = set(list1)
  for x in list2:
    if x in hashset:
      result.append(x)
  return result


list1 = [1, 2, 3]
list2 = [4, 3, 2]
text_result = text(list2, list1)
print(text_result)
