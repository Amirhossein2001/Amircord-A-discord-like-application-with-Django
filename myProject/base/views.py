from django.shortcuts import render

rooms = [
    
    {'id':1, 'name':'lets learn python'},
    {'id':2, 'name':'lets learn JS'},
    {'id':3, 'name':'lets learn React.js'}
]



def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request,pk):
    return render(request, 'base/room.html')
