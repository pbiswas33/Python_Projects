# Assuming sumup.py is in the current directory and PyPDF2 is installed

from sumup import remove_password_from_pdf

# Replace 'input.pdf' with the path to your input PDF file
# Replace 'output.pdf' with the path where you want to save the output PDF file
# Replace 'your_password_here' with the password you want to set for the PDF file

remove_password_from_pdf('RechargeBySequence.pdf', 'RechargeBySequence_removed.pdf', 'Qwerty@321')
