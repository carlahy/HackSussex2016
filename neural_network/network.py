from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import pickle

def sentenceToVector(sentence, dictionary):
  words = set(sentence.split())
  result = []
  for word in dictionary:
    if word in words:
      result.append(1)
    else:
      result.append(0)
  return result

def getOutput(net, input_data):
  return net.activate(input_data)

emojis = ['happy', 'sad', 'love', 'tired', 'surprised']
def emojiToVector(emoji):
  result = [0] * len(emojis)
  result[emojis.index(emoji)] = 1
  return result
  

def buildTrainingDataSet(inputSize, outputSize, dictionary):
  ds = SupervisedDataSet(inputSize, outputSize)
  with open('training_data/training_set.txt') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 2):
      print(i)
      sentence = lines[i][:-1]
      emoji = lines[i+1][:-1]
      senVec = sentenceToVector(sentence, dictionary)
      emoVec = emojiToVector(emoji)
      ds.addSample(senVec, emoVec)
  return ds


dictionary = []
with open('dict.txt') as f:
  for word in f.readlines():
    dictionary.append(word[:-1])

layers = [43137, 1000, 5]
net = buildNetwork(*layers, bias=True)
ds = buildTrainingDataSet(len(dictionary), len(emojis), dictionary)
trainer = BackpropTrainer(net, ds)
print("before")
trainer.train()
print("after")
with open("net.p", "wb") as f:
  pickle.dump(net, f)
with open("tra.p", "wb") as f:
  pickle.dump(trainer, f)
