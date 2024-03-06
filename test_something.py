from pathlib import Path
import pandas as pd
from zipfile import ZipFile
from pypdf import PdfReader
import variables as v
def test_csv():
    with ZipFile(v.archive) as zip_file:
        f = pd.read_csv(zip_file.open(v.file_directory + v.file_2))
        list_email = f['email'].to_list()
    assert v.user_email in list_email


def test_xlsx():
    with ZipFile(v.archive) as zip_file:
        f = pd.read_excel(zip_file.open(v.file_directory+ v.file_1))
        id_list = f['Id'].to_list()
    assert v.user_id in id_list


def test_pdf():
    with ZipFile(v.archive) as zip_file:
        reader = PdfReader(zip_file.open(v.file_directory + v.file_3))
        text_area = reader.pages[0].extract_text()
    assert v.user_name in text_area