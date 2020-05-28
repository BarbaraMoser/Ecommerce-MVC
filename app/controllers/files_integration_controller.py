from app.models.integrations.csv_files_integration import CsvFilesIntegration
from app.models.integrations.txt_files_integration import TxtFilesIntegration
from app.models.integrations.xml_files_integration import XmlFilesIntegration
from app.utils.string import StringUtils


class FilesIntegrationController:

    def txt_reader(self, value: str):
        if not StringUtils.is_empty_or_is_null(value):
            return TxtFilesIntegration.read_file(value)

    def xml_reader(self):
        try:
            return XmlFilesIntegration.read_file()
        except:
            raise Exception('Impossible read this file.')

    def csv_converter(self, file_name: str):
        try:
            if not StringUtils.is_empty_or_is_null(file_name):
                return CsvFilesIntegration.xml_to_csv(file_name)
        except:
            raise Exception('Impossible read this file.')
