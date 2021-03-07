import json
from json.decoder import JSONDecodeError
from sanitizer.exceptions import InvalidJsonError
from sanitizer.services.interfaces import JsonSanitizerInterface
from sanitizer import logger

log = logger.getLogger(__name__)


class JsonSanitizerService(JsonSanitizerInterface):
    """
    Json Sanitizer Service

    Attributes:
    ----------
    json_details: list

    Methods:
    ----------
    add_json
        loads json details into json list
    get_json
        reads json from the json list
    """

    json_details = []

    @staticmethod
    def verify_json(in_json):
        """
        :param in_json: str
        :return:
        """
        try:
            return json.loads(in_json)
        except JSONDecodeError:
            raise InvalidJsonError

    def add_json(self, in_json):
        """
        :param in_json: str
        :return: None
        """
        JsonSanitizerService.json_details.append(self.verify_json(in_json))
        log.info("Json loaded successfully....")

    def get_json(self):
        """
        :return: json string
        """
        log.info("Retrieving json.....")
        return JsonSanitizerService.json_details.pop()