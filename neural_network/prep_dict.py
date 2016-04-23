f = open('start_dict.txt', 'r')
words = f.readlines()
S = set()
for word in words:
  word = word[:-1]
  if not word[:-1] in S:
    S.add(word)
for word in sorted(list(S)):
  print(word)
