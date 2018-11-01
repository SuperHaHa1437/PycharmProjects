# import re
import json
from enum import Enum, unique


#
# a = "life is short,i use python,i love python"
#
# r = re.findall('life(.*)python(.*)python',a)
# print(r)
# json_str = '{"name":"zhang","age":18}'
# student = json.loads(json_str)
@unique
class VIP(Enum):
    YELLOW = 1
    GREEN = 1
    BLUE = 2
