from django.urls import path
from . import views

# static 폴더를 설정하기 위해 불러옴
from django.conf.urls.static import static
# settings.py 불러옴
from django.conf import settings

app_name = "opencv_webapp"
# {% url 'opencv_webapp' ... %}

urlpatterns = [
    path('', views.first_view, name="first_view"),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path('detect_face/', views.detect_face, name="detect_face")
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)