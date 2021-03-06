import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn import metrics
import numpy as np
import joblib
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.cm import rainbow
from sklearn.metrics import classification_report
from PIL import Image,ImageDraw
#from sklearn.naive_bayes import GaussianNB

#from sklearn.linear_model import LogisticRegression


##Step1: Load Dataset
class ui_random_forest_tarak(object):
    
  dataframe = pd.read_csv("csv/dataset.csv")
#print(dataframe.head())

#Step2: Split into training and test data
  x = dataframe.drop(["Label"],axis=1)
  y = dataframe["Label"]
  x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)
  s1=x_train
  s2=y_train
  s=x_test
##Step4: Build a model
    

#random forest
  print("Random forest results:\n")
  model = RandomForestClassifier(n_estimators=100,max_depth=5)
  model.fit(x_train,y_train)
  joblib.dump(model,"rf_malaria_100_5")

#visual data

  rf_scores = []
  estimators = [10, 100, 200, 500, 1000]
  for i in estimators:
        rf_classifier = RandomForestClassifier(n_estimators = i, random_state = 0)
        rf_classifier.fit(x_train, y_train)
        rf_scores.append(round(rf_classifier.score(x_test, y_test),7))
  colors = rainbow(np.linspace(0, 1, len(estimators)))
  plt.bar([i for i in range(len(estimators))], rf_scores, color = colors, width =1)
  for i in range(len(estimators)):
        plt.text(i, rf_scores[i], rf_scores[i])
#plt.xticks(ticks = [i for i in range(len(estimators))], labels = [str(estimator) for estimator in estimators])
  plt.legend()
#plt.xlabel('Number of estimators')
  plt.ylabel('Scores')
  plt.title('Random Forest Classifier scores for different number of estimators')
  plt.savefig('randomforest.png')
  plt.show()

##Step5: Make predictions and get classification report

  predictions = model.predict(x_test)

  s=classification_report(predictions,y_test)
  print(s)

  time=model.score(x_test,y_test)
  print(time)
  a=str(s)
  b='aacuray'+'     '+str(time)
  c=a+b
  img = Image.new('RGB', (400,200), color = (255, 255, 255))
 
  d = ImageDraw.Draw(img)
  d.text((10,10),c, fill=(0,0,0))
 
  img.save('randomreport.png')

