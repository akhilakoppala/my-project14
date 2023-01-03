from django.shortcuts import render

# Create your views here.
def looping(request):
    d={'name':'akhila'}
    return render(request,'looping.html',context=d)

