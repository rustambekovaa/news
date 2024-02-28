# from django.shortcuts import render

from django.shortcuts import render

from app1.models import News

def main(request):
    app1 = News.objects.all()
    return render(request,'index.html',{'app1_list':app1})
# Create your views here.
