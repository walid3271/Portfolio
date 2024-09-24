from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {
        'title':'Walid\'s Portfolio',
        'name':'Munsi Walid Al Hassan Nizhu',
        'skills':['Programming', 'Algorithm', 'Python', 'PyTorch', 'TensorFlow','Datasets','NLP', 'Object Detection', 'Segmentation', 'Pose Estimation', 'FastAPI']
    }
    return render(request,"home.html",data)
