from typing import List
from xml.etree import ElementTree as et


class XmlFilesIntegration:
    _INFOS: List = []

    @classmethod
    def read_file(cls, file_name: str, key_name: str, list_fields: List[str]):
        file = et.parse(f'{file_name}.xml')
        infos_list = file.findall(key_name)
        for item in infos_list:
            for i in range(len(list_fields)):
                cls._INFOS.append(item.find(list_fields[i]).text)
        return cls._INFOS

    @classmethod
    def find_info_by_id(cls, file_name: str, search_key: str):
        file = et.parse(f'{file_name}.xml')

        for item in file.findall('cidades'):
            if item.find('Código').text == search_key:
                return item.find('Nome').text


# >>>>>>>>>>>>>>>>>>>>>>> EXCECUÇÃO PARA TESTE <<<<<<<<<<<<<<<<<<<<<<<<<
# lendo arquivo xml
# files = XmlFilesIntegration.read_file('cidades', 'cidades', ['Código', 'Nome', 'UF', 'Região', 'País'])
# for file in files:
#     print(file)

# buscando info por id
file = XmlFilesIntegration.find_info_by_id('cidades', '1101492')
print(file)

# file = XmlFilesIntegration.read_file('cidades')
# print(file)
