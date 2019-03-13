# @Time    :2018/11/30 13:35
# @Author  :lvjunjie

import json
import yaml
s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
params = yaml.load(s)
print(params)

