import pdfplumber

# Open the PDF file
with pdfplumber.open('example.pdf') as pdf:
    # Iterate over each page in the PDF
    for page in pdf.pages:
        # Extract text from the page
        text = page.extract_text()

        # Print the extracted text
        print(text)
