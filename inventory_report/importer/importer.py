# from abc import ABC, abstractmethod


# class Importer(ABC):

#     @classmethod
#     @abstractmethod
#     def import_data(cls, path):
#         pass
from abc import ABC, abstractmethod


class Importer(ABC):
    @staticmethod
    @abstractmethod
    def import_data(file_path):
        pass
