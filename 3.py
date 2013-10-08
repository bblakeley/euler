# Problem 3
# http://projecteuler.net/problem=3

import math

n = int(raw_input("Enter a number: "))

def getFactors(n):
  max = n
  i = 2
  factors = []
  while i < max:
    if n % i == 0:
      factors.append(i)
    max = math.floor(n / i)
    i += 1
  if n % i == 0:
    factors.append(i)
  return factors

def filterPrimes(list):
  primes = []
  for i in list:
    if getFactors(i) == []:
      primes.append(i)
  return primes

print max(filterPrimes(getFactors(n)))