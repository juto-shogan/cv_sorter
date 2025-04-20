from docx import Document
from PyPDF2 import PdfReader
"""
todo list
- Create a UI when possible 
"""
'''
done-list 
- make a list supported document types
- created a function to read the document type
- create another switch case for the profession being applied for (fucntion to determine the profession )
- make a read docx or pdf function 
- create a set of key words for each profession that is being applied for
- grading system for CVs
- make a switch case for if its A doxc or a pdf
- create a user input space for straight inplaces
- create a point system based of criteria checked
'''

# AI assisted code to read a document file (docx or pdf) and return its content.
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
    # print(f'found {matched_keywords} in CV')
    
    return count, matched_keywords
            
# for checking what role the CV is best suited for
def determine_role(content):
    max_matches = 0
    best_role = None
    best_role_details = None

    # Iterate through all professions in profession_keywords
    for role, details in profession_keywords.items():
        keywords = details['keywords']
        count, _ = cv_checker(content, keywords)  # Use cv_checker to count matches
        print(f"Role: {role}, Matches: {count}")

        # Update the best role if this role has more matches
        if count > max_matches:
            max_matches = count
            best_role = role
            best_role_details = details

    if best_role:
        print(f"The most suitable role for this CV is: {best_role} with {max_matches} matches.")
        return best_role, best_role_details  # Return both the role and its details
    else:
        print("No suitable role found for this CV.")
        print('Not suitable for the job')
        return None, None  # Return None for both if no role is found

# Grades based on the keywords and the number of key words found 
def grader(count, role_details):
    keywords = role_details['keywords']
    no_of_keywords = len(keywords)
    print(f'number of keywords: {no_of_keywords}')
    print(f'number of keywords found: {count}')
    
    if no_of_keywords / 2 > count:
            print('Grade: Failed')
    else:
        if no_of_keywords == count:
            print('Grade: Passed')
        else:
                ('Grade: Under consideration')

    # Provide additional feedback
    print("\nAdditional Feedback:")
    print(f"Experience Levels: {', '.join(role_details['experience_levels'])}")
    print(f"Related Roles: {', '.join(role_details['related_roles'])}")
    print(f"Potential Needs: {', '.join(role_details['potential_needs'])}")

# AI assisted code to help with manual checking criteria against keywords
def manual_check(job_title):
    # Map job titles to their corresponding keywords
    job_keywords_map = {
        'software developer': profession_keywords['software_dev_Keywords'],
        'data scientist': profession_keywords['data_science_keywords'],
        'customer service': profession_keywords['customer_service_keywords'],
        'cyber security': profession_keywords['cyber_security_keywords']
    }

    # Check if the job title exists in the map
    if job_title in job_keywords_map:
        role_details = job_keywords_map[job_title]
        keywords = job_keywords_map[job_title]

        # Ask the user to input their skills
        user_skills = input("Enter your skills (comma-separated): ").lower().split(',')
        matched_skills = [skill.strip() for skill in user_skills if skill.strip() in keywords]
        print(f"Matched skills: {matched_skills}")

        # Provide feedback
        if matched_skills:
            print(f"You have {len(matched_skills)} matching skills for the {job_title} role.")
        else:
            print(f"No matching skills found for the {job_title} role.")
        
        # Additional feedback
        print("\nAdditional Feedback:")
        print(f"Experience Levels: {', '.join(role_details['experience_levels'])}")
        print(f"Related Roles: {', '.join(role_details['related_roles'])}")
        print(f"Potential Needs: {', '.join(role_details['potential_needs'])}")
        
    else:
        print("Job title not recognized. Please try again.")

# Keywords for different professions
profession_keywords = {
    'software_dev_Keywords': {
        'keywords': ['python', 'java', 'c++', 'javascript', 'html', 'css', 'sql', 'ruby', 'php', 'agile', 'scrum', 'restful APIs', 'microservices', 'devops', 'git', 'docker', 'kubernetes'],
        'experience_levels': ['entry-level (0-2 years)', 'junior (2-4 years)', 'mid-level (4-7 years)', 'senior (7+ years)', 'lead (10+ years)'],
        'related_roles': ['Software Engineer', 'Web Developer', 'Backend Developer', 'Frontend Developer', 'Full-Stack Developer', 'Mobile Developer', 'Application Developer'],
        'potential_needs': ['Bachelor\'s degree in Computer Science or related field', 'Strong problem-solving skills', 'Experience with specific frameworks (e.g., React, Angular, Spring, Django)', 'Understanding of software development lifecycle']
    },
    'data_science_keywords': {
        'keywords': ['python', 'r', 'sql', 'machine learning', 'statistics', 'data analysis', 'data visualization', 'big data', 'deep learning', 'natural language processing (NLP)', 'time series analysis', 'statistical modeling', 'etl'],
        'experience_levels': ['entry-level (0-2 years)', 'junior (2-4 years)', 'mid-level (4-7 years)', 'senior (7+ years)', 'lead (10+ years)'],
        'related_roles': ['Data Scientist', 'Data Analyst', 'Machine Learning Engineer', 'Business Analyst', 'Data Engineer', 'Research Scientist'],
        'potential_needs': ['Bachelor\'s or Master\'s degree in a quantitative field (e.g., Statistics, Mathematics, Computer Science)', 'Experience with data manipulation libraries (e.g., pandas, numpy)', 'Experience with visualization tools (e.g., matplotlib, seaborn, Tableau)', 'Strong analytical and problem-solving skills']
    },
    'customer_service_keywords': {
        'keywords': ['customer service', 'communication', 'problem solving', 'teamwork', 'adaptability', 'active listening', 'empathy', 'conflict resolution', 'phone etiquette', 'email communication', 'crm', 'customer satisfaction'],
        'experience_levels': ['entry-level (0-2 years)', 'associate (1-3 years)', 'specialist (3-5 years)', 'senior (5+ years)', 'manager (7+ years)'],
        'related_roles': ['Customer Service Representative', 'Customer Support Specialist', 'Account Manager', 'Client Relations Manager', 'Help Desk Agent'],
        'potential_needs': ['High school diploma or equivalent', 'Excellent verbal and written communication skills', 'Ability to remain calm under pressure', 'Strong interpersonal skills']
    },
    'cyber_security_keywords': {
        'keywords': ['network security', 'firewall', 'encryption', 'penetration testing', 'incident response', 'linux', 'information security', 'vulnerability assessment', 'security analysis', 'ids/ips', 'siem', 'risk management', 'compliance'],
        'experience_levels': ['entry-level (0-2 years)', 'junior (2-4 years)', 'security analyst (3-6 years)', 'security engineer (5-8 years)', 'security architect (7+ years)', 'security manager (10+ years)'],
        'related_roles': ['Cybersecurity Analyst', 'Security Engineer', 'Security Consultant', 'Information Security Analyst', 'Penetration Tester', 'Security Architect', 'Security Manager'],
        'potential_needs': ['Bachelor\'s degree in Computer Science, Cybersecurity, or related field', 'Relevant certifications (e.g., CompTIA Security+, CISSP, CEH)', 'Understanding of security principles and best practices', 'Experience with security tools and technologies']
    },
    'standard_keywords': {
        'keywords': ['communication', 'teamwork', 'problem solving', 'adaptability', 'leadership', 'time management', 'critical thinking', 'creativity', 'attention to detail', 'interpersonal skills', 'organization', 'initiative', 'professionalism', 'collaboration'],
        'experience_levels': ['applicable across all experience levels'],
        'related_roles': ['relevant to virtually all roles'],
        'potential_needs': ['demonstrated ability in relevant situations']
    }
}

# Test parameters
file_path = r'C:\Users\somto\Desktop\cv_sorter\cvs\Resume.docx'
supported_extensions = ['.pdf', '.docx', '.txt', '.doc', '.odt']
job_title = ['software developer', 'data scientist', 'customer service', 'cyber security']


if __name__ == "__main__":
    moder = input("Enter the mode you want for application, manual or automatic: ")

    # if the user wants to use the pipeline
    if moder == 'manual':
        job_title = input("What profession are you applying for? ").lower()
        manual_check(job_title)

    elif moder == 'automatic' or moder == 'auto':
        file_type = get_file_type(file_path, supported_extensions)
        content = read_cv(file_path)
        if content:
            best_role, role_details = determine_role(content) # Capture both returned values
            if best_role:
                print(f"Best role determined: {best_role}")
                count, matched_keywords = cv_checker(content, role_details['keywords'])
                grader(count, role_details)
        else:
            print("Could not read the content of the file.")
    else:
        print("Invalid mode selected. Please choose 'manual' or 'automatic'.")