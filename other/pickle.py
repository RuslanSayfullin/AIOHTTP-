import pickle

# take user input to take the amount of data
number_of_data = int(input('Enter the number of data: '))
data = []

# take input of the data
for i in range(number_of_data):
    raw = input(f'Enter data {i} : ')
    data.append(raw)

# save input
with open('important', 'w') as file:
    pickle.dump(data, file)
