# sample_dict = {'key' : 'value'} # Defining a dictionary

# sample_dict = {
#     'colors' : ['Orange', 'Red', 'Blue'],
#     'numbers': [1, 2, 3, 4],
#     'tools' : ['Terraform', 'Ansible', 'Docker', 'Kubernetes'],
#     (1, 2, 3, 4, 5):'a'
#     }
# Access values inside a dict
# print(sample_dict['colors'])
# print(sorted(sample_dict['colors']))
# print(sample_dict['numbers'][-1])

# Altering the values
# sample_dict['numbers'][-1] = 400
# print(sample_dict['numbers']) # The original value is also effected

## Nested Dictionary
# sample_dict = {
#     "employee": {
#         "name": "John",
#         "age" : 30,
#         "city" : "New York"
#     }
# }
# print(sample_dict["employee"]["city"])

## Methods
# sample_dict = {
#     'colors' : ['Orange', 'Red', 'Blue'],
#     'numbers': [1, 2, 3, 4],
#     'tools' : ['Terraform', 'Ansible', 'Docker', 'Kubernetes'],
#     (1, 2, 3, 4, 5):'a'
#     }
# print(sample_dict.keys()) # can access/extract keys
# print(sample_dict.values()) # can access/extract the values
# print(sample_dict.items()) # can access/extract both keys and values

# Adding some more values to dictionaries
sample_dict = {
    'colors' : ['Orange', 'Red', 'Blue'],
    'numbers': [1, 2, 3, 4],
    'tools' : ['Terraform', 'Ansible', 'Docker', 'Kubernetes'],
    (1, 2, 3, 4, 5):'a'
    }
sample_dict['fruits'] = ['Orange', 'banana', 'apple']
print(sample_dict)