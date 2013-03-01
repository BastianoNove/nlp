from __future__ import division
from collections import defaultdict
from itertools import izip

def unigram(words):
  """returns a dict of unigram frequencies""" 
  freq = defaultdict(int) 
  for w in words:
    freq[w] += 1
  return freq 

def bigram(words):
  """returns a dict of bigram frequencies""" 
  freq = defaultdict(int)
  for (u,v) in izip(*(words[i:] for i in range(2))):
    freq[(u,v)] += 1
  return freq

def trigram(words):
  """returns a dict of trigram frequencies"""
  freq = defaultdict(int)
  for (u,v,w) in izip(*(words[i:] for i in range(3))):
    freq[(u,v,w)] += 1
  return freq

def unigram_mle(unigram_freq):
  """returns a dict of unigram maximum likelihood estimates.
     qml(w) = count(w) / count(all words) 
  """
  qml = defaultdict(int)
  numwords = sum(unigram_freq.itervalues())
  for w in unigram_freq.keys():
    qml[w] = unigram_freq[w]/numwords
  return qml

def bigram_mle(bigram_freq, unigram_freq):
  """returns a dict of bigram maximum likelihood estimates.
     qml(v|u) = count(v,w) / count(v) 
  """
  qml = defaultdict(int)
  for v,w in bigram_freq.keys():
    qml[(w,v)] = bigram_freq[(v,w)] / unigram_freq[v]
  return qml

def trigram_mle(trigram_freq, bigram_freq):
  """returns a dict of trigram maximum likelihood estimates.
     i.e., qml(w|u,v) = count(u,v,w) / count(u,v)
  """
  qml = defaultdict(int)
  for u,v,w in trigram_freq.keys():
    qml[(w,u,v)] = trigram_freq[(u,v,w)] / bigram_freq[(u,v)] 
  return qml 

def test():
  assert len(unigram('ski ba bop ba dop bop'.split())) == 4
  assert len(bigram('one one two three'.split())) == 3
  assert len(trigram('developers developers developers'.split())) == 1
  sentence = "hello world world this is is is".split()
  assert len(unigram_mle(unigram(sentence)))==4
  print "tests pass"

test()
