class Document: 
    def __init__(self, id, id_user, id_config_doc, id_resultOCR, doc_file, processed):
        self.id = id
        self.id_user = id_user
        self.id_config_doc = id_config_doc
        self.id_resultOCR = id_resultOCR
        self.doc_file = doc_file
        self.processed = processed

        