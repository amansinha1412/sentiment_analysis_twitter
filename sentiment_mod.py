import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC,LinearSVC,NuSVC
from statistics import mode
from nltk.tokenize import word_tokenize
from nltk.classify import ClassifierI

class VoteClassifier:
   def __init__(self,*classifiers):
          self._classifiers=classifiers
       
   def classify(self,features):
       votes=[]
       for c in self._classifiers:
           v = c.classify(features)
           votes.append(v)
      
       return mode(votes)

   def confidence(self,features):
       votes=[]
       for c in self._classifiers:
           v = c.classify(features)
           votes.append(v)
   
       choice_votes=votes.count(mode(votes))
       conf=choice_votes / len(votes)
       return votes


documents_f=open("pickled_algos/documents.pickle","rb")
documents=pickle.load(documents_f)
documents_f.close()

random.shuffle(documents)

word_features_f=open("pickled_algos/word_features.pickle","rb")
word_features=pickle.load(word_features_f)
word_features_f.close()


def find_features(document): 
    words=word_tokenize(document)
    features={}
    for w in word_features:
        features[w]=(w in words)
    
    return features

#featuresets_f=open("pickled_algos/featuresets.pickle","rb")
#featuresets = pickle.load(featuresets_f)
#featuresets_f.close()

featuresets= [(find_features(rev),category) for (rev,category) in documents]

random.shuffle(featuresets)
print(len(featuresets))


training_set=featuresets[3000:]
testing_set=featuresets[:3000]
#naivebayes,BernoulliNB_classifier,lr_classifier,MNB_classifier,BernoulliNB_classifier,sgd_classifier

open_file=open("pickled_algos/naivebayes.pickle","rb")
classifier=pickle.load(open_file)
open_file.close()

open_file=open("pickled_algos/BernoulliNB_classifier.pickle","rb")
BernoulliNB_classifier=pickle.load(open_file)
open_file.close()

open_file=open("pickled_algos/lr_classifier.pickle","rb")
lr_classifier=pickle.load(open_file)
open_file.close()

open_file=open("pickled_algos/MNB_classifier.pickle","rb")
MNB_classifier=pickle.load(open_file)
open_file.close()

open_file=open("pickled_algos/sgd_classifier.pickle","rb")
sgd_classifier=pickle.load(open_file)
open_file.close()
      
voted_classifier=VoteClassifier(classifier,BernoulliNB_classifier,lr_classifier,MNB_classifier,sgd_classifier)

def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)
