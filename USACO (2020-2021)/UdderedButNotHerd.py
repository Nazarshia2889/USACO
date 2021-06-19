cowphabet = list(input())
john = list(input())

count = [0] * len(john)

a = 0
x = 0
y = 0

while y < len(john):
  for j in range(len(cowphabet)):
    if john[x] == cowphabet[j]:
      count[a] += 1
      if x < len(john)-1:
        x += 1
      y += 1
  a += 1

result = 0

for i in count:
  if i > 0:
    result += 1

print(result)

