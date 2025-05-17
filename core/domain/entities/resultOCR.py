class ResultOCR:
    def __init__(self, id, raw, clean, success, mistakes):
        self.id = id
        self.raw = raw
        self.clean = clean
        self.success = success
        self.mistakes = mistakes