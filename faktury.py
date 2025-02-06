import pdfplumber
import pandas as pd
from tkinter import Tk, Button, Listbox, MULTIPLE, END, messagebox
from tkinter.filedialog import askopenfilenames
import re
from datetime import datetime

def extract_data_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
        
        bilet_match = re.search(r"Bilet nr:\s*(\S+)", text)
        faktura_match = re.search(r"Faktura VAT Nr\s*(\S+)", text)
        data_match = re.search(r"Data wystawienia:\s*(\d{2}\.\d{2}\.\d{4})", text)
        
        return [
            bilet_match.group(1) if bilet_match else "Brak",
            faktura_match.group(1) if faktura_match else "Brak",
            data_match.group(1) if data_match else "Brak"
        ]

def process_pdfs(files_list, output_file):
    data = []
    for file in files_list:
        extracted_data = extract_data_from_pdf(file)
        data.append(extracted_data)
    
    df = pd.DataFrame(data, columns=["Bilet nr", "Faktura VAT Nr", "Data wystawienia"])
    df.to_excel(output_file, index=False)
    messagebox.showinfo("Info", f"Przetwarzanie zakończone. Plik zapisano jako: {output_file}")

def browse_files():
    files_selected = askopenfilenames(filetypes=[("Pliki PDF", "*.pdf")])
    files_listbox.delete(0, END)
    for file_path in files_selected:
        files_listbox.insert(END, file_path)

def generate_report():
    files = files_listbox.get(0, END)
    if not files:
        messagebox.showwarning("Ostrzeżenie", "Nie wybrano żadnych plików PDF!")
        return
    
    curr_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"raport_{curr_date}.xlsx"
    process_pdfs(files, output_file)

root = Tk()
root.title("Fakturator")

files_listbox = Listbox(root, width=50, selectmode=MULTIPLE)
files_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

browse_button = Button(root, text="Wybierz pliki PDF", command=browse_files)
browse_button.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

generate_button = Button(root, text="Generuj raport", command=generate_report)
generate_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
