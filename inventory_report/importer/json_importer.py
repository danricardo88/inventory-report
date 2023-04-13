import json
from inventory_report.importer.importer import Importer


class Json_Importer(Importer):
    @classmethod
    def import_data(cls, path):
        if ".json" not in path:
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            content = json.load(file)
            return content
