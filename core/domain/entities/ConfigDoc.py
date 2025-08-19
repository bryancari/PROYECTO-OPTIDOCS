from typing import Optional


class ConfigDoc:
    def __init__(self, ocr_chosen, type_doc, language, id: Optional[int] = None):
        self.id = id
        self.ocr_chosen = ocr_chosen
        self.type_doc = type_doc
        self.language = language
