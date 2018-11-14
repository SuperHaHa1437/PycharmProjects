import re

text = 'a) Preparation.<br>The six aspects of preparation are the activities of Ser-ling-ba. <br>【◎ 初加行法有六，乃是金洲大師傳記，】,python i use superhaha'

# a = re.findall('【[\s\S]{0,}】',text)
# a = re.search('【(.*)】',text)
a = re.findall('【(.*)】(.*)superhaha', text)
print(a)
