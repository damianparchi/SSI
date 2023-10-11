import pandas as pd
import random

class DatabaseReader:
    def __init__(self, type_file, data_file):
        self.file_type = type_file
        self.file_data = data_file

    file_type = 'iris-type.txt'
    data_type = pd.read_csv(file_type, sep='\t', header=None)
    #lista zawiera pierwsza kolumne wczytanych danych z iris-type.txt
    types = data_type[0].tolist() 

    #z iris.txt do zmiennej data
    #nadajemy kolumnom w ramce danych data nazwy z listy types
    file_data = 'iris.txt'
    data = pd.read_csv(file_data, sep='\t', header=None)
    data.columns = types 
    
    # atrybut o podanym indeksie jest atrybutem "s"
    # na podstawie informacji z pliku iris-type.txt
    def is_attribute(self, index):
        if self.data_type.iloc[index][1] == 's':
            return True
        else:
            return False

    #zwraca nazwe atrybutu na podstawie iris-type.txt
    def name_attribute(self, index):
        return self.data_type.iloc[index][0]

# instancja
database = DatabaseReader('iris.txt', 'iris-type.txt')

# lista unikalnych losowych indeksów atrybutów
num_attributes = len(database.types)
num_to_check = random.randint(1, num_attributes)
random_indices = random.sample(range(num_attributes), num_to_check)

for index in random_indices:
    print(f"Atrybut: {index}:")
    print(f"Czy jest stringiem?: {database.is_attribute(index)}")
    print(f"Nazwa: {database.name_attribute(index)}")