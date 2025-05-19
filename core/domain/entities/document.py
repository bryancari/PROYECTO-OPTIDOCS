from typing import Optional
from datetime import datetime

class Document: 
    def __init__(self, id_user, id_config_doc, id_resultOCR, doc_file, processed, 
                 id: Optional [int] = None, created_at: Optional[datetime] = None, updated_at: Optional[datetime] = None):
        self.id = id
        self.id_user = id_user
        self.id_config_doc = id_config_doc
        self.id_resultOCR = id_resultOCR
        self.doc_file = doc_file
        self.processed = processed
        self.created_at = created_at
        self.updated_at = updated_at

        