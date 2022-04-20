import pathlib
import re
import json
my_file = pathlib.Path("project.json")
if my_file.exists():
    with open(my_file, "r") as fr:
        f_ = json.load(fr)
        print(str(f_))
        str_1 = re.findall("'sampling_rate': '(.*?)'", str(f_))
        str_2 = re.findall("'Dominant_frequency': '(.*?)'", str(f_))
        str_3 = re.findall("'sampling_time': '(.*?)'", str(f_))
        str_4 = re.search("'xishu'",str(f_))

        if len(str_1) == 0 or len(str_2) == 0 or len(str_3) == 0 or str_4 == None:
            pass


else:
    pass