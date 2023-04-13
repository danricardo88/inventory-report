# import xmltodict
# from inventory_report.importer.importer import Importer


# class Xml_Importer(Importer):
#     @classmethod
#     def import_data(cls, path):
#         if ".xml" not in path:
#             raise ValueError("Arquivo inválido")
#         with open(path, "r") as file:
#             content = xmltodict.parse(file.read())
#             return content["dataset"]["record"]
import os
import xml.etree.ElementTree as ET

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if not file_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        if not os.path.isfile(file_path):
            raise FileNotFoundError("Arquivo não encontrado")
        tree = ET.parse(file_path)
        root = tree.getroot()
        products = []
        for product in root:
            p = {}
            for field in product:
                p[field.tag] = field.text
            products.append(p)
        return products
