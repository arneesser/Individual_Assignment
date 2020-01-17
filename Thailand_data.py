import json
with open('Thailand_data.json', encoding = 'utf16') as file:
    data = json.load(file)

# Extracting specific keys from the dictionary of first entry
entry_one = data[0]
first_dict = dict((x, entry_one[x]) for x in ['country', 'year', 'best'] if x in entry_one)

# For Loop that creates a list of dictionaries with specified keys
good_data = []
for entry in data:
    dictionary = dict((x, entry[x]) for x in ['country', 'year', 'best', 'high', 'low'] if x in entry)
    good_data.append(dictionary)

# Transferring contents to .csv file 
with open('Thailand_data.csv', 'w') as file:
    file.write('Country, Year, Best, High, Low \n')
    for line in good_data:
        file.write(f'{line["country"]},{line["year"]},{line["best"]},{line["high"]},{line["low"]}\n')
