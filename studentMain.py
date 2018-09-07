#!/usr/bin/python

""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.

    The objective of this exercise is to recreate the decision
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """

from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, output_image
from ClassifySVM2 import classifySVM
# from mysql.connector import connection
# import csv
import sys
from ClassifyNB import classify
from classifyDTC import classifyDTC

# import numpy as np
# import pylab as pl




# cnx = connection.MySQLConnection(user='admin', password='CEqNzCAUip99V?fsx',
#                                  host='127.0.0.1',
#                                  database='employees')
# cnx.close()



features_train, labels_train, features_test, labels_test = makeTerrainData()

# with open('testout.csv', 'rb') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     index = -1
#     for row in spamreader:
#         if (index>0):
#             features_train[index][0] = float(row[3])
#             features_train[index][1] = float(row[1])
#             labels_train[index] = float(row[2])
#         index += 1




### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]

# You will need to complete this function imported from the ClassifyNB script.
# Be sure to change to that code tab to complete this quiz.
#clf = classifySVM(features_train, labels_train)
clf = classifyDTC(features_train, labels_train)

### draw the decision boundary with the text points overlaid
prettyPicture(clf, features_test, labels_test, "testDTC.png")
output_image("testDTC.png", "png", open("testDTC.png", "rb").read())


# f = open('testout.csv', 'wt')
# try:
#     writer = csv.writer(f)
#     writer.writerow(('Grade', 'Bumpiness', 'Fast/Slow'))
#     for ii in range(0, len(features_train)):
#         writer.writerow((features_train[ii][0], features_train[ii][1], labels_train[ii]))
# finally:
#     f.close()

# print open(sys.argv[1], 'rt').read()




