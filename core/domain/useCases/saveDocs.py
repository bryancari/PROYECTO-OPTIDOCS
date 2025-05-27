from core.ports.repositoryDoc import RepositoryDoc
from core.domain.entities.document import Document

class SaveDocUseCase:
    def __init__(self, repository: RepositoryDoc):
        self.repository = repository

    def save(self, document: Document) -> Document:
        return self.repository.saveDocs(document)