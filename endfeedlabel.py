from reportlab.lib.pagesizes import A4
### get PDF file libraries
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

from constants import bordered_style, non_bordered_style, uppercase


class EndFeedLabel:
    def __init__(self, work_order_id, mfg_end_code, end_code):
        wo=uppercase(work_order_id)
        mec=uppercase(mfg_end_code)
        ec=uppercase(end_code)

        # add Paragraph style ##
        border_style = bordered_style()
        non_border_style = non_bordered_style()

        width, height = A4  # size of the file
        my_path = 'test.pdf'

        c = canvas.Canvas(my_path, pagesize=A4)
        p1 = Paragraph('WORK ORDER NUMBER:', non_border_style)  # add style
        p1.wrapOn(c, 400, 50)  # width , height of Paragraph
        p1.drawOn(c, width - 500, height - 60)  # location of Paragraph

        p11 = Paragraph(wo.get(), border_style)  # add style
        p11.wrapOn(c, 400, 50)  # width , height of Paragraph
        p11.drawOn(c, width - 500, height - 120)  # location of Paragraph

        p2 = Paragraph('MFG END CODE:', non_border_style)  # add style
        p2.wrapOn(c, 400, 50)  # width , height of Paragraph
        p2.drawOn(c, width - 500, height - 190)  # location of Paragraph

        p21 = Paragraph(mec.get(), border_style)  # add style
        p21.wrapOn(c, 400, 50)  # width , height of Paragraph
        p21.drawOn(c, width - 500, height - 250)  # location of Paragraph

        p3 = Paragraph('END CODE:', non_border_style)  # add style
        p3.wrapOn(c, 400, 50)  # width , height of Paragraph
        p3.drawOn(c, width - 500, height - 320)  # location of Paragraph

        p31 = Paragraph(ec.get(), border_style)  # add style
        p31.wrapOn(c, 400, 50)  # width , height of Paragraph
        p31.drawOn(c, width - 500, height - 380)  # location of Paragraph

        c.save()
