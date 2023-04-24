import tkinter as tk
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
### get PDF file libraries
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


class EndFeedLabel:
    def __init__(self, work_order_id, mfg_end_code, end_code):
        # add Paragraph style ##
        my_Style = ParagraphStyle('My Para style',
                                  fontName="Times-Roman",
                                  fontSize=30,
                                  fontWeight="bold",
                                  alignment=TA_LEFT,
                                  borderWidth=.5,
                                  borderColor='grey',  # FFFF00',
                                  backColor='white',  # '#F1F1F1',
                                  borderPadding=(10, 20, 20),
                                  leading=20
                                  )
        width, height = A4  # size of the file
        my_path = 'test.pdf'

        c = canvas.Canvas(my_path, pagesize=A4)
        p1 = Paragraph('Work Order Number: &nbsp;&nbsp;&nbsp;' + work_order_id, my_Style)  # add style
        p1.wrapOn(c, 400, 50)  # width , height of Paragraph
        p1.drawOn(c, width - 500, height - 60)  # location of Paragraph

        p2 = Paragraph('Mfg End Code:&nbsp;&nbsp;' + mfg_end_code, my_Style)  # add style
        p2.wrapOn(c, 400, 50)  # width , height of Paragraph
        p2.drawOn(c, width - 500, height - 150)  # location of Paragraph

        p3 = Paragraph('End Code:&nbsp;&nbsp;&nbsp;' + end_code, my_Style)  # add style
        p3.wrapOn(c, 400, 50)  # width , height of Paragraph
        p3.drawOn(c, width - 500, height - 240)  # location of Paragraph

        

        c.save()
