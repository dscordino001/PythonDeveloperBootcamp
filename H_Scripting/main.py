import PyPDF2

# working with dummy.pdf
with open(".\\dummy.pdf", "rb") as dummy: # rb is to read the binary. need to do this for pdf
    pdfReader = PyPDF2.PdfFileReader(dummy)
    print(pdfReader.numPages) # print the number of pages in the pdf
    print(pdfReader.getPage(0))
    page = pdfReader.getPage(0)
    page.rotateCounterClockwise(180) # rotate the page upside down
    writer = PyPDF2.PdfFileWriter
    writer.addPage(page)
    with open("tilt.pdf", "wb") as file:
        writer.write(file)
