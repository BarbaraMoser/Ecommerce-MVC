from app.models.integrations.txt_files_integration import TxtFilesIntegration
from app.utils.string import StringUtils


class FilesIntegrationController:

    def txt_integration(self, value: str):
        if not StringUtils.is_empty_or_is_null(value):
            return TxtFilesIntegration.read_file(value)
