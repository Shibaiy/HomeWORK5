from pathlib import Path
import pandas as pd
from zipfile import ZipFile
from pypdf import PdfReader
def test_csv():
    with ZipFile(str(Path('./tmp/test_archive.zip'))) as zip_file:
        f = pd.read_csv(zip_file.open('tmp/csv_test.csv'))
        list_email = f['email'].to_list()
        assert 'payton.luettgen@gmail.com' in list_email


def test_xlsx():
    with ZipFile(str(Path('./tmp/test_archive.zip'))) as zip_file:
        f = pd.read_excel(zip_file.open('tmp/xlsx_test.xlsx'))
        id_list = f['Id'].to_list()
        print(id_list)
        assert 8642 in id_list


def test_pdf():
    with ZipFile(str(Path('./tmp/test_archive.zip'))) as zip_file:
        reader = PdfReader(zip_file.open('tmp/PDF-3.pdf'))
        text_area = reader.pages[0].extract_text()
        assert 'Максим Шибаев' in text_area