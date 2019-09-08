"""
正则表达式：是一种字符串的处理方式，用于字符串的匹配
字符串的匹配有两种：
    内容匹配    python re
        通过描述要匹配的内容的类型和数量来实现匹配
    结构匹配    xpath
        通过描述要匹配的内容在整体中的结构来实现匹配
"""
import re
string = "hello \n  \t world 1234  _ _ "
# 类型匹配
# 原样匹配
# res = re.findall("正则表达式",字符串)
# res = re.findall("l",string)
# print (res)#['l', 'l', 'l']
# . 除了 \n 之外的所有内容
# res = re.findall(".",string)
# print (res)#['h', 'e', 'l', 'l', 'o', ' ', ' ', ' ', '\t', ' ', 'w', 'o', 'r', 'l', 'd', ' ', '1', '2', '3', '4', ' ', ' ', '_', ' ', '_', ' ']
# \d  匹配的是数字
# res = re.findall("\d\d\d",string)
# print (res)#['123']
# \D 除了数字的所有字符
# res= re.findall("\D",string)
# print (res)
# \w 匹配数字  字符 下划线
# res = re.findall("\w",string)
# print (res)#['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', '1', '2', '3', '4', '_', '_']
# \W 除了 \w 的所有内容
# res = re.findall("\W",string)
# print (res)#[' ', '\n', ' ', ' ', '\t', ' ', ' ', ' ', ' ', ' ', ' ']
# [] 返回中括号中的任意一个字符
# res = re.findall("[a-zA-Z0-9]",string)
# print (res)
# #  取反
# res = re.findall("[^a-zA-Z0-9]",string)
# print (res)
# | 匹配任意一边的字符
# res = re.findall("hello|world",string)
# print (res)#['hello', 'world']

string = "hello \n  \t world 111 333  _ _ "

# () 组匹配 将括号后面的作为条件
# res = re.findall("\dw",string)#格式必须是一个数字和一个字母，才有结果
# print (res)#[]  ['1w']
# res = re.findall("(\d)w",string)#（）后面的是一个条件，所以不包含在结果内部
# print (res)#['1']
# res = re.findall("(\d)h",string)
# print (res)

# # 分组 起一个组名  组名叫id
#  id  = \d
# res = re.findall("(?P<id>\d)h",string)
# print (res)
# (?P=id)  对前面的组名 id 的引用   id= 2
# (?P<id>\d)h(?P=id)  (?P<id>\d)h2  111    (\d)\d1
# res = re.findall("(?P<id>\d)\d(?P=id)",string)#这里为何只输出一个1
# print (res)#['1', '3']
# res = re.findall("(?P<id>\d)h2",string)
# print (res)#[]

string = "hello \n  \t world 111 333  _ _ "
# 长度匹配
# # * 匹配0个或者多个
# res = re.findall("\d*",string)
# print(res)#['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '111', '', '333', '', '', '', '', '', '', '']
# # + 匹配1个或者多个
# res = re.findall("\d+",string)
# print(res)#['111', '333']
# # ? 匹配0个或者 1个
# res = re.findall("\d?",string)
# print (res)#['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1', '1', '1', '', '3', '3', '3', '', '', '', '', '', '', '']
# # {} 匹配指定次数
# res = re.findall("\d{2}",string)
# print (res)#['11', '33']
# res = re.findall("\d{1,3}",string)
# print (res)#['111', '333']
# 特殊匹配
string = "hello \n  \t world 111 333  _ _ k"

# ^ 匹配开头
# res = re.findall("^\w{1,3}",string)
# print (res)#['hel']
# # $ 匹配结尾
res = re.findall("\w$",string)#只返回回来一个以结尾
print (res)#['k']





