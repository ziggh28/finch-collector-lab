from django.shortcuts import render
from .models import finch

# Create your views here.
from django.http import HttpResponse

def home(request):
  return render(request,'home.html')

def about(request):  
  return render(request,'about.html')

def finches_index(request):
  finches = finch.objects.all()
  return render(request, 'finches/index.html', {'finches':finches})

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html',{'finch': finch })


class finch: 
  def _init_(self, name, color, avis):
    self.name = name
    self.color = color
    self.avis = avis

# finches = [
#   finch(flawless,birdy),
#   finch(b),
#   finch()
# ]
