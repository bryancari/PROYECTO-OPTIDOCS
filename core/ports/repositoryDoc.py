from abc import ABC, abstractmethod

class RespositoryDoc(ABC):

    @abstractmethod
    def saveDocs():
        pass

    @abstractmethod
    def deleteDocs():
        pass

    @abstractmethod
    def filterDocs():
        pass
    
    @abstractmethod
    def listDocs():
        pass

    @abstractmethod
    def searchDocs():
        pass