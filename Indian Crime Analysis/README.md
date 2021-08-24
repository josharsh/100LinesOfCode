# Crime Analysis on Indian Crime Data

#### Owner: Navansh Goel
#### Linkedin: https://www.linkedin.com/in/navanshgoel/
Crime prediction and criminal identification are the major problems to the police department as there is a tremendous amount of crime data that exists. There is a need for technological developments through which case solving could be faster. 

The aim of this project is to make crime prediction using the features present in the dataset and then comparing the predicted data with the actual data. The dataset is extracted from the official sites.


# Objective

The objective would be to train a model for prediction. Building the model will be done using a better algorithm depending upon the accuracy. The K - Means Clustering Algorithm, Principal Component Analysis(PCA) and other algorithms will be used for crime prediction. Visualization of the dataset is done to analyze the crimes which may have occurred.
## Dataset
A large dataset of different types of crimes committed in various districts of Indian States from 2001 to 2012 is taken from Kaggle website. Further, selected data is chosen based on the largest characteristic details.

You can find the dataset at:
https://www.kaggle.com/rajanand/crime-in-india

### Note:
*This analysis by no means is a comparison to the real work done by the criminal check authorities of India. This work is just an approach to improve and enhance the interest and curiosity of technology driven individuals in the field of Data analytics for Crime Control.*

# How to run the code file

The python notebook with .ipynb extension can be run using google colaboratory platform or jupyter notebook. 
### Google Colaboratory
Refer the following link to import a python notebook in Google Colaboratory:
https://research.google.com/colaboratory/faq.html

### Jupyter Notebook
Refer the link below to install Jupyter notebook:
https://jupyter.org/install

Refer the link below to import the python notebook into the jupyter notebook environment:
https://jupyter-notebook.readthedocs.io/en/4.x/examples/Notebook/rstversions/Importing%20Notebooks.html 

## Alternative Solution
A python notebook (.py extension) can be opened using vscode. For this necessary libraries must be installed. 

Refer the link below:
https://code.visualstudio.com/docs/datascience/jupyter-notebooks

# Methods Used
## K-Means Clustering ++ 
K-Means Clustering is an Unsupervised Learning Algorithm that is used to solve the clustering problems in machine learning or data science.
The K - Means Clustering Algorithm mainly performs two tasks:

 - Determines the best value for K center points or centroids by an iterative process.
 - Assigns each data point to its closest k-center. Those data points which are near to the particular k-center, create a cluster

### Advantages of using the Algorithm:

 - Guarantees Convergence
 - Generalises to Clusters of different shapes and sizes
 - Relatively simple to implement
 - Scales to large data sets

 
## Principle Component Analysis

Principal Component Analysis, or PCA, is a dimensionality-reduction method that is often used to reduce the dimensionality of large data sets, by transforming a large set of variables into a smaller one that still contains most of the information in the large set.
Steps: 

 - Standardization
 - Covariance Matrix Computation
 - Computing the Eigen Vector and Eigen Values
 - Feature Vector
 - Recasting the Data Along the Principle component Axes

