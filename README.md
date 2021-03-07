# Data sanitizer

## Json Sanitizer to sanitize given json based on different rules(customizable)
    Current version does the following:
     - Loads the json
     - Sanitize it(removing null and empty data)
     
     
## Example:

```input_json = '''{
  "k1" : "v1",
  "k2" : ["v2", "v3", "", {"k21": "v21", "k22": ""}],
  "k3" : {"k4" : "v4", "k5" : ["v5", "v6", null], "k6": {"k7" : "v7", "k8" : ""}},
  "k9" : null
}'''
```

```
output_json = '''{'k1': 'v1', 'k2': ['v2', 'v3', {'k21': 'v21'}], 'k3': {'k4': 'v4', 'k5': ['v5', 'v6'], 'k6': {'k7': 'v7'}}}'''
```
