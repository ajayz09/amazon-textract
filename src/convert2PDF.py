import os
import filetype
from pdf2image import convert_from_path

path = "../documents"
for document in os.listdir(path):
    document = path + '/' + document
    kind = filetype.guess(document)
    if(kind.extension == 'pdf'):
        documentImage = document.replace(".pdf",".jpg")
        pages = convert_from_path(document, 500)
        for page in pages:
            page.save(documentImage, 'JPEG')
        os.remove(document)    