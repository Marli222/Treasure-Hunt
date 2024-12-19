import json

# JSON list string
json_list = '["Amb1", "Gob"]'

# Convert to Python list
python_list = json.loads(json_list)

print(python_list)  # Output: ['Amb1', 'Gob']

import json

# JSON list string
json_list = '["Amb2"]'

# Convert to Python list
python_list = json.loads(json_list)

print(python_list)  # Output: ['Amb2']
