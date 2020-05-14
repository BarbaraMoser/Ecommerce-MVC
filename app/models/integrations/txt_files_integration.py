class TxtFilesIntegration:
    _FILE_NAME = 'cidades.txt'
    _DIR_FILE_TXT = f'C:\\Users\\bazyn\\Projects - 3o Semestre\\Alan\\Ecommerce-MVC\\app\\docs\\{_FILE_NAME}'
    _INFO_NOT_FOUND = 'Info não encontrada.'

    @classmethod
    def read_file(cls, value: str):
        file = open(f'{cls._DIR_FILE_TXT}')
        info = cls._find_info_by_id(cls, value, file)
        if not len(info):
            raise Exception(cls._INFO_NOT_FOUND)
        return info

    def _find_info_by_id(self, id: str, file):
        return [(line) for line in file if id in line]
