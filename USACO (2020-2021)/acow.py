first = list(map(int, input().split()))
papers = first[0]
l = first[1]
cs = list(map(int, input().split()))

def hindex(cs):
  indices = []
  for i in range(len(cs)):
    curr = cs[i]
    result = filter(lambda x: x >= curr, cs)
    newRes = list(result)
    if cs[i] <= len(newRes):
        indices.append(curr)
  return max(indices)

def hlist(cs):
  indices = []
  for i in range(len(cs)):
    curr = cs[i]
    result = filter(lambda x: x >= curr, cs)
    newRes = list(result)
    if cs[i] <= len(newRes):
        indices.append(curr)
  x = sorted(indices, reverse = True)
  y = []
  for i in x:
    if i not in y:
        y.append(i)
  return y

if l == 0:
  print(hindex(cs))
else:
  if l >= papers:
    for i in cs:
      i += 1
    print(hindex(cs))
  else:
    c = l
    hl = hlist(cs)
    hlIndex = 0
    copy = cs.copy()
    while True:
      if c == 0:
        break
      else:
        copyTwo = copy.copy()
        copy[copy.index(hl[hlIndex])] += 1
        c -= 1
        newH = hindex(copy)
        if newH < hl[hlIndex]:
          if hlIndex != len(hl)-1:
            hlIndex +=  1
            copy = copyTwo.copy()
            c += 1
    print(hindex(copy))


