from django.shortcuts import render

def flower(request):
    return render(request,"flower.html")
def honey(request):
    return render(request,"bees.html")
def finish(request):
    name=request.GET.get('name')
    num1=int(request.GET.get('number1'))
    num2=int(request.GET.get('number2'))
    print(name)
    print(num1)
    print(num2)
    sum=num1+num2
    return render(request,"submit.html",{"sum":sum,"name":name,"num1":num1,"num2":num2})
def submit(request):
    return render(request,"form.html")
