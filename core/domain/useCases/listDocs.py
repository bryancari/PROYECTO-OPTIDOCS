from core.ports.repositoryDoc import RepositoryDoc
from core.domain.entities.document import Document


class ListDocsUseCase:
    def __init__(self, repository: RepositoryDoc):
        self.repository = repository

    def listDocs(self) -> list[Document]:
        return self.repository.listDocs()
