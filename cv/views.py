from django.shortcuts import render,HttpResponse
from .models import Profile
# Create your views here.
def index(request):
    user_cv= Profile.objects.all()
    context={
        'user_cv':user_cv
    }
    return render(request,'cv/index.html',context)