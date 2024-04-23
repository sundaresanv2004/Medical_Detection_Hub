from django.shortcuts import render, redirect

from .ml.pneumonia_detection import pneumonia_detection
from .ml.skin_cancer import skin_cancer_cla
from .models import Category, UploadImage
from .forms import UploadImageForm


def home(request):
    category = Category.objects.all()
    return render(request, 'home.html', {'category': category})


def image_process(ty, id_):
    image = UploadImage.objects.get(id=id_)
    if ty == "Skin Cancer Detection":
        return skin_cancer_cla(str(image.image))
    elif ty == 'Pneumonia Detection':
        return pneumonia_detection(str(image.image))


def upload(request, pk):
    category = Category.objects.get(id=pk)
    form = UploadImageForm()
    image = UploadImage()
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image.category_id = pk
            image.image = form.cleaned_data['image']
            image.save()
            dict1 = image_process(category.title, image.id)
            image = UploadImage.objects.get(id=image.id)
            image.result = dict1['name']
            image.description = dict1['desc']
            image.score = dict1['range']
            image.save()
            return redirect('result', image.id)

    return render(request, 'upload.html', {'category': category, 'form': form})


def result(request, pk1):
    form = UploadImage.objects.get(id=pk1)
    category = Category.objects.get(id=form.category_id)

    return render(request, 'result.html', {'category': category, 'form': form})
