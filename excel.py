import xlsxwriter

outWorkbook = xlsxwriter.Workbook("WPM.xlsx")
outSheet = outWorkbook.add_worksheet()

names = ["A", "B", "C"]
values = [70, 82, 71]

outSheet.write("A1", "Names")
outSheet.write("B1", "Score")

for item in range(len(names)):
    outSheet.write(item+1, 0, names[item])
    outSheet.write(item+1, 1, values[item])

outWorkbook.close()