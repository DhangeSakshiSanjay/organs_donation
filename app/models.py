from django.db import models
from django.contrib.auth.models import User

def document_upload_path(instance, filename):
    return f'documents/{instance.name}/{filename}'

def document_upload_path(instance, filename):
    return f'document1/{instance.id_document}/{filename}'

def documents_upload_path(instance, filename):
    return f'before_opt/{instance.file}/{filename}'

def documents_upload_path(instance, filename):
    return f'after_opt/{instance.file}/{filename}'

class Hospital(models.Model):
    fname = models.TextField(max_length=255)
    lname = models.TextField(max_length=255)
    hname = models.TextField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.hname


class Form(models.Model):
    name = models.TextField(max_length=255)
    hospital_name = models.CharField(max_length=255)
    organ_name = models.TextField(max_length=255,null=False)
    email = models.EmailField()
    id_document = models.ImageField(upload_to=document_upload_path)
    # healthcare_proxy = models.ImageField(upload_to=document_upload_path)
    organ_donor_card = models.ImageField(upload_to=document_upload_path)
    status = models.CharField(max_length=20, default='Pending')
    
    
    def __str__(self):
        return self.name
    
class Form1(models.Model):
    name = models.TextField(max_length=255)
    organ_name = models.CharField(max_length=255, default='')
    email = models.EmailField()
    id_document = models.ImageField(upload_to=document_upload_path)
    # healthcare_proxy = models.ImageField(upload_to=document_upload_path)
    organ_donor_card = models.ImageField(upload_to=document_upload_path)
    status = models.CharField(max_length=20, default='Pending')
    
    def __str__(self):
        return self.name
    
class FileDoc(models.Model):
    email = models.EmailField() 
    file = models.ImageField(upload_to=documents_upload_path)

    def __str__(self):
        return str(self.file)  
    
class FileDoc1(models.Model):
    email = models.EmailField() 
    file = models.ImageField(upload_to=documents_upload_path)

    def __str__(self):
        return str(self.file)  
