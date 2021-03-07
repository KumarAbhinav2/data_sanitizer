from sanitizer.settings import RULES

class JsonSanitizer:
    """
    Json Controller

    Attributes:
    -----------
    json_service: object

    Methods:
    --------
    rules:
        matches for the validity of the rules
    sanitize:
        called protected method
    _sanitize:
        recursive function to sanitize all keys/values
    """

    def __init__(self, json_service):
        self.json_service = json_service

    @staticmethod
    def rules(val):
        """
        :param val:
        :return:
        """
        # More rules can be added as per need
        if all(rule(val) for rule in RULES):
            return True
        return False

    def sanitize(self):
        """
        :return: dict
        """
        value = self.json_service.get_json()
        return self._sanitize(value)

    def _sanitize(self, value):
        """
        :param value: union(str, dict, list)
        :return: dict
        """
        if isinstance(value, dict):
            return {key: self._sanitize(val) for key, val in value.items() if self.rules(val)}
        elif isinstance(value, list):
            return [self._sanitize(x) for x in value if x]
        else:
            return value