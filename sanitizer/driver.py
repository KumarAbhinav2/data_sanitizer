"""
Json Sanitizer to sanitize given json based on different rules(customizable).
Current version does the following:
 - Loads the json
 - Sanitize it(removing null and empty data)
"""
from  traceback import format_exc
from sanitizer.exceptions import InvalidJsonError
from sanitizer.services.services import JsonSanitizerService
from sanitizer.controllers.json_controller import JsonSanitizer

from sanitizer import logger
log = logger.getLogger(__name__)

in_json = '''{
  "k1" : "v1",
  "k2" : ["v2", "v3", "", {"k21": "v21", "k22": ""}],
  "k3" : {"k4" : "v4", "k5" : ["v5", "v6", null], "k6": {"k7" : "v7", "k8" : ""}},
  "k9" : null
}'''

in_json1 = '''{
    "k1": "v1",
    "k2": 
}
'''

def main():
  try:
    service_obj = JsonSanitizerService()
    log.info("Json is getting loaded....")
    service_obj.add_json(in_json)
    obj = JsonSanitizer(service_obj)
    log.info("Initiating json sanitization...")
    print(obj.sanitize())
  except InvalidJsonError:
    log.error(format_exc())
    return "Invalid Json Found", 500
  except Exception:
    log.error(format_exc())
    return "Something went wrong, please check with dev team", 500


if __name__ == '__main__':
  log.info("Initiating the process.....")
  main()