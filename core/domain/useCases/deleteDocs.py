from core.ports.repositoryDoc import RepositoryDoc

class DeleteDocsUseCase:
    def __init__(self, repository: RepositoryDoc):
        self.repository = repository

    def search(self, doc_id: int | str):
        self.repository.deleteDocs(doc_id)