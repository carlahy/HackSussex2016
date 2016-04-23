from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import pickle

emojis = ['happy', 'sad', 'love', 'tired', 'surprised']

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


dictionary = []
with open('training_data/training_set.txt') as f:
  S = set()
  for line in f.readlines():
    line = line[:-1]
    for word in line.split():
      S.add(word)
  dictionary = sorted(list(S))

net = None
with open("net.p", "rb") as f:
  net = pickle.load(f)

print("type your sentence")
sentence = input()
res = getOutput(net, sentenceToVector(sentence, dictionary))
print(res)