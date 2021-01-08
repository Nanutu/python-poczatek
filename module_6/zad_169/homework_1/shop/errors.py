class OrderElementsLimitError(Exception):
    def __init__(self, places_limit, message=None, *args):
        self.places_limit = places_limit
        if message is None:
            message = f"Przekroczono limit ilości elementów zamówienia, który wynosi {places_limit}."
        super().__init__(message, *args)
