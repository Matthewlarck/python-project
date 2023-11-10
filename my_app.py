from docx import Document

document = Document()

name = 'Matthew'
phone_number = '702-755-5822'
email = 'matthewlarck@gmail.com'

document.add_paragraph(
    'hello')

document.save('cv.docx')