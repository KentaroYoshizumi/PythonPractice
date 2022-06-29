def linearsearch(number_list, n):
  found = False
  for i in number_list:
      if i == n:
          found = True
          break
  return found


numbers = range(0, 100)
s1 = linearsearch(numbers, 100)
print(s1)
s2 = linearsearch(numbers, 202)
print(s2)
