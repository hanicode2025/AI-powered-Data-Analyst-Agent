import pandas as pd
from data_loader import load_data
from llama_interface import ask_llama_from_df
from visual import plot_churn_boxplot

df = load_data("C:/Users/T.Haneesh/ml/churn-bigml-20.csv")

question = "Give 3 key insights from this churn data."
response = ask_llama_from_df(df, question)
print("LLaMA-4's Answer:\n")
print(response)

plot_churn_boxplot(df)
