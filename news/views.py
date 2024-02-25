from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *
from accounts.models import Account


# Create your views here.
@method_decorator(login_required, name='dispatch')
class NewPostView(View):
    def get(self,request):
        acc = Account.objects.get(user=request.user)
        if acc.user_type == 'public':
            msg = "Only a reporter can post news!"
            return redirect(f"/?msg={msg}")
        return render(request,'post.html')
    
    def post(self,request):
        title = request.POST.get("title")
        cover = request.FILES.get("cover")
        content = request.POST.get("content")

        acc = Account.objects.get(user=request.user)
        News.objects.create(title=title,content=content,news_cover_img=cover,posted_by=acc)
        msg = "News post successfully!"
        return redirect(f"/?msg={msg}")