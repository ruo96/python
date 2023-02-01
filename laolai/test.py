import pandas as pd

zetyun_data = pd.read_csv("dataset/zetyun.csv")
scc_data = pd.read_csv("dataset/scc.csv")
esf_data = pd.read_csv("dataset/esf.csv")

li_zetyun = zetyun_data['id'].values.tolist()
li_scc = scc_data['id'].values.tolist()
li_esf = esf_data['id'].values.tolist()

intersection_1 = [x for x in li_zetyun if x in li_scc]

intersection_2 = [x for x in intersection_1 if x in li_esf]

print(len(intersection_2))
