zodiac = ["Ox", "Tiger", "Rabbit", 
"Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]
arr = []
results = []
n = 0

for i in range(int(input())):
  s = input().split()
  arr.append(s)
be = "Ox"
r = "Ox"
l = 0
for i in range(len(arr)):
  yearA = arr[l][4]
  t = arr[l][3]
  a = arr[l][0]
  b = arr[l][-1]
  count = 0
  if t == 'previous':
    if b == 'Bessie':
      index = zodiac.index('Ox')
      if index-1 <= -1:
        index = 11
      else:
        index -= 1
    else:
      index = zodiac.index(r)
      if index-1 <= -1:
        index = 11
      else:
        index -= 1
    while zodiac[index] != yearA:
      if index-1 <= -1:
        index = 11
        count += 1
      else:
        index -= 1
        count += 1
    x = []
    x.append(a)
    x.append(b)
    x.append(count)
    results.append(x)
  else:
    if b == 'Bessie':
      index = zodiac.index('Ox')
      if index+1 >= 12:
        index = 0
      else:
        index += 1
    else:
      index = zodiac.index(r)
      if index+1 >= 12:
        index = 0
      else:
        index += 1
    while zodiac[index] != yearA:
      if index+1 >= 12:
        index = 0
        count += 1
      else:
        index += 1
        count += 1
    x = []
    x.append(b)
    x.append(a)
    x.append(count)
    results.append(x)
  l += 1
  r = yearA

yearCounter = 0
new = 'Bessie'
for i in range(len(results)):
  if i+1 < len(results) and i != len(results)-1:
    if results[i+1][1] != 'Bessie':
      if results[i][1] == new:
        yearCounter -= results[i][2]
      elif results[i][0] == new:
        yearCounter += results[i][2]
      if results[i][1] == 'Elsie' or results[i][0] == 'Elsie':
        break
      new = results[i][0]
    else:
      if results[i][0] == 'Elsie' or results[i][1] == 'Elsie':
        if results[i][1] == new:
          yearCounter -= results[i][2]
        elif results[i][0] == new:
          yearCounter += results[i][2]
        if results[i][1] == 'Elsie' or results[i][0] == 'Elsie':
          break
        new = results[i][0]
      else:
        yearCounter = 0
        new = 'Bessie'
  else:
    if results[i][1] == new:
      yearCounter -= results[i][2]
    elif results[i][0] == new:
      yearCounter += results[i][2]
    

print(abs(yearCounter))
