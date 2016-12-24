# Sentiment Analysis using Twitter Data in Python #

* **Installation**
* **Theory**

## Installation ##

* Clone the repository into the local repository
* we will need python and the following modules for installtion:-

  1. nltk

  2. sklearn

  3. ggplotter

  4. statistics 

* we can install the above modules using pip commands onto the system
* we will have to create a twitter app in order to stream in data from twitter.Thus the following steps will have to be followed for collecting data from twitter:-

1. After you sign in, you’ll be taken to your application creation page. Be sure to fill in your application’s name, a description about your application and a placeholder for the website field in correct format. Leave the callback url field blank. This tells your app to return to this location after authenticating.

2. Read and agree to Twitter’s “Developer Rules Of The Road”. Check the box next to “Yes, I agree”.

3. In the space below, enter the characters you see in the CAPTCHA and click on the “Create your Twitter application” button.

4. Doing this will take you to your Twitter app’s detail page. Under the OAuth settings, you’ll see that your app’s Access level is set to “Read-only” by default. To enable members to post to Twitter, click on the Settings tab at the top to change the Access level from “Read-only” to “Read and Write”.  Also check the box next to where it reads, “Allow this application to be used to Sign In with Twitter.”

5. Create the access tokens to provide access to your app to retrieve data from twitter.

6. copy the **access_token,access_secret,consumer_key,consumer_secret key** in the **twitter_sentiment_analysis.py** file

7. run the **creating_better_dataset.py** file to create and train the classifiers.

8. **creating_better_dataset.py** file builds and pickles the **classifiers** and the **dataset**.

* Now we run the **twitter_sentiment_analysis.py** file , we can track queries for any topic by setting up the **track** variable in the file.

* Now running the **graph_plotter.py** file would display the live sentiments on the graph by plotting on it.

##Working##

Python provide us with nltk module which can be used for Natural Language Processing.Python has a set of tools which can be used to collect data, build the classifiers, label the sentiment of a document and finally plot it on the graph to show the sentiments on a visual basis. This python reuces a huge amount of workload needed to build a sentiment classifier.


In the above project the classifer used is a voted_classifier which is the combination of five classifiers.The classification of a text,document is done on the basis of confidence level of the classification done by the classifier.
Thus the classification is done on the basis of majority of kind of votes a text/document gets .The higher no of votes of a particular type a document gets it is assigned the same label.
 

The classifiers used for voted classifer are naive_bayes,logisticRegression_clasifier,BernoulliNB_clasifier,MNB_classifier,SGD_classifier and SVC_classifier.

