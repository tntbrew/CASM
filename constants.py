from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle

FONT_SIZE = font = "Arial 13 "
USER_ACCESS_CODES = ["Operator", "Can Maker", "Admin"]
BACKGROUND = 'khaki'
BUTTON_BACKGROUND = 'pale green'


def bordered_style():
    my_Style = ParagraphStyle('My Para style',
                              fontName="Helvetica-Bold",
                              fontSize=25,
                              alignment=TA_CENTER,
                              borderWidth=.5,
                              borderColor='grey',  # FFFF00',
                              backColor='white',  # '#F1F1F1',
                              borderPadding=(10, 20, 20),
                              leading=20
                              )
    return my_Style


def non_bordered_style():
    my_Style1 = ParagraphStyle('My Para style',
                               fontName="Helvetica",
                               fontSize=30,
                               alignment=TA_CENTER,
                               borderWidth=0,
                               borderColor='grey',  # FFFF00',
                               backColor='white',  # '#F1F1F1',
                               borderPadding=(10, 20, 20),
                               leading=20
                               )
    return my_Style1
