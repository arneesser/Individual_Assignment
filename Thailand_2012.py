import json
with open('Thailand_2012.json', encoding = 'utf16') as file:
    data = json.load(file)

entry_one = data[0]
Headers = ['Country', 'Year', 'Best estimate of deaths']
# Extracting specific keys from the dictionary of first entry
first_dict = dict((x, entry_one[x]) for x in ['country', 'year', 'best'] if x in entry_one)
small_data = []

# For Loop that creates a list of dictionaries with specified keys
for entry in data:
    dictionary = dict((x, entry[x]) for x in ['country', 'year', 'best'] if x in entry)
    small_data.append(dictionary)


# Transferring contents to .csv file 
with open('Thailand_2012.csv', 'w') as file:
    file.write('Country, Year, Best estimate of deaths\n')
    for line in small_data:
        file.write(f'{line["country"]},{line["year"]},{line["best"]}\n')
