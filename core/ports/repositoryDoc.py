from abc import ABC, abstractmethod
from core.domain.entities.document import Document
from typing import List, Optional, Any


class RepositoryDoc(ABC):
    @abstractmethod
    def saveDocs(self, document: Document) -> Document:
        pass

    @abstractmethod
    def deleteDocs(
        self, doc_id: Optional[int] = None, doc_name: Optional[str] = None
    ) -> None:
        pass

    @abstractmethod
    def filterDocs(self, **filters: Any) -> List[Document]:
        pass

    @abstractmethod
    def listDocs(self) -> List[Document]:
        pass

    @abstractmethod
    def searchDocs(
        self, doc_id: Optional[int] = None, doc_name: Optional[str] = None
    ) -> Optional[Document]:
        pass
