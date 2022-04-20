import json
D = []
with open("project.json", "r") as fr:
    f_ = json.load(fr)
    R = f_["xishu"]
for i in list(R):
    D.append(float(i))
print(D)