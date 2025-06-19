# CV Role Recommender & Grader

Python script to analyse CVS (PDF, DOCX, TXT) for suitable job roles via keyword matching. It grades CVS based on essential skills and provides feedback on qualifications and experience.

---

## Features

- **Automatic Role Detection**: Identifies the best-fit role from predefined categories.
- **Keyword Matching & Grading**: Assesses CV alignment with role-specific keywords.
- **Manual Skill Check**: Allows manual skill input for quick role matching.
- **Multi-Format Support**: Reads `.pdf`, `.docx`, `.txt` files.
- **Extensible Profiles**: Easily add roles via `profession_keywords`.

---

## Supported Professions

Includes profiles for:

- Software Developer
- Data Scientist
- Customer Service
- Cyber Security

Each profile contains keywords, experience levels, related roles, and requirements.

---

## Potential Applications

- Recruitment software integration
- Job matching platforms
- Career counselling tools
- ATS enhancement
- Self-assessment for job seekers

---

## Requirements

Install:

```bash
pip install python-docx Pypdf2
```

---

## How to Use

1. **Prepare**: Place CV in specified path or update `file_path`.
2. **Run**: `python main.py`
3. **Choose Mode**:
   - `manual`: Input job title and skills.
   - `automatic`: Program reads CV for best role match.

---

## Example Interaction

### Manual Mode:

```bash
Enter mode (manual/automatic): manual
Profession: data scientist
Your skills (comma-separated)? Python, pandas, machine learning, SQL
Matched skills: ['python', 'machine learning', 'sql']
3 matching skills for a data scientist.
```

### Automatic Mode:

```bash
Enter mode (manual/automatic): automatic
Verified Docx file
Reading...
Software Developer: 10 matches
Data Scientist: 12 matches
Customer Service: 3 matches
Cyber Security: 2 matches
Best role: Data Scientist (12 matches)
Grade: Passed

Feedback:
Experience: entry-level (0-2 years), junior (2-4 years), ...
Related: Data Scientist, Data Analyst, ...
Needs: Bachelor's/Master's in a quantitative field, ...
```

---

## Notes

- Configured for local testing/development.
- Extendable `profession_keywords` for more roles.
- UI planned for the future.

---

## File Structure

```
main.py     # Core script
README.md   # Documentation
```

---

## Contributions

Fork, suggest roles, or submit pull requests for improvements (grading, UI).

---
