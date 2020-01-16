import json
with open('Thailand_2012.json', encoding = 'utf16') as file:
    data = json.load(file)

first_dict = data[0]

# Extracting specific keys from the dictionary of first entry
entry_one = dict((x, first_dict[x]) for x in ['country', 'year', 'best'] if x in first_dict)
print(entry_one)
