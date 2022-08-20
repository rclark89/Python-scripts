# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 14:01:51 2022

@author: Ross
"""
import os
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import glob

def single_page(path):
    input_pdf = PdfFileReader(path)
    output = PdfFileWriter()
    output.addPage(input_pdf.getPage(0))
    with open(path, "wb") as output_stream:
        output.write(output_stream)
    

def pdf_splitter(path):
    
    #Define variables.
    file_name = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    
    for page in range(pdf.getNumPages()):
        #instantiates PdfFileWriter object
        pdf_writer = PdfFileWriter()
        
        #adds page to this object
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        
        #Generate output file names
        output_filename = r"C:\Users\Ross\Documents\Python Scripts\PDF_splitter\{}_page_{}.pdf".format(
            file_name, page+1)
        
        #Generate output files.
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
            
        print('Created: {}'.format(output_filename))
        
def pdf_merger(output_path, input_paths):
    
    #Instantiate PdfFileMerger object
    pdf_merger = PdfFileMerger()
    #file_handles = []
    
    #for each path in inout_paths, append a new file.
    for path in input_paths:
        pdf_merger.append(path)
    
    #generate 
    with open(output_path, 'wb') as out:
        pdf_merger.write(out)

