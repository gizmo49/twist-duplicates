from django.http import HttpResponse
from django.shortcuts import render
from .models import Video
from .forms import UploadFileForm
from django.http import HttpResponseRedirect

def handle_uploaded_file(f):
    with open('media/uploads/video.mp4', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def showvideo(request):
   if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("success")
        else:
            form = UploadFileForm()
        
        return render(request, 'home.html', {'form': form})    
   else:
        form = UploadFileForm(request.POST, request.FILES)
        return render(request, 'home.html', {'form': form})    
