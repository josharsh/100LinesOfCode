import tkinter as tk
from tkinter import filedialog, Label

from pypdf import PdfWriter, PdfReader
import os

def open_pdf_file(pdf_path_var, button):
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if os.path.splitext(filename)[1].lower() == ".pdf":
        print(f"Selected file: {filename}")
        pdf_path_var.set(filename)
        button.config(text=os.path.basename(filename))
        #Add code here to handle the selected PDF file

def merge_pdfs(pdf1_path, pdf2_path, error_var):
    if not pdf1_path or not pdf2_path:
        print("Please select both PDF files before merging.")
        error_var.set("Please select both PDF files before merging.")
        return

    try:
        pdf1_reader = PdfReader(pdf1_path)
        pdf2_reader = PdfReader(pdf2_path)
    except Exception as e:
        print(f"Error reading PDF files: {e}")
        error_var.set("Error reading PDF files.")
        return

    output_pdf = PdfWriter()
    maxlen = max(len(pdf1_reader.pages), len(pdf2_reader.pages))
    for i in range(maxlen):
        if i < len(pdf1_reader.pages):
            output_pdf.add_page(pdf1_reader.pages[i])
        if i < len(pdf2_reader.pages):
            output_pdf.add_page(pdf2_reader.pages[i])

    output_pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    output_pdf.write(output_pdf_path)
    print(f"PDF files merged successfully into {output_pdf_path}")
    error_var.set("PDF files merged successfully into.")

def main(root, error_var):
    root.title("PDF Merger")
    #root.geometry("900x600")
    root.resizable(0, 0)
    pdf1_path = tk.StringVar()
    pdf2_path = tk.StringVar()
    button_pdf1 = tk.Button(root, text="Click and select a PDF file here", command=lambda: open_pdf_file(pdf1_path, button_pdf1), width=30, height=4)
    button_pdf2 = tk.Button(root, text="Click and select a PDF file here", command=lambda: open_pdf_file(pdf2_path, button_pdf2), width=30, height=4)
    button_merge_pdfs = tk.Button(root, text="Merge PDFs", command=lambda: merge_pdfs(pdf1_path.get(), pdf2_path.get(), error_var), width=60, height=2)
    
    button_pdf1.grid(row=0, column=0)
    button_pdf2.grid(row=0, column=1)
    button_merge_pdfs.grid(row=1, column=0, columnspan=2)
    Label(root, text="Log: ").grid(row=2, column=0,sticky='W')
    Label(root, textvariable=error_var).grid(row=3, column=0, columnspan=2, sticky='W')
    

if __name__ == "__main__":
    root = tk.Tk()  #Use this instead of tk.Tk() for drag and drop (DnD)
    error_var = tk.StringVar(value="No Error")
    main(root, error_var)
    root.mainloop()         #places window on screen and listens for events
