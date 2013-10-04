# Problem 1
# http://projecteuler.net/problem=1

n = int(raw_input('n: '))

def three_five(n):
  multiples = []
  for i in range(1,n):
    if ((i % 3 == 0) or (i % 5 == 0)):
      multiples.append(i)
  return sum(multiples)

print three_five(n)