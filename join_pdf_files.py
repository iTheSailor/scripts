from PyPDF2 import PdfMerger
import os


def join_pdf_files(source_folder, destination_folder, final_name):
    merger = PdfMerger()
    for folder_name, sub_folders, file_names in os.walk(source_folder):
        for file_name in file_names:
            if file_name.endswith('.pdf'):
                pdf_path = os.path.join(folder_name, file_name)
                merger.append(pdf_path)
                print('Appended ' + pdf_path)
    merger.write(destination_folder + '/' + final_name + '.pdf')
    merger.close()
    print('Done.')

source_folder = input('Enter the source folder: ')
destination_folder = input('Enter the destination folder: ')
final_name = input('Enter the name of the joined file: ')

join_pdf_files(source_folder, destination_folder, final_name)

# Path: projects/test_folder/ocv_discovery.py