from django.shortcuts import render
from django.http import HttpResponse
from book.models import Book
import requests
import json

#根据ISBN查询数据库获取书籍信息
def GetBookInformation_Mysql(isbn):
    thisbook = Book.objects.filter(isbn=isbn)
    if thisbook.count() == 0:
        return False, 0
    return True, thisbook[0]


#根据ISBN调用98API获取书籍信息
def GetBookInformation_API(isbn):
    #联网调用API
    bookinformation = requests.get("https://www.98api.cn/api/isbn.php?isbn="+isbn)
    #获取页面内容
    bookinformation = bookinformation.text
    #解码
    bookinformation = bookinformation.encode('utf-8').decode('unicode_escape')
    #转化成字典
    bookinformation = json.loads(bookinformation)
    #查找出错,ISBN不存在
    if 'error' in bookinformation.keys() or 'title' not in bookinformation.keys():
        return False, 0
    #将API中的信息存入数据库中
    thisbook = Book()
    thisbook.isbn = isbn
    thisbook.title = bookinformation.get('title', "")
    Author = bookinformation.get('author', "")
    if type(Author) == list and len(Author) != 0:
        tot = ""
        for everyone in Author:
            tot += everyone.get('name', "")
            tot += " "
        thisbook.author = tot
        print(tot)
    thisbook.logo = bookinformation.get('logo', "")
    thisbook.publisher = bookinformation.get('publisher', "")
    thisbook.published = bookinformation.get('published',  "")
    thisbook.page = bookinformation.get('page', "")
    thisbook.price = bookinformation.get('price', "")
    thisbook.designed = bookinformation.get('designed', "")
    thisbook.description = bookinformation.get('description', "")
    thisbook.save()
    return True, thisbook


#根据ISBN获取书籍信息
def GetBookInformation(isbn):
    thisbook = GetBookInformation_Mysql(isbn)
    if thisbook[0] == False:
        thisbook = GetBookInformation_API(isbn)
    if thisbook[0] == False:
        return False, 0
    else:
        return True, thisbook[1]    

#/isbn=... URL对应的函数
def Query_ISBN(request, isbn):
    #return HttpResponse(isbn)
    #根据ISBN查询信息
    Result = GetBookInformation(isbn)
    #构造JSON格式返回数据
    ResultJson=""
    if Result[0] == False:
        ResultJson={"error":"未查询到结果"}
    else:
        #ISBN查询成功，构造JSON格式数据
        ResultJson={}
        ResultJson['isbn'] = Result[1].isbn
        ResultJson['title'] = Result[1].title
        ResultJson['author'] = Result[1].author
        ResultJson['logo'] = Result[1].logo
        ResultJson['publisher'] = Result[1].publisher
        ResultJson['published'] = Result[1].published
        ResultJson['page'] = Result[1].page
        ResultJson['price'] = Result[1].price
        ResultJson['designed'] = Result[1].designed
        ResultJson['description'] = Result[1].description
        
    return HttpResponse(json.dumps(ResultJson, ensure_ascii=False), content_type="application/json,charset=utf-8" )
    #return HttpResponse(ResultJson)


#/book
def Query_Book(requests):
    return HttpResponse("Hello")