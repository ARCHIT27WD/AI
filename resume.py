import openai

# OpenAI API key
api_key = 'your_openai_api_key'

# Function to call OpenAI API with the prompt
def parse_resume(resume_text):
    prompt = f"""
    You are an AI that parses resumes. Given the text of a resume, convert its content into the following JSON format:

    {{
      "name": "Full Name",
      "contact_information": {{
        "email": "Email Address",
        "phone": "Phone Number",
        "address": "Full Address"
      }},
      "summary": "Professional Summary",
      "experience": [
        {{
          "job_title": "Job Title",
          "company": "Company Name",
          "location": "Location",
          "start_date": "Start Date",
          "end_date": "End Date",
          "responsibilities": [
            "Responsibility 1",
            "Responsibility 2",
            ...
          ]
        }},
        ...
      ],
      "education": [
        {{
          "degree": "Degree",
          "institution": "Institution Name",
          "location": "Location",
          "start_date": "Start Date",
          "end_date": "End Date"
        }},
        ...
      ],
      "skills": [
        "Skill 1",
        "Skill 2",
        ...
      ],
      "certifications": [
        {{
          "name": "Certification Name",
          "institution": "Institution Name",
          "date": "Date Obtained"
        }},
        ...
      ],
      "projects": [
        {{
          "name": "Project Name",
          "description": "Project Description",
          "technologies": [
            "Technology 1",
            "Technology 2",
            ...
          ]
        }},
        ...
      ]
    }}

    Here is the resume text:

    {resume_text}

    Provide the parsed JSON output below:
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500
    )

    return response.choices[0].text.strip()

# Example resume text
resume_text = """
John Doe
Email: john.doe@example.com
Phone: 123-456-7890
Address: 123 Main St, Anytown, USA

Summary:
Experienced software engineer with a strong background in developing scalable applications and working in dynamic environments.

Experience:
Software Engineer
Tech Solutions Inc., New York, NY
June 2018 - Present
- Developed web applications using Python and Django.
- Collaborated with cross-functional teams to deliver projects on time.
- Implemented RESTful APIs for seamless data integration.

Education:
Bachelor of Science in Computer Science
University of Somewhere, Somewhere, USA
September 2014 - May 2018

Skills:
- Python
- Django
- REST APIs
- JavaScript
- React

Certifications:
Certified Python Developer
Python Institute, June 2019

Projects:
Resume Parser
Developed an automated resume parsing tool using NLP techniques.
Technologies: Python, spaCy
"""

# Call the function and print the output
parsed_resume_json = parse_resume(resume_text)
print(parsed_resume_json)
