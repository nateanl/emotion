
# coding: utf-8

# In[17]:

from scipy.io import arff
import pandas
from sklearn import svm, metrics
from sklearn.model_selection import cross_val_predict
import numpy as np


# In[18]:

data, meta = arff.loadarff('emobase2010.arff')


# In[27]:

data.dtype.names


# In[4]:

data


# In[ ]:

df = pandas.DataFrame.from_records(adata)


# In[30]:

df.columns = data.dtype.names


# In[64]:

# remove neutral, unknown and other classes
a = df['class']!=b'NEU'
b = df['class']!=b'UNK'
c = df['class']!=b'OTH'
df = df.loc[a&b&c]


# In[65]:

df['class'].value_counts()


# In[66]:

adata = df.as_matrix()


# In[8]:

wclf = svm.SVC(kernel='linear', class_weight='balanced')


# In[ ]:

features, labels = np.split(adata, [-1], axis=1)
labels = [s for s in labels]


# In[87]:

np.unique(labels)


# In[81]:

predicted = cross_val_predict(wclf, features, labels)


# In[85]:

metrics.accuracy_score(labels, predicted)


# In[89]:

# rough baseline -- majority class
print(467/len(data), len(data)/len(np.unique(labels)))

