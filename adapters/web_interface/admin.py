from django.contrib import admin
from .models import (
    UserProfile,
    ResultOCRModel,
    ConfigDocModel,
    DocumentModel,
    DocumentTypeModel,
    LabelFieldModel,
)
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from core.ocrEngine import main_ocr_function  # Asegúrate de tener esta función implementada


# --------------------------
# Extender el modelo de usuario con perfil
# --------------------------
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# --------------------------
# Modelos ConfigDoc y ResultOCR
# --------------------------
@admin.register(ConfigDocModel)
class ConfigDocAdmin(admin.ModelAdmin):
    list_display = ["id", "ocr_chosen", "type_doc", "language"]


@admin.register(ResultOCRModel)
class ResultOCRAdmin(admin.ModelAdmin):
    list_display = ["id", "success", "created_at"]
    readonly_fields = ["raw", "clean", "mistakes"]


# --------------------------
# Procesamiento de Documentos desde el admin
# --------------------------
@admin.register(DocumentModel)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "processed", "created_at", "preview_file"]
    readonly_fields = ["created_at", "updated_at"]
    actions = ["procesar_documentos"]

    def preview_file(self, obj):
        if obj.doc_file:
            return format_html('<a href="{}" target="_blank">Ver archivo</a>', obj.doc_file.url)
        return "Sin archivo"
    preview_file.short_description = "Archivo"

    def procesar_documentos(self, request, queryset):
        for doc in queryset:
            if not doc.processed:
                resultado = main_ocr_function(
                    filepath=doc.doc_file.path,
                    config={
                        "ocr": doc.config.ocr_chosen,
                        "type": doc.config.type_doc,
                        "lang": doc.config.language,
                    }
                )
                doc.result.raw = resultado.get("raw", {})
                doc.result.clean = resultado.get("clean", {})
                doc.result.success = resultado.get("success", False)
                doc.result.mistakes = resultado.get("mistakes", [])
                doc.result.save()
                doc.processed = True
                doc.save()
        self.message_user(request, "Los documentos seleccionados fueron procesados correctamente.")
    procesar_documentos.short_description = "Procesar documentos con OCR"

    def save_model(self, request, obj, form, change):
        # Solo crear resultado si no existe
        if not obj.result_id:
            result = ResultOCRModel.objects.create()
            obj.result = result
        super().save_model(request, obj, form, change)

# --------------------------
# Tipos de documentos y etiquetas dinámicas
# --------------------------
class LabelFieldInline(admin.TabularInline):
    model = LabelFieldModel
    extra = 1

@admin.register(DocumentTypeModel)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    inlines = [LabelFieldInline]


@admin.register(LabelFieldModel)
class LabelFieldAdmin(admin.ModelAdmin):
    list_display = ["name", "value_format", "document_type"]
