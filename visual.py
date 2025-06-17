# visualizer.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:/Users/T.Haneesh/ml/churn-bigml-20.csv")
sns.boxplot(x='Churn', y='Customer service calls', data=df)
plt.title('Customer Service Calls vs Churn')
plt.xlabel('Churn')
plt.ylabel('Customer Service Calls')
plt.tight_layout()
plt.show()
