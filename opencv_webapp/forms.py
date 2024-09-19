from django import forms
from .models import ImageUploadModel

# 기본 Form을 사용
class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)

    # 이미지필드는 파일필드에서 이미지에 최적화된 필드이다. file = forms.FileField()
    image = forms.ImageField()

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = ("description", "document",)
        