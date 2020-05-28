from app.models.integrations.csv_files_integration import CsvFilesIntegration


class FileConverterFactory:

    @classmethod
    def get_file_converter(cls, initial_format: str, final_format: str, infos_file: dict):
        if initial_format == 'txt' and final_format == 'csv':
            pass
        elif initial_format == 'txt' and final_format == 'xml':
            pass
        elif initial_format == 'xml' and final_format == 'csv':
            return CsvFilesIntegration.xml_to_csv(
                infos_file['file-name'],
                infos_file['item_key'],
                infos_file['list_fields'],
            )
