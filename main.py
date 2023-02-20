import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Лист1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf")