# tested with python3.7
import sys
# PyPDF2 is deprecated. pypdf is the active successor.
# To install module, run 'python -m pip install pypdf'
from pypdf import PdfReader, PdfWriter

def makeOutputFilename(input_filename, total_page_num, start_page, end_page):
    output_filename_part = f'{start_page}-{end_page}'
    if end_page == total_page_num:
        output_filename_part = output_filename_part + '(end)'
    return f'{input_filename}.{output_filename_part}.pdf'

def write_pdf(pdf_writer, output_filename):
    with open(output_filename, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

def split(input_filename, page_ranges):
    pdf = PdfReader(input_filename)
    total_page_num = len(pdf.pages)
    print(f'total_page_num: {total_page_num}')

    if len(page_ranges) == 0:
        # just to check total page num
        return

    extracted_page_indexes = set()

    for page_range in page_ranges:
        splitted_range = page_range.split('-')
        if len(splitted_range) != 2:
            print(f'page range:{page_range} is invalid')
            exit()

        start_page = int(splitted_range[0])
        end_page = splitted_range[1]
        if end_page == 'end':
            end_page = total_page_num
        end_page = int(end_page)

        if start_page > end_page or end_page > total_page_num:
            print(f'page range:{page_range} is invalid')
            exit()

        pdf_writer = PdfWriter()
        current_page_index = start_page - 1
        end_page_index = end_page - 1
        print(f'extracting {page_range}')
        while (current_page_index <= end_page_index):
            pdf_writer.add_page(pdf.pages[current_page_index])
            extracted_page_indexes.add(current_page_index)
            current_page_index = current_page_index + 1

        output_filename = makeOutputFilename(input_filename, total_page_num, start_page, end_page)
        write_pdf(pdf_writer, output_filename)
    
    if len(extracted_page_indexes) != total_page_num:
        print("[Warning] total extracted pages is less than original total page num")

def main():
    if len(sys.argv) < 2:
        print("To show total page num: python split.py filename")
        print("To split: python split.py filename 1-3 4-end")
        return
    filename = sys.argv[1]
    page_ranges = []
    for i in range(2, len(sys.argv)):
        page_range = sys.argv[i]
        page_ranges.append(page_range)
    split(filename, page_ranges)


if __name__ == '__main__':
    main()
