import uuid
import cv2  
import random
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm


def compare_videofiles(request):
    if request.method == 'POST':
        # cap = cv2.VideoCapture('static/uploads/3bf9ac21-64be-4f85-8ae7-586fda750b5f.mp4')
        cap2 = cv2.VideoCapture('static/uploads/ee8889e1-955c-4a93-bac1-64c7436fca0d.avi')
        allframes = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
        randrange = random.sample(range(1, allframes), 5)
        for i in randrange:
            print("oldhead%s.jpg"%str(i))
            cap2.set(1, int(i))
            success, frame2 = cap2.read()
            cv2.imwrite("oldhead%s.jpg"%str(i), frame2)
        return HttpResponse('COMPLETELY UNRELATTED VIDEOS')
       

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
