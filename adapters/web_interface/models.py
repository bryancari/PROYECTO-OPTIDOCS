from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birth = models.DateField(verbose_name="Fecha de nacimiento")
    permission = models.PositiveBigIntegerField(verbose_name="Permiso")

class ResultOCRModel(models.Model):
    raw = models.JSONField(default=dict, verbose_name="Resultado crudo")
    clean = models.JSONField(default=dict, verbose_name="Resultado procesado")
    success = models.BooleanField(default=False, verbose_name="Condición del crudo")    
    mistakes = models.JSONField(default=list, verbose_name="Errores")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de procesado")

    class Meta:
        db_table = "Resultados"
        verbose_name = "Resultado"
        verbose_name_plural = "Resultados"

class DocumentTypeModel(models.Model):
    name = models.CharField(max_length=80, verbose_name="Tipo de documento")
    
    class Meta:
        db_table = "Tipos de documentos"
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documentos"        

class LabelFieldValue(models.Model):
    value = models.CharField(max_length=80, verbose_name="Valor")

    class Meta:
        db_table = "Valores"
        verbose_name = "Valor de etiqueta"
        verbose_name_plural = "Valores de etiquetas"        

class LabelFieldModel(models.Model):
    name = models.CharField(max_length=80, verbose_name="Etiqueta")
    value_format = models.ForeignKey(LabelFieldValue, on_delete=models.CASCADE, verbose_name="Formato de la etiqueta")
    document_type = models.ForeignKey(DocumentTypeModel, on_delete=models.CASCADE, related_name="labels", verbose_name="Tipo de documento")

    class Meta:
        db_table = "Etiquetas"
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"        

"""
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
"""

class OCRProvider(models.Model):
    name = models.CharField(max_length=5, verbose_name="Servicio OCR")

    class Meta:
        db_table = "OCR_Providers"
        verbose_name = "Servicio OCR"
        verbose_name_plural = "Servicios OCR"

class Language(models.Model):
    code = models.CharField(max_length=10, verbose_name="Código")
    name = models.CharField(max_length=50, verbose_name="Lenguaje")

    class Meta:
        db_table = "Lenguajes"
        verbose_name = "Lenguaje"
        verbose_name_plural = "Lenguajes"        

class ConfigDocModel(models.Model):
    #ocr_chosen = models.CharField(max_length = 50, choices=ocr_choices, verbose_name="Opciones de OCR")
    #type_doc = models.CharField(max_length=50, choices=type_doc_choices, verbose_name="Tipos de documentos")
    #language = models.CharField(max_length=50, choices=languages_choices, verbose_name="Opciones de lenguaje")

    ocr_chosen = models.ForeignKey(OCRProvider, on_delete=models.CASCADE, verbose_name="Servicio OCR")
    type_doc = models.ForeignKey(DocumentTypeModel, on_delete=models.CASCADE, verbose_name="Tipo de documento")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Lenguaje")

    class Meta:
        db_table = "Configuraciones"
        verbose_name = "Configuración de documento"
        verbose_name_plural = "Configuraciones de documentos"

class DocumentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    config = models.ForeignKey(ConfigDocModel, on_delete=models.CASCADE, verbose_name="Configuración del documento")
    result = models.OneToOneField(ResultOCRModel, on_delete=models.CASCADE, verbose_name="Resultado del OCR")
    processed = models.BooleanField(default=False, verbose_name="Estado actual")
    doc_file = models.FileField(upload_to='documentos/', verbose_name="Archivo", null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        db_table = "Documentos"
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"