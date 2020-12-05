# from urllib.request import urlopen
# from io import StringIO
# import csv
# data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
# dataFile = StringIO(data)
# csvReader = csv.reader(dataFile)
# dictReader = csv.DictReader(dataFile)
# print(dictReader.fieldnames)
# for row in csvReader:
#     print(row)
# # for row in csvReader:
#     print("The album \""+row[0]+"\" was released in "+str(row[1]))

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content
pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()