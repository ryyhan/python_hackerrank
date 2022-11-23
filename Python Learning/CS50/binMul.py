def binProd(binOne, binTwo):
  i = 0
  rem = 0
  sum = []
  bProd = 0
  while binOne != 0 or binTwo != 0:
    sum.insert(i, (((binOne % 10) + (binTwo % 10) + rem) % 2))
    rem = int(((binOne % 10) + (binTwo % 10) + rem) / 2)
    binOne = int(binOne/10)
    binTwo = int(binTwo/10)
    i = i+1
  if rem != 0:
    sum.insert(i, rem)
    i = i+1
  i = i-1
  while i >= 0:
    bProd = (bProd * 10) + sum[i]
    i = i-1
  return bProd

binMul = 0
factr = 1
print(end="Enter First Binary Number: ")
binOne = int(input())
print(end="Enter Second Binary Number: ")
binTwo = int(input())
while binTwo != 0:
  digit =  binTwo % 10
  if digit == 1:
    binOne = binOne * factr
    binMul = binProd(binOne, binMul)
  else:
    binOne = binOne * factr
  binTwo = int(binTwo/10)
  factr = 10
print("\nMultiplication Result = " +str(binMul))