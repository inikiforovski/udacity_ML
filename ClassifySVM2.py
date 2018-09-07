from sklearn.naive_bayes import GaussianNB
from sklearn import svm

def classifySVM(features_train, labels_train):

### import the sklearn module for GaussianNB
### create classifier
### fit the classifier on the training features and labels
### return the fit classifier


### your code goes here!

    clf2 = svm.SVC()
    return clf2.fit(features_train, labels_train)
    # return clf2.predict([[-0.8, -1]])
