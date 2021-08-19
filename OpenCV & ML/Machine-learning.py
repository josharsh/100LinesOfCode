from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import scipy.sparse.linalg
from scipy.sparse import linalg
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width',
          'petal-length', 'petal-width',
          'class']
dataset = read_csv(url, names = names)


print(dataset.shape) 
print(dataset.head(25)) 
print(dataset.describe()) 
print(dataset.groupby('class').size()) 


dataset.plot(kind = "box", subplots = True,
             layout = (2,2), sharex = False,
             sharey = False)
pyplot.show() 

dataset.hist()
pyplot.show() 

scatter_matrix(dataset)
pyplot.show()

array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train,Y_validation = train_test_split(X, y, test_size=0.20, random_state = 1)

models = []
models.append(("LR", LogisticRegression(solver="liblinear",multi_class="ovr"))) 
models.append(('LDA', LinearDiscriminantAnalysis()))    
models.append(("KNN", KNeighborsClassifier()))           
models.append(("CART", DecisionTreeClassifier()))       
models.append(("NB", GaussianNB()))                      
models.append(("SVM", SVC(gamma="auto")))               

results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring = "accuracy")
    results.append(cv_results)
    names.append(name)
    print("%s: %f (%f)"%(name, cv_results.mean(),cv_results.std()))

pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()
    
model = SVC(gamma = "auto")
model.fit(X_train, Y_train)
prediction = model.predict(X_validation)

print(accuracy_score(Y_validation, prediction))
print(confusion_matrix(Y_validation, prediction))
print(classification_report(Y_validation, prediction))