import openpyxl
import os
from django.conf import settings

def get_url_from_excel(service_name, file_name="config.xlsx"):
    """
    Reads URL from config.xlsx based on service_name
    """
    file_path = os.path.join(settings.BASE_DIR, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file {file_path} not found")

    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    for row in sheet.iter_rows(min_row=2, values_only=True):  # skip header
        if row[0] == service_name:
            return row[1]

    raise ValueError(f"Service '{service_name}' not found in {file_name}")
