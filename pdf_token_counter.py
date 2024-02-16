import sys
import tiktoken
import PyPDF2

def count_tokens_in_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)

        # Initialize an empty string to hold the PDF content
        pdf_content = ''

        # Loop through each page in the PDF and extract the text
        for page in pdf_reader.pages:
            pdf_content += page.extract_text()

    # Get the encoding
    enc = tiktoken.get_encoding("cl100k_base")

    # Tokenize the PDF content
    tokens = enc.encode(pdf_content)

    # Return the number of tokens
    return len(tokens)

# Get the path to the PDF file from the command line arguments
pdf_path = sys.argv[1]

# Call the function with the command line provided PDF file
print(count_tokens_in_pdf(pdf_path))