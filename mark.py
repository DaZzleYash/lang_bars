import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
df = pd.read_csv('data.csv')
responses = df['LanguagesWorkedWith']
required_query = Counter()
for response in responses:
	required_query.update(response.split(';'))
lang_name, popularity = [], []
for i in required_query.most_common(18):
	lang_name.append(i[0])
	popularity.append(i[1])
lang_name.reverse()
popularity.reverse()
plt.barh(lang_name, popularity)
plt.show()
# print(required_query)