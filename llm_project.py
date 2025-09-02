#تحليل المشاعر 

!pip install pandas transformers openpyxl
import pandas as pd
from transformers import pipeline

from google.colab import files
upload=files.upload()


df= pd.read_csv(list(upload.keys())[0])


print("أول 5 أسطر من البيانات ")
print(df.head())

sentiment_model= pipeline("sentiment-analysis" , model="nlptown/bert-base-multilingual-uncased-sentiment")


df["Sentiment"] = df["comment"].apply(lambda x: sentiment_model(str(x))[0]["label"])


print("/n البيانات بعد التحليل:")
print(df.head())

output_path = "comments_with_sentiment.xlsx"
df.to_excel(output_path, index=False)

print("تم انشاء الملف بنجاح :{output_path}")
files.download(output_path)
