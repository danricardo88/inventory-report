from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import Csv_Importer
from inventory_report.importer.json_importer import Json_Importer
from inventory_report.importer.xml_importer import Xml_Importer


report_type = {"simples": SimpleReport, "completo": CompleteReport}


class InventoryReport:
    @classmethod
    def import_data(cls, path):
        if ".csv" in path:
            data = Csv_Importer.import_data(path)
        elif ".json" in path:
            data = Json_Importer.import_data(path)
        elif ".xml" in path:
            data = Xml_Importer.import_data(path)
        else:
            # raise ValueError("Arquivo inválido")
            data = Xml_Importer.import_data(path)

        return report_type[type].generate(data)
