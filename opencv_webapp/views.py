from django.shortcuts import render
from .forms import SimpleUploadForm, ImageUploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .cv_functions import cv_detect_face

# Create your views here.

def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})


def simple_upload(request):

    if request.method == "POST":
        # request.POST # title
        # request.FILES # image
        form = SimpleUploadForm(request.POST, request.FILES)

        if form.is_valid():
            myfile = request.FILES['image'] # 메모리에 일시적으로 저장된 파일
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile) # 저장이 끝난 파일
            uploaded_file_url = fs.url(filename) # 저장이 끝난 파일로 접근하는 url
            # fs.save() / fs.url() / fs.delete()

            context = {'form':form, 'uploaded_file_url': uploaded_file_url}
            return render(request, 'opencv_webapp/simple_upload.html', context)
    else:
        form = SimpleUploadForm()
        context = {"form":form}
        return render(request, 'opencv_webapp/simple_upload.html', context)
    

def detect_face(request):
    if request.method == 'POST' :
        form = ImageUploadForm(request.POST, request.FILES) # filled form

        if form.is_valid():
            post = form.save(commit=False) # 중간 저장
            # save() 함수는 DB에 저장될 ImageUploadModel 클래스 객체 자체를 리턴함 (== record 1건)
            # Form에 채워진 데이터를 DB에 실제로 저장하기 전에 변경/추가할 수 있음 (commit=False)
            # ex) post.description = papago.translate(post.description)
            post.save() # Form 객체('form')에 채워져 있는 데이터를 DB에 실제로 저장
            # document : ImageUploadModel Class에 선언되어 있는 “document”에 해당

            # form.instance는 채워진 form을 말한다.
            imageURL = settings.MEDIA_URL + form.instance.document.name
            # == form.instance.document.url
            # == post.document.url
            # => '/media/images/2021/10/29/ses_XQAftn4.jpg'
            
            cv_detect_face(settings.MEDIA_ROOT_URL + imageURL) # 추후 구현 예정
            # => './media/images/2021/10/29/ses_XQAftn4.jpg'
            
            return render(request, 'opencv_webapp/detect_face.html', {'form':form, 'post':post})
    else:
        form = ImageUploadForm() # empty form
        return render(request, 'opencv_webapp/detect_face.html', {'form':form})