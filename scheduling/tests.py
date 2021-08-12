from django.test import TestCase

# Create your tests here.
import xlrd
# Create your views here.
loc = ('./file.xlsx')
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
 
for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0))