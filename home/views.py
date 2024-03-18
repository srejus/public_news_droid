from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from news.models import News,Comment
from accounts.models import Account

# Create your views here.
class IndexView(View):
    def detect_fake(self,comments,news):
        predefined_list = ['fake', 'incorrect', 'invalid', 'fabricated', 'misleading', 'untrue', 'deceptive', 'bogus']

        comment_list = comments.values_list('comment',flat=True)
        new_comment_list = [i.lower() for i in comment_list]
        
        count_predefined = 0
        total_comments = 0
        
        for comment in new_comment_list:
            words = comment.split()  # Split comment into words
            for word in words:
                if word.lower() in predefined_list:
                    count_predefined += 1
            total_comments += 1

        # Determine if most comments contain words from predefined list
        threshold = 0.5  # Adjust as needed, e.g., if over 50% of comments contain predefined words
        if total_comments > 0 and count_predefined / total_comments >= threshold:
            news.is_fake = True
            news.save()
            return "Fake"
        else:
            return "Correct"
    
    def get(self,request,id=None):
        news = News.objects.all().order_by('-id')
        if id:
            news = news.get(id=id)
            if request.user.is_authenticated:
                acc = Account.objects.get(user=request.user).user_type
            else:
                acc = None
            comments = Comment.objects.filter(news=news).order_by('-id')
            if news.is_fake == False:
                x = self.detect_fake(comments,news)
                print("X Value " ,x)
            return render(request,'single_news.html',{'news':news,'acc':acc,'comments':comments})
        
        msg = request.GET.get("msg")
        return render(request,'index.html',{'all_news':news,'msg':msg})

    def post(self,request,id=None):
        comment = request.POST.get("comment")

        news = News.objects.get(id=id)
        acc = Account.objects.get(user=request.user)
        Comment.objects.create(commented_by=acc,news=news,comment=comment)
        
        return redirect(f"/{id}")
        
    

@method_decorator(login_required, name='dispatch')
class ReporterIndexView(View):
    def get(self,request):
        news = News.objects.filter(posted_by__user=request.user).order_by('-id')
        acc = Account.objects.get(user=request.user)
        if acc.user_type != 'reporter':
            return redirect("/")
        
        return render(request,'index_reporter.html',{'all_news':news,"acc":acc})