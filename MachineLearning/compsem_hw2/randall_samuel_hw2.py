###########
# Solution, homework 2
#
# Name and EID: Samuel Randall spr699
# Option chosen: A
###

## Problem 1

from gensim.models import Word2Vec 
from nltk.corpus import brown
from nltk.corpus import gutenberg

brownmodel1 = Word2Vec(brown.sents(), iter=1, min_count=10, size=100)
brownmodel2 = Word2Vec(brown.sents(), iter=1, min_count=10, size=200)
gutmodel1 = Word2Vec(gutenberg.sents(), iter=1, min_count=10, size=100)
gutmodel2 = Word2Vec(gutenberg.sents(), iter=1, min_count=10, size=200)

## Three words: Bright, Clear, Bank
print("brownmodel1 data: ")
print("bright: ",brownmodel1.wv.most_similar('bright', topn=10))
print("clear: ",brownmodel1.wv.most_similar('clear', topn=10))
print("bank: ",brownmodel1.wv.most_similar('bank', topn=10))

print("brownmodel2 data: ")
print("bright: ",brownmodel2.wv.most_similar('bright', topn=10))
print("clear: ",brownmodel2.wv.most_similar('clear', topn=10))
print("bank: ",brownmodel2.wv.most_similar('bank', topn=10))

print("gutmodel1 data: ")
print("bright: ",gutmodel1.wv.most_similar('bright', topn=10))
print("clear: ",gutmodel1.wv.most_similar('clear', topn=10))
print("bank: ",gutmodel1.wv.most_similar('bank', topn=10))

print("gutmodel2 data: ")
print("bright: ",gutmodel2.wv.most_similar('bright', topn=10))
print("clear: ",gutmodel2.wv.most_similar('clear', topn=10))
print("bank: ",gutmodel2.wv.most_similar('bank', topn=10))

# The difference from dimension size is rather small, but the difference
# between corpuses is significant. The brown corpus included more occurances
# for the definition of 'bank' that is the institution, whereas the gutenburg
# corpus refers to the geographic feature.

## Problem 2

from collections import Counter

def average(numberlist):
    return (sum(numberlist) / max(len(numberlist), 1))

tree_list = []
tree_list.append(gutmodel1.wv.similarity("tree", "mouse"))
tree_list.append(gutmodel1.wv.similarity("tree", "man"))
tree_list.append(gutmodel1.wv.similarity("tree", "paper"))

mouse_list = []
mouse_list.append(gutmodel1.wv.similarity("mouse", "tree"))
mouse_list.append(gutmodel1.wv.similarity("mouse", "man"))
mouse_list.append(gutmodel1.wv.similarity("mouse", "paper"))

man_list = []
man_list.append(gutmodel1.wv.similarity("man", "tree"))
man_list.append(gutmodel1.wv.similarity("man", "mouse"))
man_list.append(gutmodel1.wv.similarity("man", "paper"))

paper_list = []
paper_list.append(gutmodel1.wv.similarity("paper", "tree"))
paper_list.append(gutmodel1.wv.similarity("paper", "man"))
paper_list.append(gutmodel1.wv.similarity("paper", "mouse"))

avg = {}
avg["man"] = average(man_list)
avg["mouse"] = average(mouse_list)
avg["paper"] = average(paper_list)
avg["tree"] = average(tree_list)

counter = Counter(avg)
print(min(counter, key=counter.get))

## Problem 3

import pandas
filename = "/Users/samuelrandall/CompSem/compsem_hw2/BLESS.txt"
bless = pandas.read_csv(filename, sep="\s+")
print(bless)

# There are 26554 rows and 15 with attri relation

## Problem 4

def sim_or_zero(word1, word2, model):
    if word1 in model and word2 in model:
        return model.wv.similarity(word1, word2)
    else:
        return 0.0
            
bless["space1"] = [sim_or_zero(row["Word1"][:-2], row["Word2"][:-2], brownmodel1) for index, row in bless.iterrows()]
bless["space2"] = [sim_or_zero(row["Word1"][:-2], row["Word2"][:-2], brownmodel2) for index, row in bless.iterrows()]

print(bless)

## Problem 5

import scipy

b_attri = bless[bless.Relation == "attri"]
print("space1", end="\n\n")

print("attri:")
print("mean", b_attri.space1.mean())
print("median", b_attri.space1.median())
print("1st quartile", b_attri.space1.quantile(0.25)) 
print("3rd quartile", b_attri.space1.quantile(0.75), end="\n\n")

b_coord = bless[bless.Relation == "coord"]

print("coord:")
print("mean", b_coord.space1.mean())
print("median", b_coord.space1.median())
print("1st quartile", b_coord.space1.quantile(0.25)) 
print("3rd quartile", b_coord.space1.quantile(0.75), end="\n\n")

b_event = bless[bless.Relation == "event"]

print("event:")
print("mean", b_event.space1.mean())
print("median", b_event.space1.median())
print("1st quartile", b_event.space1.quantile(0.25)) 
print("3rd quartile", b_event.space1.quantile(0.75), end="\n\n")

b_mero = bless[bless.Relation == "mero"]

print("mero:")
print("mean", b_mero.space1.mean())
print("median", b_mero.space1.median())
print("1st quartile", b_mero.space1.quantile(0.25)) 
print("3rd quartile", b_mero.space1.quantile(0.75), end="\n\n")

# Space 2

print("space2", end="\n\n")

print("attri:")
print("mean", b_attri.space2.mean())
print("median", b_attri.space2.median())
print("1st quartile", b_attri.space2.quantile(0.25)) 
print("3rd quartile", b_attri.space2.quantile(0.75), end="\n\n")

print("coord:")
print("mean", b_coord.space2.mean())
print("median", b_coord.space2.median())
print("1st quartile", b_coord.space2.quantile(0.25)) 
print("3rd quartile", b_coord.space2.quantile(0.75), end="\n\n")

print("event:")
print("mean", b_event.space2.mean())
print("median", b_event.space2.median())
print("1st quartile", b_event.space2.quantile(0.25)) 
print("3rd quartile", b_event.space2.quantile(0.75), end="\n\n")


print("mero:")
print("mean", b_mero.space2.mean())
print("median", b_mero.space2.median())
print("1st quartile", b_mero.space2.quantile(0.25)) 
print("3rd quartile", b_mero.space2.quantile(0.75), end="\n\n")

# There does not appear to be any differences between the two spaces




