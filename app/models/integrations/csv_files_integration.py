import csv
import xml.etree.ElementTree as ET
from typing import List


class CsvFilesIntegration:
    _ENCODING = 'utf-8'

    @classmethod
    def read_file(cls, file_name: str):
        with open(f'{file_name}.csv', 'r', encoding=cls._ENCODING) as csvfile:
            reader = csv.reader(csvfile)
            return [row for row in reader]

    @classmethod
    def xml_to_csv(cls, file_name: str, item_key: str, list_fields: List[str]):
        tree = ET.parse(f'{file_name}.xml')
        root = tree.getroot()

        new_file = open(f'{file_name}.csv', 'w', encoding=cls._ENCODING)

        csvwriter = csv.writer(new_file)
        file_head = []

        count = 0
        for item in root.findall(item_key):
            key_infos = []
            address_list = []
            if count == 0:
                for i in range(len(list_fields)):
                    file_head.append(item.find(list_fields[i]).tag)
                    csvwriter.writerow(file_head)
                count += 1
            for i in range(len(list_fields)):
                key_infos.append(item.find(list_fields[i]).text)
                csvwriter.writerow(key_infos)
        new_file.close()
        return file_name


# >>>>>>>>>>>>>>>>>>>>>>> EXCECUÇÃO PARA TESTE <<<<<<<<<<<<<<<<<<<<<<<<<

# lendo arquivo csv
files = CsvFilesIntegration.read_file('home')
for file in files:
    print(file)

# convertendo xml em csv
file_name = CsvFilesIntegration.xml_to_csv(
    'schema',
    'Municipio',
    [
        'Codigo',
        'Nome',
        'UF',
        'Região',
        'País',
    ])

files = CsvFilesIntegration.read_file(file_name)
for file in files:
    print(file)
