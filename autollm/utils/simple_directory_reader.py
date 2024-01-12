from autollm.utils.markdown_reader import MarkdownReader
from autollm.utils.pdf_reader import LangchainPDFReader
from llama_index.readers.file.base import BaseFileReader
from llama_index.schema import Document


class SimpleDirectoryReader(BaseFileReader):
    def __init__(
        self,
        input_dir: str,
        exclude_hidden: bool = True,
        file_extractor: dict = None,
        input_files: list = None,
        filename_as_id: bool = True,
        recursive: bool = True,
        required_exts: list = None,
        **kwargs
    ):
        super().__init__(
            input_dir=input_dir,
            exclude_hidden=exclude_hidden,
            file_extractor=file_extractor,
            input_files=input_files,
            filename_as_id=filename_as_id,
            recursive=recursive,
            required_exts=required_exts,
            **kwargs
        )

    def load_data(self, show_progress: bool = True) -> list:
        documents = []
        for file_path in self.get_file_paths():
            ext = self.get_file_extension(file_path)
            if ext in self.file_extractor:
                reader = self.file_extractor[ext]
                doc = reader.read(file_path)
                if doc:
                    documents.append(doc)
        return documents
