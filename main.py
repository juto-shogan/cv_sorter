from docx import Document
from PyPDF2 import PdfReader
"""
todo list
- create a user input space for straight inplaces
- create another switch case for the profession being applied for 
- create a point system based of criteria checked
- Create a UI when possible 
"""
'''
done-list 
- make a list supported document types
- created a function to read the document type
- make a read docx or pdf function 
- create a set of key words for each profession that is being applied for
- grading system for CVs
- make a switch case for if its A doxc or a pdf
'''



# AI generated code to read a document file (docx or pdf) and return its content.
def get_file_type(file_path, supported_extensions):
    extension_map = {
        '.pdf': 'PDF',
        '.docx': 'DOCX',
        '.txt': 'Text',
        '.doc': 'DOC',
        '.otd': 'OpenDocument',
        '.odt': 'Doc',
    }
    for ext in supported_extensions:
        if file_path.endswith(ext):
            return extension_map.get(ext, 'Unknown')
    return 'Unsupported'

# For Extracting the files content
def read_cv(file_path):
    
    # Reads a document file (docx or pdf) and returns its content.
    file_type = get_file_type(file_path, supported_extensions)
    
    # Check if the file type is supported
    # for docx files
    if file_type == 'DOCX':
        print("Verified it is a Docx file")
        print("Reading the file...")
        
        # Reading the docx file
        doc = Document(file_path)
        content = []
        for para in doc.paragraphs:
            content.append(para.text)
        return '\n'.join(content).lower()
        
    # For Pdfs    
    elif file_type == 'PDF':
        doc = PdfReader(file_path)
        content = []
        for page in doc.pages:
            content.append(page.extract_text())
        return '\n'.join(content).lower()
    
    # For text files
    elif file_type == 'Text':
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content.lower()
    
    # for doc files
    else:
        print('not ready yet')
        
# For checking extracte content against keywords
def cv_checker(content, keywords):
    count = 0
    matched_keywords = []
    
    for keyword in keywords:
        if keyword in content:
            count += 1
            matched_keywords.append(keyword)
    print(f'found {matched_keywords} in CV')
    return count, matched_keywords
        
# Grades based on the keywords and the number of key words found 
def grader(count, keywords):
    no_of_keywords = len(keywords)
    print(f'number of keywords: {no_of_keywords}')
    print(f'number of keywords found: {count}')
    
    if no_of_keywords > count:
        print('failed')
    else:
        if no_of_keywords == count:
            print('passed')
        else:
            print('under consideration')

    


# Test parameters
file_path = r'C:\Users\somto\Desktop\cv_sorter\cvs\Resume.pdf'
supported_extensions = ['.pdf', '.docx', '.txt', '.doc', '.odt']
keyword = ['python', 'tensorflow', 'c++', 'javascript', 'html', 'css', 'sql', 'ruby', 'php', 'machine learning']

if __name__ == "__main__":
    file_type = get_file_type(file_path, supported_extensions)
    content = read_cv(file_path)
    if content:
        count, matched_keywords = cv_checker(content, keyword)
        grader(count, keyword)  
    
# Keywords for different professions
profession_keywords = {
'software_dev_Keywords' : ['python', 'java', 
               'c++', 'javascript', 
               'html', 'css', 'sql', 
               'ruby', 'php',],


'data_science_keywords' : ['python', 'r', 
                         'sql', 'machine learning', 
                         'statistics'],

'customer_service_keywords' : ['customer service', 
                             'communication', 
                             'problem solving', 
                             'teamwork', 'adaptability']}

