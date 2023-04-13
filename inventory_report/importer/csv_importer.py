# import csv
# from inventory_report.importer.importer import Importer


# class Csv_Importer(Importer):
#     @classmethod
#     def import_data(cls, path):
#         if ".csv" not in path:
#             raise ValueError("Arquivo inválido")
#         with open(path, "r") as file:
#             content = csv.DictReader(file, delimiter=",", quotechar='"')
#             return list(content)
import csv
import os

from inventory_report.importer.importer import Importer
# from inventory_report.reports.inventory_simples_report import SimpleReport


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if not file_path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        if not os.path.isfile(file_path):
            raise FileNotFoundError("Arquivo não encontrado")
        with open(file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            products = [dict(row) for row in reader]
        return products
