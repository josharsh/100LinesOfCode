from glob import glob
from PyPDF2 import PdfFileMerger

import tkinter as tk
from tkinter import filedialog


def loadFileDialog():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askdirectory()
    return file_path


def pdf_merge(file_path):
    ''' Merges all the pdf files in file_path directory '''
    merger = PdfFileMerger()
    allpdfs = [a for a in glob(f"{file_path}/*.pdf")]
    [merger.append(pdf) for pdf in allpdfs]
    with open("Merged_pdfs.pdf", "wb") as new_file:
        merger.write(new_file)


if __name__ == "__main__":
    print('Select folder')
    file_path = loadFileDialog()
    print('Merging all selected files')
    pdf_merge(file_path)
    print('Merged file')
