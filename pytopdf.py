from fpdf import FPDF
import torch

class PDF(FPDF):

    def __init__(self,pdf_name) -> None:
        self.pdf_name = pdf_name
        
        self.fpdf = FPDF()
        self.fpdf.add_page()
        self.use_height = self.fpdf.h - self.fpdf.t_margin - self.fpdf.b_margin
        self.use_width = self.fpdf.w - self.fpdf.l_margin - self.fpdf.r_margin

        self.img_height = 30
        self.img_width = 30

        print(f'usable height = {self.use_height} , width = {self.use_width}')

    def print(self,input_para,w=0,h=0,x_increment=5,y_increment=5):
        
        
        if w == 0 and h == 0:
            w,h = self.img_width,self.img_height

        #checking if the length of the image when put on the pdf will cross the margin
        if self.fpdf.get_y() + h >= self.use_height:
            self.fpdf.add_page() #adding a page if the end of the page is reached
        
        #checking if the width is reached
        if self.fpdf.get_x() + w >= self.use_width: 
            self.fpdf.set_x(self.fpdf.l_margin) #setting the x value to 0 i.e to the left margin
            self.fpdf.set_y(self.fpdf.get_y()+h+y_increment) #setting the y value to left margin + 35

        ## First we'll create for the image printing
        x,y = self.fpdf.get_x(),self.fpdf.get_y()
        self.fpdf.image(input_para,x,y,w,h)
        self.fpdf.set_x(x+w+x_increment)
        # self.fpdf.set_y(y+30)

        print(f'value of x = {self.fpdf.get_x()} , y = {self.fpdf.get_y()}')

    def close(self):
        self.fpdf.output(self.pdf_name)
        