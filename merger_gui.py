import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

# Global list to store selected PDFs
pdf_files = []

# Function to add PDF to the list
def add_pdf():
    file = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")],
        defaultextension=".pdf"
    )
    if file:
        pdf_files.append(file)
        listbox.insert(tk.END, file.split("/")[-1])  # Show only file name

# Function to merge all added PDFs
def merge_pdfs():
    if len(pdf_files) < 2:
        messagebox.showerror("Error", "Add at least 2 PDF files to merge.")
        return

    output_path = filedialog.asksaveasfilename(
        title="Save Merged PDF As",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )

    if output_path:
        merger = PdfMerger()
        for pdf in pdf_files:
            merger.append(pdf)
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Success", f"Merged PDF saved at:\n{output_path}")
    else:
        messagebox.showwarning("Cancelled", "Save operation cancelled.")

# GUI setup
root = tk.Tk()
root.title("PDF Merger")
root.geometry("500x400")
root.resizable(False, False)

label = tk.Label(root, text="Selected PDFs to Merge:", font=("Arial", 12))
label.pack(pady=10)

# Listbox to display selected PDFs
listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=5)

# Add and Merge Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="+ Add PDF", command=add_pdf, font=("Arial", 11), bg="#3498db", fg="white", width=15)
add_button.grid(row=0, column=0, padx=10)

merge_button = tk.Button(button_frame, text="Merge PDFs", command=merge_pdfs, font=("Arial", 11), bg="#27ae60", fg="white", width=15)
merge_button.grid(row=0, column=1, padx=10)

root.mainloop()