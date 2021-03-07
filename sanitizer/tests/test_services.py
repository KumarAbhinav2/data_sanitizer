from sanitizer.services.services import JsonSanitizerService
import unittest
import json
from unittest.mock import patch, Mock
from sanitizer import logger
from sanitizer.exceptions import InvalidJsonError


class TestServices(unittest.TestCase):

    def setUp(self) -> None:
        self.obj = JsonSanitizerService()
        self.valid_in_json = '''{
                                  "k1" : "v1",
                                  "k2" : ["v2", "v3", "", {"k21": "v21", "k22": ""}],
                                  "k3" : {"k4" : "v4", "k5" : ["v5", "v6", null], "k6": {"k7" : "v7", "k8" : ""}},
                                  "k9" : null
                                }'''

        self.invald_in_json = '''{
                                    "k1": "v1",
                                    "k2": 
                                    }
                            '''

        self.expected = {'k1': 'v1', 'k2': ['v2', 'v3', {'k21': 'v21'}], 'k3': {'k4': 'v4', 'k5': ['v5', 'v6'], 'k6': {'k7': 'v7'}}}

    @patch('sanitizer.services.services.JsonSanitizerService.verify_json')
    def test_add_json(self, mock_verify):
        mock_verify.return_value = json.loads(self.valid_in_json)
        self.obj.add_json(self.valid_in_json)
        mock_verify.assert_called_once()
        self.assertLogs(logger.getLogger('test'), 'info')
        self.assertEqual(len(JsonSanitizerService.json_details), 1)

    @patch('sanitizer.services.services.JsonSanitizerService.verify_json')
    def test_add_json_raises_exception(self, mock_verify):
        mock_verify.side_effect = InvalidJsonError
        with self.assertRaises(InvalidJsonError):
            self.obj.add_json(self.invald_in_json)
        self.assertLogs(logger.getLogger('test'), 'error')

    def test_verify_json(self):
        ret = self.obj.verify_json(self.valid_in_json)
        self.assertIsInstance(ret, dict)
        self.assertEqual(ret, json.loads(self.valid_in_json))

    def test_verify_json_exception(self):
        with self.assertRaises(InvalidJsonError):
            self.obj.verify_json(self.invald_in_json)


if __name__ == '__main__':
        unittest.main()
