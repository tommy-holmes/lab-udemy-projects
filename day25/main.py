import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

new_data = pandas.DataFrame(data_dict)
#new_data.to_csv('squirrel_count.csv')