import lxml.etree as ET


class TxtFilesIntegration:
    _ENCODING_WINDOWS = 'windows-1252'
    _ENCODING_UTF = 'utf-8'
    _INFO_NOT_FOUND = 'Info não encontrada.'

    @classmethod
    def read_file(cls, file_name: str):
        return open(f'{file_name}.txt', encoding=cls._ENCODING_WINDOWS)

    @classmethod
    def find_info_by_id(cls, file_name: str, search_key: str):
        file = cls.read_file(file_name)
        return [(line) for line in file if search_key in line]

    @classmethod
    def txt_to_xml(cls, file_name: str):
        f = open(f'{file_name}.txt', encoding=cls._ENCODING_WINDOWS)
        lines = f.readlines()
        root = ET.Element(file_name)

        count = 0
        fields = []
        for l in lines:
            elems = l.split(";")
            line = ET.SubElement(root, file_name)

            if count == 0:
                for i in range(len(elems)):
                    fields.append(elems[i].strip('\n'))
                count += 1

            for i in range(len(elems)):
                item = ET.SubElement(line, fields[i])
                item.text = elems[i]

        tree = ET.ElementTree(root)
        tree.write(f'{file_name}.xml', encoding=cls._ENCODING_UTF, pretty_print=True)


# >>>>>>>>>>>>>>>>>>>>>>> EXCECUÇÃO PARA TESTE <<<<<<<<<<<<<<<<<<<<<<<<<
# lendo arquivo txt
file = TxtFilesIntegration.read_file('cidades')
for line in file:
    print(line)

# buscando info por id
file = TxtFilesIntegration.find_info_by_id('cidades', '1101492')
print(file)

# convertendo de txt pra xml
TxtFilesIntegration.txt_to_xml('cidades')
