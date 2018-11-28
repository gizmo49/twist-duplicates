import uuid
# import cv2  
# import numpy as np
from django.http import HttpResponse
from django.shortcuts import render
from .models import Video
from .forms import UploadFileForm
from django.http import HttpResponseRedirect

def compare_videofiles(request):
    if request.method == 'POST':
        return HttpResponse('cap')

def handle_uploaded_file(f, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    with open('static/uploads/' + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        return ('../static/uploads/' + filename)

def showvideo(request):
   if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            path_res = handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
            return render(request, 'home.html', {'form': form, 'path_res':path_res})    
        else:
            form = UploadFileForm()
        
        return render(request, 'home.html', {'form': form})    
   else:
        form = UploadFileForm(request.POST, request.FILES)
        return render(request, 'home.html', {'form': form})    
