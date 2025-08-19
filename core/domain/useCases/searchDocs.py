from core.ports.repositoryDoc import RepositoryDoc
from core.domain.entities.document import Document


class SearchDocsUseCase:
    def __init__(self, repository: RepositoryDoc):
        self.repository = repository

    def search(self, doc_id: int | str) -> Document:
        return self.repository.searchDocs(doc_id)
