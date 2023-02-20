import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    # Load Excel files to dataframes
    df = pd.read_excel(filepath, sheet_name="Лист1")

    # Create a pdf list for each dataframe
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.add_page()

    # Add first string with a number of invoice
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"Date: {date}")

    pdf.output(f"PDFs/{filename}.pdf")