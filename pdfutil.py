
from fpdf import FPDF

def createPDF():
    fpdf = FPDF()

    fpdf.add_page()

    fpdf.set_text_color(23,70,23)

    hei = fpdf.h - fpdf.t_margin - fpdf.b_margin
    print(hei,fpdf.h,fpdf.t_margin,fpdf.b_margin)

    fpdf.set_font("Arial",size=50)

    fpdf.text(10,40,txt="HELLO NIG")

    fpdf.image("imgg.jpg",50,50,w=28,h=28)
    fpdf.image("img22.jpg",80,50,w=28,h=28)

    fpdf.add_page()
    fpdf.text(50,50,"asdf")

    fpdf.output("outpdf.pdf")


if __name__ == "__main__":
    createPDF()