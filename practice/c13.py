import re

text = 'a) Preparation.<br>The six aspects of preparation are the activities of Ser-ling-ba. <br>【◎ 初加行法有六，乃是金洲大師傳記，】'

a = re.findall('【[\s\S]{0,}】',text)
print(a)