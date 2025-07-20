from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

# Add your OpenAI key
os.environ["OPENAI_API_KEY"] = "your-api-key"

def analyze_resume(data):
    llm = OpenAI(temperature=0.7)
    prompt = PromptTemplate.from_template("""
    Analyze the following resume and give a score out of 100.
    Give suggestions for improvement too.

    Name: {name}
    Education: {education}
    Experience: {experience}
    Skills: {skills}

    Provide a score and 3 suggestions.
    """)
    input_data = prompt.format(**data)
    return llm.invoke(input_data)
