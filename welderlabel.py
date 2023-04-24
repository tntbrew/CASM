
from reportlab.lib.pagesizes import A4

### get PDF file libraries
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from constants import bordered_style, non_bordered_style


class WelderLabel:

    def __init__(self, work_order_id, customer_number, plate_code, body_code, mfg_end_code, end_code, tda):
        # add Paragraph style ##
        border_style = bordered_style()
        non_border_style = non_bordered_style()

        width, height = A4  # size of the file
        my_path = 'welder.pdf'

        c = canvas.Canvas(my_path, pagesize=A4)
        p1 = Paragraph('Work Order Number:', non_border_style)  # add style
        p1.wrapOn(c, 400, 50)  # width , height of Paragraph
        p1.drawOn(c, width - 500, height - 60)  # location of Paragraph

        p11 = Paragraph(work_order_id, border_style)  # add style
        p11.wrapOn(c, 400, 50)  # width , height of Paragraph
        p11.drawOn(c, width - 500, height - 120)  # location of Paragraph

        p2 = Paragraph('Customer Number:', non_border_style)  # add style
        p2.wrapOn(c, 400, 50)  # width , height of Paragraph
        p2.drawOn(c, width - 500, height - 190)  # location of Paragraph

        p21 = Paragraph(customer_number, border_style)  # add style
        p21.wrapOn(c, 400, 50)  # width , height of Paragraph
        p21.drawOn(c, width - 500, height - 250)  # location of Paragraph

        p4 = Paragraph('MFG Plate Code:', non_border_style)  # add style
        p4.wrapOn(c, 400, 50)  # width , height of Paragraph
        p4.drawOn(c, width - 500, height - 320)  # location of Paragraph

        p41 = Paragraph(plate_code, border_style)  # add style
        p41.wrapOn(c, 400, 50)  # width , height of Paragraph
        p41.drawOn(c, width - 500, height - 390)  # location of Paragraph

        p5 = Paragraph('Body Code:', non_border_style)  # add style
        p5.wrapOn(c, 400, 50)  # width , height of Paragraph
        p5.drawOn(c, width - 500, height - 460)  # location of Paragraph

        p51 = Paragraph(body_code, border_style)  # add style
        p51.wrapOn(c, 400, 50)  # width , height of Paragraph
        p51.drawOn(c, width - 500, height - 520)  # location of Paragraph

        p6 = Paragraph('MFG End Code:', non_border_style) # add style
        p6.wrapOn(c, 400, 50) # width , height of Paragraph
        p6.drawOn(c, width-500,height-590) # location of Paragraph

        p61 = Paragraph(mfg_end_code, border_style) # add style
        p61.wrapOn(c, 400, 50) # width , height of Paragraph
        p61.drawOn(c, width-500,height-650) # location of Paragraph

        p7 = Paragraph('End Code:', non_border_style)  # add style
        p7.wrapOn(c, 400, 50)  # width , height of Paragraph
        p7.drawOn(c, width - 500, height - 720)  # location of Paragraph

        p71 = Paragraph(end_code, border_style)  # add style
        p71.wrapOn(c, 400, 50)  # width , height of Paragraph
        p71.drawOn(c, width - 500, height - 780)  # location of Paragraph

        c.save()
