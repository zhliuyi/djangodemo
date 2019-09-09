import re
s="飞流直下三千尺，疑是银河落九天"
res=re.findall('三(.{2})',s)
print(res)#['千尺']
import re
s="飞流直下三千尺，疑是银河落九天"
res=re.findall('三.{2}',s)
print(res)#['三千尺']
