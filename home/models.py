import uuid
from django.db import models


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    file_desc = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class UploadImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    description = models.TextField(null=True, blank=True)
    result = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    score = models.CharField(max_length=200, null=True, blank=True)
