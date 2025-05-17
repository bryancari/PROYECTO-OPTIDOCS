from django.db import models

class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    birth = models.DateField()
    permission = models.PositiveBigIntegerField()

class ResultOCR(models.Model):
    raw = models.JSONField(default=dict)
    clean = models.JSONField(default=dict)
    success = models.BooleanField(default=False)    
    mistakes = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

ocr_choices = [
    ("desconocido", "Desconocido"),
    ("Azure", "Azure AI Vision"),
    ("Amazon", "Amazon Web Services"),
]

type_doc_choices = [
    ("desconocido", "Desconocido"),
    ("cedula", "Cédula"),
    ("RIF", "RIF"),
    ("ISLR", "ISLR"),
    ("Factura", "Factura"),
]

languages_choices = [
    ("desconocido", "Desconocido"),
    ("SPA", "Español"),
    ("ENG", "Inglés"),
]

class ConfigDoc(models.Model):
    ocr_chosen = models.CharField(max_length = 50, choices=ocr_choices)
    type_doc = models.CharField(max_length=50, choices=type_doc_choices)
    language = models.CharField(max_length=50, choices=languages_choices)

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    config = models.OneToOneField(ConfigDoc, on_delete=models.CASCADE)
    result = models.OneToOneField(ResultOCR, on_delete=models.CASCADE)
    processed = models.BooleanField(default=False)
    doc_file = models.FileField(upload_to='documentos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)