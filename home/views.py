from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from news.models import News
from accounts.models import Account

# Create your views here.
class IndexView(View):
    def get(self,request,id=None):
        news = News.objects.all().order_by('-id')
        if id:
            news = news.get(id=id)
            return render(request,'single_news.html',{'news':news})
        
        return render(request,'index.html',{'all_news':news})
    

@method_decorator(login_required, name='dispatch')
class ReporterIndexView(View):
    def get(self,request):
        news = News.objects.filter(posted_by__user=request.user).order_by('-id')
        acc = Account.objects.get(user=request.user)
        return render(request,'index_reporter.html',{'all_news':news,"acc":acc})