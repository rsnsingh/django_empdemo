from django.shortcuts import render
from empApp.models import Employee
from empApp.models import Contact
from empApp.forms import UserRegistrationForm
from . import forms
from empApp.models import Post

def employeedata(request):
    employees=Employee.objects.all()
    empDict={'employees': employees}
    return render(request, 'empApp/employees.html', empDict)

def indexpage(request):
    return render(request, 'empApp/index.html')


def contactpage(request):
    return render(request, 'empApp/contact.html')

def aboutpage(request):
    return render(request, 'empApp/about.html')

def homepage(request):
    return render(request, 'empApp/home.html')

def newspage(request):
    return render(request, 'empApp/news.html')

def userRegistrationView(request):
    form=forms.UserRegistrationForm()
    if request.method=='POST':
        form=forms.UserRegistrationForm(request.POST) #. .UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid  ")
            print("First Name: ",form.cleaned_data['firstName'])
            print("Last Name : ",form.cleaned_data['lastName'])
            print("Gender    : ",form.cleaned_data['gender'])
            print("Email     : ",form.cleaned_data['email'])
            print("Salary    : ",form.cleaned_data['salary'])
            print("password  : ",form.cleaned_data['password'])
        else:
            print("Form is invalid.....")
    return render(request,'empApp/userRegistration.html',{'form':form})


def contactus(request):
    if request.method=='POST':
        full_name=request.POST['fname']
        email=request.POST['email']
        message=request.POST['message']
        contact=Contact.objects.create(full_name=full_name,email=email,message=message)
        #messages.success(request,'Data has been submitted')
    return render(request,'empApp/contactus.html')

def createpost(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Post()
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()

            return render(request, 'empApp/create.html')

    else:
        return render(request, 'empApp/createpost.html')

    return render(request, 'empApp/createpost.html')

def showposts(request):
    posts= Post.objects.all()
    postDict={'posts': posts}
    return render(request, 'empApp/showposts.html', postDict)