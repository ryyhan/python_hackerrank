from fpdf import FPDF

class PDF():
    def __init__(self,name):
        self._pdf=FPDF()
        self._pdf.add_page()
        self._pdf.set_font("times",style="BIU",size=45)
        self._pdf.cell(0,50,"CS50 Shirtificate",new_x="LMARGIN",new_y="NEXT",align="C")
        self._pdf.image("shirtificate.png",w=self._pdf.epw)
        self._pdf.set_font_size(40)
        self._pdf.set_text_color(219, 255, 244)
        self._pdf.text(x=48,y=150,txt=f"{name} took CS50")

    def write(self,name):
        self._pdf.output(name)

def get_name():
    name=input("Enter your name : ")
    return name

pdf=PDF(get_name())
pdf.write("shirtificate.pdf")