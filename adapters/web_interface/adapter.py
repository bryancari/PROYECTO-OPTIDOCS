from core.ports.repositoryDoc import RepositoryDoc
from core.domain.entities.document import Document
from .models import DocumentModel
from adapters.web_interface.mappers import EntitiesMappers

class RepositorySQLAdapter(RepositoryDoc):
    def saveDocs(self, document: Document):
        doc_model = EntitiesMappers.document_to_document_model(document)
        doc_model.save()
        return EntitiesMappers.document_model_to_document(doc_model)
    
    def searchDocs(self, doc_identifier) -> Document:
        try:
            if isinstance(doc_identifier, int):
                model = DocumentModel.objects.get(id=doc_identifier)
            else:        
                model = DocumentModel.objects.get(doc_file__icontains=doc_identifier)
            return EntitiesMappers.document_model_to_document(model)
        except DocumentModel.DoesNotExist:
            raise ValueError("Documento no encontrado")

    def filterDocs(self, **filters) -> list[Document] :
        results = DocumentModel.objects.filter(**filters)
        return [EntitiesMappers.document_model_to_document(doc) for doc in results]
    
    def listDocs(self) -> list[Document]:
        results = DocumentModel.objects.all()
        return [EntitiesMappers.document_model_to_document(doc) for doc in results]
    
    def deleteDocs(self, doc_identifier):
        try:
            if isinstance(doc_identifier, int):
                model = DocumentModel.objects.get(id=doc_identifier)
            else:
                model = DocumentModel.objects.get(doc_file__icontains=doc_identifier)            
            model.delete()
        except DocumentModel.DoesNotExist:
            raise ValueError("Documento no encontrado")        