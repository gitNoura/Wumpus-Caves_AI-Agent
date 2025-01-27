import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.metrics import accuracy_score, precision_score
 
#Create the NumPy array for actual and expected labels.
expected    = np.array(
  ['Success','Success','Success','Success','Success','Success','Success','Success','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Success','Success','Success','Success','Success','Success','Success','Success','Success','Success','Success','Success','Success','Success','Success'])
actual = np.array(
  ['Success','Success','Success','Success','Success','Success','Success','Success','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure','Failure'])
 
#compute the confusion matrix.
cm = confusion_matrix(actual,expected)
 
#Plot the confusion matrix.
sns.heatmap(cm, 
            annot=True,
            fmt='g', 
            xticklabels=['Success','Failure'],
            yticklabels=['Success','Failure'])
plt.ylabel('Expected',fontsize=13)
plt.xlabel('The Agent',fontsize=13)
plt.title('Confusion Matrix',fontsize=17)
plt.show()


accuracy = accuracy_score(actual, expected)
print("Accuracy   :", accuracy)
precision = precision_score(actual, expected, pos_label='Failure')
print("Precision :", precision)