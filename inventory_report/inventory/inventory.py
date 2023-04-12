import csv
import json

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        with open(file_path, "r") as file:
            if file_path.endswith(".csv"):
                reader = csv.DictReader(file)
                data = [dict(row) for row in reader]
            elif file_path.endswith(".json"):
                data = json.load(file)
            else:
                raise ValueError(
                    "Tipo de arquivo inválido. Forneça um arquivo CSV ou JSON."
                )
            if report_type == "simples":
                return SimpleReport.generate(data)
            elif report_type == "completo":
                return CompleteReport.generate(data)
            else:
                raise ValueError(
                    "Relatório inválido, forneça 'simples' ou 'completo."
                )
