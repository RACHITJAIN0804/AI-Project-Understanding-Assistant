class ProjectAssistantException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class FileSaveError(ProjectAssistantException):
    pass


class FileExtractionError(ProjectAssistantException):
    pass


class InvalidRepositoryError(ProjectAssistantException):
    pass



class RepositoryReadError(ProjectAssistantException):
    pass


class PromptGenerationError(ProjectAssistantException):
    pass


class AIServiceError(ProjectAssistantException):
    pass


class ConfigurationError(ProjectAssistantException):
    pass


class FileValidationError(ProjectAssistantException):
    pass


class UnsupportedFileTypeError(ProjectAssistantException):
    pass