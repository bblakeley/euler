# Problem 2
# http://projecteuler.net/problem=2

n = 4000000
current = 0
next = 1
result = 0
while current <= n:
  if current % 2 == 0:
    result += current
  previous = current
  current = next
  next = current + previous
print result