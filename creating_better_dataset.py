import nltk
import random
from nltk.corpus import movie_reviews
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC , LinearSVC , NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize,sent_tokenize
import codecs
import io

class VoteClassifier(ClassifierI):
   def __init__(self,*classifiers):
       self._classifiers=classifiers
 
   def classify(self,features):
       votes=[]
       for c in self._classifiers:
           v=c.classify(features)
           votes.append(v)
       return mode(votes)


   def confidence(self,features):
       votes=[]
       for c in self._classifiers:
           v=c.classify(features)
           votes.append(v)
       
       choice_votes=votes.count(mode(votes))
       conf=choice_votes/len(votes)
       return conf
     
#short_pos=codecs.open("positive_pp.txt","r").read()
#short_neg=codecs.open("negative_pp","r").read()

with io.open("positive.txt", "r", encoding="utf-8") as my_file:
     short_pos = my_file.read()

with io.open("negative.txt", "r", encoding="utf-8") as my_file:
     short_neg = my_file.read()

documents=[]
all_words=[]
#print short_pos[1]

#allowed_word_types=["J","R","V"]
allowed_word_types=["J"]

for r in short_pos.split('\n'): 
    documents.append((r,"pos")) 
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())
  
for r in short_neg.split('\n'): 
    documents.append((r,"neg")) 
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())



save_documents = open("pickled_algos/documents.pickle","wb")
pickle.dump(documents, save_documents)
save_documents.close()

#short_pos_words=word_tokenize(short_pos)
#short_neg_words=word_tokenize(short_neg)

#all_words=[]

#for w in short_pos_words:
#    all_words.append(w.lower())
#for w in short_neg_words:
#     all_words.append(w.lower())

all_words=nltk.FreqDist(all_words)


#print(all_words.most_common(15))
#print all_words


word_features=list(all_words.keys())[:3000]

save_word_features=open("pickled_algos/word_features.pickle","wb")
pickle.dump(word_features,save_word_features)
save_word_features.close()




def find_features(document):
    words=word_tokenize(document)
    features={}
    for w in word_features:
        features[w]=(w in words)

    return features



#print (find_features('/home/aman/Desktop/nlp/neg_movie_rev'))

feature_sets= [(find_features(rev),category) for (rev,category) in documents]

save_featurests=open("pickled_algos/featuresets.pickle","wb")
pickle.dump(feature_sets,save_featuresets)
save_featuresets.close()

#print (feature_sets[1])

random.shuffle(feature_sets)

training_set=feature_sets[:10000]

testing_set=feature_sets[10000:]


classifier= nltk.NaiveBayesClassifier.train(training_set)



save_classifier = open("pickled_algos/naivebayes.pickle","wb")
pickle.dump(classifier,save_classifier)
save_classifier.close()

##classifier_f=open("naivebayes2.pickle","rb")
##classifier=pickle.load(classifier_f)
##classifier_f.close()

print("naive bayes classify accuracy",(nltk.classify.accuracy(classifier,testing_set))*100)


classifier.show_most_informative_features(15)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

save_classifier=open("pickled_algos/MNB_classifier.pickle","wb")
pickle.dump(MNB_classifier,save_classifier)
save_classifier.close()


Bernoulli_classifier = SklearnClassifier(BernoulliNB())
Bernoulli_classifier.train(training_set)
print("Bernoulli_classifier accuracy percent:", (nltk.classify.accuracy(Bernoulli_classifier, testing_set))*100)

save_classifier=open("pickled_algos/BernoulliNB_classifier.pickle","wb")
pickle.dump(Bernoulli_classifier,save_classifier)
save_classifier.close()

lr_classifier = SklearnClassifier(LogisticRegression())
lr_classifier.train(training_set)
print("LOgistic_Regression_classifier accuracy percent:", (nltk.classify.accuracy(lr_classifier, testing_set))*100)

save_classifier=open("pickled_algos/lr_classifier.pickle","wb")
pickle.dump(lr_classifier,save_classifier)
save_classifier.close()

sgd_classifier = SklearnClassifier(SGDClassifier())
sgd_classifier.train(training_set)
print("sgd_classifier accuracy percent:", (nltk.classify.accuracy(sgd_classifier, testing_set))*100)

save_classifier=open("pickled_algos/sgd_classifier.pickle","wb")
pickle.dump(sgd_classifier,save_classifier)
save_classifier.close()

#classifier_list=[classifier, MNB_classifier,Bernoulli_classifier,lr_classifier,sgd_classifier]

voted_classifier=VoteClassifier(classifier, MNB_classifier,Bernoulli_classifier,lr_classifier,sgd_classifier)

#print("Classification:", voted_classifier.classify(testing_set[0][0]), "Confidence %:",voted_classifier.confidence(testing_set[0][0])*100)

#print("Classification:", voted_classifier.classify(testing_set[1][0]), "Confidence %:",voted_classifier.confidence(testing_set[1][0])*100)

#print("Classification:", voted_classifier.classify(testing_set[2][0]), "Confidence %:",voted_classifier.confidence(testing_set[2][0])*100)

#print("Classification:", voted_classifier.classify(testing_set[3][0]), "Confidence %:",voted_classifier.confidence(testing_set[3][0])*100)

#print("voted classifier accuracy:",(nltk.classify.accuracy(voted_classifier,testing_set))*100)





