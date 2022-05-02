from pathlib import Path
from openpyxl import load_workbook
from books.models import Book

def run(path: str):
	wb = load_workbook(Path(path))
	sheet = wb.active
	flag = False
	for row in sheet.iter_rows(values_only=True):
		if flag == False:
			flag = True
			continue
		if row[0] is None:
			break
		new_book = Book(storage=row[0],
						fond=row[1],
						inventory=row[2],
						number=row[3],
						exodus=row[4],
						months=None if row[5] is None else row[5].split(','),
						months_numbers=None if row[6] is None else row[6].split(','),
						special_name=row[7],
						dating=row[8],
						size=row[9],
						book_format=row[10],
						book_type=row[11],
						file_path=row[12],
						handwriting=row[13],
						material=row[14],
						description=row[15],
						additional_info=row[16]
						)
		new_book.save()
