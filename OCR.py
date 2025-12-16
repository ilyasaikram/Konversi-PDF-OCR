import argparse
import ocrmypdf

# Set up argument parser
parser = argparse.ArgumentParser(description="Convert a scanned PDF to a searchable PDF using OCR with high accuracy.")
parser.add_argument('-i', required=True, help="Path to the input PDF file")
parser.add_argument('-o', required=True, help="Path to the output PDF file")
parser.add_argument('--lang', default='eng+ind', help="Language(s) for OCR, e.g., 'eng' or 'eng+ind' (default: 'eng+ind')")
parser.add_argument('--mode', default='redo', choices=['redo', 'force', 'skip'], help="Mode for handling existing text: 'redo' (redo OCR on existing text), 'force' (force OCR by rasterizing), 'skip' (skip pages with text). Default: 'redo'")

# Parse arguments
args = parser.parse_args()

# Input values
input_pdf = args.i
output_pdf = args.o
language = args.lang
mode = args.mode

# Map mode to ocrmypdf parameters
if mode == 'redo':
    ocr_kwargs = {'redo_ocr': True}
elif mode == 'force':
    ocr_kwargs = {'force_ocr': True}
elif mode == 'skip':
    ocr_kwargs = {'skip_text': True}

# Run OCR with settings for high accuracy
ocrmypdf.ocr(
    input_pdf,
    output_pdf,
    deskew=False,         # Set to True if unpaper is installed
    clean=False,          # Set to True if unpaper is installed
    language=language,    # Specify language for accurate recognition
    optimize=0,           # No optimization to avoid lossy compression
    output_type='pdf',    # Output as standard PDF
    progress_bar=False,   # Disable progress bar for script usage
    **ocr_kwargs          # Apply the chosen mode
)

print(f"Searchable PDF successfully created and saved to {output_pdf}")
print(f"Mode used: {mode}. If text is still not selectable, try a different --mode (e.g., 'force'). Test the output in Adobe Acrobat for best results.")