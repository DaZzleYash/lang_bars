import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

df = pd.read_csv("data.csv")
data = Counter()
for i in df['LanguagesWorkedWith']:
	data.update(i.split(";"))
# print(data)
# print(data.most_common(15))
lang_name, popularity = [], []
for i in data.most_common(18):
	lang_name.append(i[0])
	popularity.append(i[1])

# print(lang_name)
# print(popularity)

plt.pie(popularity[:5], 
	labels = lang_name[:5], 
	startangle = 90, 
	explode = [0, 0, 0, 0.1, 0.1], 
	shadow = True, 
	autopct = '%1.1f%%'
)
plt.title("Mark II")
plt.show()