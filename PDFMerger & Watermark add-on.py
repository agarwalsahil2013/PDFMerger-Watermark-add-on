import PyPDF2
import os
    
pdf_loc = input("Hi there! Please paste your folder location where all PDF's are located: ")

#Printing files which needs to merge
user_location = os.listdir(f"{pdf_loc}")
for i in user_location:
  if os.path.splitext(i)[-1] == ".pdf": 
    print(f"\nFile extracted by our system are : {i}")
  else:
    print(f"\nGotcha!! {i} doesn't have .pdf file format. So, we are excluding from merger")
user_permission = input("\nDo you want to process (Y/N): ")

# Function to combine all PDF into One
def pdf_combiner(pdf_list, source): 
  merger = PyPDF2.PdfFileMerger()
  for pdf in pdf_list:
    if os.path.splitext(pdf)[-1] == ".pdf":
      merger.append(f"{source}/{pdf}")
  merger.write(f"{source}/CombinedAllPDF.pdf")

# Combining file based on user response
if user_permission.upper() == "Y":
  pdf_combiner(user_location,pdf_loc)
  print("\nYour CombinedAllPDF.pdf file is ready. Please look into your directory")
elif user_permission.upper() == "N":
  print("\nPlease remove the file which you don't want to merge and run again")

# Add-on functionality --> Watermark 
user_watermark = input("\nDo you want to attach watermark to each page?(Y/N): ")

if user_watermark.upper() == "Y":
  wtr_file_loc = input("\nPlease provide a file location contaning your filename here: ")

  template = PyPDF2.PdfFileReader(open(f'{pdf_loc}/CombinedAllPDF.pdf','rb'))
  watermark = PyPDF2.PdfFileReader(open(f'{wtr_file_loc}','rb'))
  output = PyPDF2.PdfFileWriter()

  for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open(f"{pdf_loc}/watermarked_output.pdf", 'wb') as f:
      output.write(f)
  print("\nHurray!! Your watermark on each page has been completed successfully.")
else:
  print("\nFine!! It was just an add-on. See you next time.")
