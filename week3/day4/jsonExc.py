import json


def get_salary(dictionary):
   return dictionary['company']['employee']['payable']['salary']


def add_birth_date(dictionary, date):
    dictionary['company']['employee']['birth_date'] = date


def write_dict_to_file(dictionary):
    with open("sample.json", "w") as outfile:
        json.dump(dictionary, outfile, indent=2, sort_keys=True)

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

my_dictionary = json.loads(sampleJson)

print(my_dictionary)
add_birth_date(my_dictionary, '1.1.1993')
print(my_dictionary)
write_dict_to_file(my_dictionary)

