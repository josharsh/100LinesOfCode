from PyPDF2 import PdfReader, PdfWriter
import math

def create_booklet(input_path, output_path, debug=True):
    """
    Convert a PDF into a booklet format where pages are arranged for duplex printing
    with short-edge flipping. Handles both even and odd page counts correctly.
    
    Args:
        input_path (str): Path to the input PDF file
        output_path (str): Path where the output PDF will be saved
        debug (bool): Whether to print debug information
    """
    # Read the input PDF
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    # Get total number of pages
    total_pages = len(reader.pages)
    
    # For booklet printing, we need a multiple of 4 pages
    remainder = total_pages % 4
    padding_needed = (4 - remainder) if remainder != 0 else 0
    total_needed = total_pages + padding_needed
    
    if debug:
        print(f"Original page count: {total_pages}")
        print(f"Remainder when divided by 4: {remainder}")
        print(f"Padding pages needed: {padding_needed}")
        print(f"Final page count needed: {total_needed}")
    
    # Create a list of all pages
    pages = []
    for i in range(total_pages):
        pages.append(reader.pages[i])
    
    # Create a single blank page if needed
    blank_page = None
    if padding_needed > 0:
        blank_page = writer.add_blank_page(
            width=pages[0].mediabox.width,
            height=pages[0].mediabox.height
        )
        # Add the blank pages to our pages list
        for _ in range(padding_needed):
            pages.append(blank_page)
    
    # Calculate number of sheets
    sheets = total_needed // 4
    
    if debug:
        print(f"Number of sheets: {sheets}")
        print("\nPage arrangement:")
    
    # Create a new writer for the final output
    final_writer = PdfWriter()
    
    # Arrange pages in booklet order
    for sheet in range(sheets):
        # Calculate the page numbers for this sheet
        last_page = total_needed - 1 - (sheet * 2)
        first_page = sheet * 2
        second_page = (sheet * 2) + 1
        second_last_page = total_needed - 2 - (sheet * 2)
        
        if debug:
            print(f"\nSheet {sheet + 1}:")
            print(f"  Front: {last_page + 1} and {first_page + 1}")
            print(f"  Back:  {second_page + 1} and {second_last_page + 1}")
        
        # Add the pages in the correct order to the final writer
        final_writer.add_page(pages[last_page])
        final_writer.add_page(pages[first_page])
        final_writer.add_page(pages[second_page])
        final_writer.add_page(pages[second_last_page])
    
    # Save the output PDF
    with open(output_path, 'wb') as output_file:
        final_writer.write(output_file)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python script.py input.pdf output.pdf")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    try:
        create_booklet(input_path, output_path)
        print("\nBooklet created successfully!")
    except Exception as e:
        print(f"Error creating booklet: {str(e)}")