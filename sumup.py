from PyPDF2 import PdfReader, PdfWriter

def add_password_to_pdf(input_pdf, output_pdf, password):
    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(input_pdf)

    for page in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page])

    pdf_writer.encrypt(password)

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

    print(f"Password has been added to the PDF file: {output_pdf}")
    
def remove_password_from_pdf(input_pdf, output_pdf, password):
    pdf_writer = PdfWriter()
    pdf_reader = PdfReader(input_pdf)
    
    # Check if the PDF is encrypted
    if pdf_reader.is_encrypted:
        # Attempt to decrypt the PDF with the provided password
        if pdf_reader.decrypt(password):
            for page in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page])
            
            with open(output_pdf, 'wb') as out:
                pdf_writer.write(out)
            
            print(f"Password has been removed from the PDF file: {output_pdf}")
        else:
            print("The password provided is incorrect.")
    else:
        print("The PDF file is not encrypted.")


# Example usage
# add_password_to_pdf('input.pdf', 'output.pdf', 'your_password_here')
