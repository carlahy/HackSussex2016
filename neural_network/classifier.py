from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import pickle

emojis = ['happy', 'sad', 'love', 'tired', 'surprised']
unicode_vals = [0x1F600, 0x1F61E, 0x2764, 0x1F629, 0x1F62F]

def getOutput(net, input_data):
  return net.activate(input_data)

def sentenceToVector(sentence, dictionary):
  words = set(sentence.split())
  result = []
  for word in dictionary:
    if word in words:
      result.append(1)
    else:
      result.append(0)
  return result


stopwords = set()
with open('training_data/stopwords.txt') as f:
  for word in f.readlines():
    stopwords.add(word[:-1])

dictionary = []
with open('training_data/training_set.txt') as f:
  S = set()
  for line in f.readlines():
    line = line[:-1]
    for word in line.split():
      S.add(word)
  S = S - stopwords
  dictionary = sorted(list(S))


net = None
with open("net.p", "rb") as f:
  net = pickle.load(f)

while True:
  sentence = input().lower()
  res = getOutput(net, sentenceToVector(sentence, dictionary)).tolist()
  i = res.index(max(res))
  print(sentence + "  " + str(chr(unicode_vals[i])))
