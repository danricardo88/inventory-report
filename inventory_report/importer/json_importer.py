# import json
# from inventory_report.importer.importer import Importer


# class Json_Importer(Importer):
#     @classmethod
#     def import_data(cls, path):
#         if ".json" not in path:
#             raise ValueError("Arquivo inválido")

#         with open(path, "r") as file:
#             content = json.load(file)
#             return content
import json
import os

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if not file_path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        if not os.path.isfile(file_path):
            raise FileNotFoundError("Arquivo não encontrado")
        with open(file_path) as json_file:
            data = json.load(json_file)
        return data
