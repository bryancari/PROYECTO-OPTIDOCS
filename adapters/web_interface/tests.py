from django.test import TestCase
from adapters.web_interface.mappers import EntitiesMappers
from adapters.web_interface.models import (
    DocumentModel,
    ResultOCRModel,
    ConfigDocModel,
    OCRProvider,
    DocumentTypeModel,
    Language,
)
from core.domain.entities.resultOCR import ResultOCR
from django.contrib.auth.models import User


class TestMappers(TestCase):

    def setUp(self):

        self.user = User.objects.create(username="testuser")
        self.language = Language.objects.create(code="es", name="Español")
        self.ocr = OCRProvider.objects.create(name="tesser")
        self.doc_type = DocumentTypeModel.objects.create(name="Factura")

        self.config = ConfigDocModel.objects.create(
            ocr_chosen=self.ocr, type_doc=self.doc_type, language=self.language
        )

        self.result = ResultOCRModel.objects.create(
            raw={"text": "raw text"},
            clean={"text": "clean text"},
            success=True,
            mistakes=[],
        )

    def test_document_model_to_document(self):
        model = DocumentModel.objects.create(
            user=self.user,
            config=self.config,
            result=self.result,
            processed=True,
            doc_file="documentos/test.pdf",
        )

        document = EntitiesMappers.document_model_to_document(model)

        self.assertEqual(document.id, model.id)
        self.assertEqual(document.id_user, self.user.id)
        self.assertEqual(document.id_config_doc, self.config.id)
        self.assertEqual(document.id_resultOCR, self.result.id)
        self.assertEqual(document.doc_file, model.doc_file)
        self.assertEqual(document.processed, model.processed)

    def test_resultOCR_model_to_resultOCR(self):
        entity = EntitiesMappers.resultOCR_model_to_resultOCR(self.result)

        self.assertEqual(entity.id, self.result.id)
        self.assertEqual(entity.raw, self.result.raw)
        self.assertEqual(entity.clean, self.result.clean)
        self.assertEqual(entity.success, self.result.success)
        self.assertEqual(entity.mistakes, self.result.mistakes)

    def test_resultOCR_to_resultOCR_model_without_id(self):
        entity = ResultOCR(
            raw={"k": "v"}, clean={"k": "v_clean"}, success=True, mistakes=[]
        )

        model = EntitiesMappers.resultOCR_to_resultOCR_model(entity)

        self.assertEqual(model.raw, entity.raw)
        self.assertEqual(model.clean, entity.clean)
        self.assertEqual(model.success, entity.success)
        self.assertEqual(model.mistakes, entity.mistakes)
