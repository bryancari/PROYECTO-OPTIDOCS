from core.ports.repositoryDoc import RepositoryDoc
from core.domain.entities.document import Document


class FilterDocsUseCase:
    def __init__(self, repository: RepositoryDoc):
        self.repository = repository

    def filterDocs(self, **kwargs) -> list[Document]:
        return self.repository.filterDocs(**kwargs)
