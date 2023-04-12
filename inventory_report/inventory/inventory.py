import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        if report_type not in ["simples", "completo"]:
            raise ValueError("Tipo inválido")

        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = [dict(row) for row in reader]

        if report_type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
