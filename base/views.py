from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import re
from.models import myData
# Create your views here.


def index (request):
    dat = request.GET.get('text')
    dat = request.GET.get('text')
   
    if dat:
        myWords = len(dat.split())
        myCharacter = len(dat)
        noSpace = len(dat.replace(" ",""))
        syllable_count = sum(len(list(filter(lambda x: x != '', word.split('-')))) for word in dat.split())
        num_sentences = len(re.split('[.!?]', dat))
        num_paragraphs = len(dat.split('\n\n'))
    # Handle the case where 'text' is empty or not present
    else:
        myWords = 0  
        myCharacter = 0
        noSpace = 0
        syllable_count = 0
        num_sentences = 0
        num_paragraphs = 0
    return render(request,'index.html',{'total': myWords, 'total1': myCharacter,'noSpace1':noSpace,'syllableCount': syllable_count,'numSentences':num_sentences,'numParagraphs':num_paragraphs})
def registration(request):
    
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']

        if password== password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'The username already exist')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'The email already exists')
                return redirect('registration')
            else:
                user=User.objects.create_user(username=username, password=password,email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password mismatch')
            return redirect ('registration')
    else:
        return render(request,'register.html') 
    
def login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect ('index')
        else:
            messages.info(request,'Wrong credentials')
            return redirect ('registration')    
    else:
        return render(request,'login.html')
    