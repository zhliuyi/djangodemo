from django.http import HttpResponse

def index(request):
    """
    视图  函数视图
    :param request: 请求对象，包含了请求信息的一个请求对象
    :return: response 响应对象
    """
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("这是一个about页面")
def urltest(request,num):
    print(num)#这个在控制台的位置输出
    return HttpResponse("这是一个url测试视图%s"%(num))

def urltestnew(request,city,year):
    return HttpResponse("%s年在%s" % (year,city))
def hello():
    return "hello"

from django.template import Template,Context
def gethtml(request):
    html="""
    <html>
        <head>
        </head>
        <body>
        <h1>This  is {{name}}</h1>
        
        <a href="https://www.baidu.com/">点击到百度{{content}}</a>
        <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1568004730204&di=9a31a1fdedeb2fd07864763b9d306745&imgtype=0&src=http%3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F2017-11-11%2F5a06a6b3d5aae.jpg">
        <p style="color:red">青山宗上代掌门，景阳真人师兄，惊才绝艳，待人温润如玉，使人如沐春风，心思缜密，精于算计，亲手教出景阳，柳词，元骑鲸，南忘等人。朝天大陆最可怕的人物之一。由于当年的青山掌门亦恩师沉舟真人飞升失败道消，太平所在的上德峰一系受到诸峰排挤无法接任掌门，青山道统断绝。太平不得已设局亲下冥部卧底，并成功说服冥皇与人族谈判，冥皇虽受背叛被人族生擒，太平仍获得莫大功绩与声望并重回上德峰凝聚力量，最终清洗青山宗反对势力重回掌门之位重续青山道统。太平成为掌门后励精图治，率领青山宗先后抗击雪国，铲除邪道大派玄阴宗，确立梅会制度，成为朝天大陆第一人。但太平亦暗自施行极端理念“天下太平”，为景阳所不喜，终因意图夺舍前代神皇，触犯景阳逆鳞，被景阳连同元柳二人镇压，打入剑狱300年。在景阳飞升时用移魂之法逃离剑狱，借一名冥部弟子身体逃出化名阴三。</p>
        
        </body>
    
    
    
    </html>
    
    
    
    """

    #1.构建模板结构
    template_obj=Template(html)
    #2.创建渲染模板
    params=dict(name='w我是谁',content="ninininini")
    content_obj=Context(params)

    #3.进行数据渲染
    result=template_obj.render(content_obj)
    #4.返回结果
    return HttpResponse(result)

    # return HttpResponse(html)


from django.shortcuts import render
def indextmp(request):
    name='哈士奇'
    return render(request,'index.html',{'name':name})

from django.shortcuts import render_to_response
def abc(request):
    name = "hi"
    return render_to_response("abc.html",{"name":name})


# from django.template.loader import get_template
# def abc(request):
#     template = get_template("abc.html")
#     name = "hello"
#     result = template.render({'name':name})
#
#     return HttpResponse(result)

def tpltest(request,age):
    class Say(object):
        def say(self):
            return "hello"
    name="张三"
    # age=19
    age=int(age)
    hobby=["eat","sing","pingfang","football"]
    score={"shuxue":89,"yingyu":89,"yuwen":100}
    say=Say()
    # return  render(request,"tpltest.html",{'name':name,"age":age,"hobby":hobby,"score":score})
    return render(request, "tpltest.html", locals())

def statictest(request):
    return render(request,'statictest.html')

def staticdemo(request):
    params=[
        {"name":"麦迪","img":"maidi.jpg","url":"https://baike.baidu.com/item/%E7%89%B9%E9%9B%B7%E8%A5%BF%C2%B7%E9%BA%A6%E6%A0%BC%E9%9B%B7%E8%BF%AA/6118977?fromtitle=%E9%BA%A6%E8%BF%AA&fromid=136057&fr=aladdin"},
        {"name":"科比","img":"kb.jpg","url":"https:www.baidu.com"},
        {"name": "姚明", "img": "ym.jpg", "url": "https:www.sina.com"},
        {"name": "易建联", "img": "yjl.jpg", "url": "https:www.taobao.com"},
    ]
    return  render(request,"staticdemo.html",locals())

def staticdemo2(request):
    params=[
        {"name": "麦迪", "img": "maidi.jpg","age": "22"},
        {"name": "科比", "img": "kb.jpg", "age": "23"},
        {"name": "姚明", "img": "ym.jpg", "age": "32"},
        {"name": "易建联", "img": "yjl.jpg", "age": "12"},
    ]
    return  render(request,"staticdemo2.html",locals())