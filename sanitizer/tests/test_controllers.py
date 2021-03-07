from sanitizer.controllers.json_controller import JsonSanitizer
from sanitizer.services.services import JsonSanitizerService
import unittest
import json
from unittest.mock import patch, Mock


class TestServices(unittest.TestCase):

    def setUp(self) -> None:
        self.service_obj = JsonSanitizerService()
        self.obj = JsonSanitizer(self.service_obj)
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

    def test_rules(self):
        ret = self.obj.rules({'test':'test'})
        self.assertEqual(ret, True)

    def test_rules_false(self):
        ret = self.obj.rules({})
        self.assertEqual(ret, False)

    class JsonSanitizer:
        def _sanitize(self):
            pass

    @patch.object(JsonSanitizer, '_sanitize')
    def test_sanitize(self, mock_object):
        mock_object.side_effect = self.expected
        self.service_obj.get_json = Mock(return_value = json.loads(self.valid_in_json))
        ret = self.obj.sanitize()
        self.assertEqual(ret, json.dumps(self.expected))

    def test__sanitize(self):
        self.service_obj.get_json = Mock(return_value=json.loads(self.valid_in_json))
        ret = self.obj.sanitize()
        self.assertEqual(ret, json.dumps(self.expected))


if __name__ == '__main__':
        unittest.main()
