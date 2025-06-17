import pandas as pd
from llama_interface import ask_llama_from_df

file_path = "C:/Users/T.Haneesh/ml/churn-bigml-20.csv"
df = pd.read_csv(file_path)
question = "Give 3 key insights from this churn data."
response = ask_llama_from_df(df, question)
print("LLaMA-4's Answer:\n")
print(response)
