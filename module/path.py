import os.path


MAIN = os.path.dirname(os.path.dirname(__file__))
DATA = os.path.join(MAIN, "data")
RESOURCES = os.path.join(MAIN, "resources")

DATA_FILES = os.listdir(DATA)

ARCHIVE = os.path.join(RESOURCES, "pack_zip.zip")
EXTRACTED_CSV = os.path.join(RESOURCES, "csv.csv")
EXTRACTED_PDF = os.path.join(RESOURCES, "pdf.pdf")
EXTRACTED_XLSX = os.path.join(RESOURCES, "xlsx.xlsx")