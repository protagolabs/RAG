import json
import jsonlines
from openai import OpenAI
import torch
import ollama
import re
from datasets import load_dataset, Dataset

# Initialize the LLM client
client = OpenAI(
    base_url='http://localhost:11434/v1',
    api_key='gemma2'
)

def role_answer(prompt, question):
    #prompt = prompt + '\n' + 'Question: ' + question
    response = client.chat.completions.create(
        model='gemma2',
        messages=[{"role": "system", "content": prompt}, {"role": "user", "content": 'Question: ' + question}],
        #messages=[{"role": "system", "content": prompt}],
        max_tokens=1000,
        n=1,
        temperature=0.1,
    )
    answer = response.choices[0].message.content
    
    return answer

# Dictionary containing categories and corresponding prompts
categories = {
    "Definitions and Concepts": "Context: I would like to ask some questions related to definitions and concepts, and I would like the LLM to respond as a professional Lexicographer.\nRole: Lexicographer\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.'and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Events and History": "Context: I would like to ask some questions related to events and history, and I would like the LLM to respond as a professional Historian.\nRole: Historian\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Health and Medicine": "Context: I would like to ask some questions related to health and medicine, and I would like the LLM to respond as a professional Medical Doctor.\nRole: Medical Doctor\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Business and Finance": "Context: I would like to ask some questions related to business and finance, and I would like the LLM to respond as a professional Financial Analyst.\nRole: Financial Analyst\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Products and Services": "Context: I would like to ask some questions related to products and services, and I would like the LLM to respond as a professional Product Manager.\nRole: Product Manager\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Science and Technology": "Context: I would like to ask some questions related to science and technology, and I would like the LLM to respond as a professional Scientist.\nRole: Scientist\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "People and Roles": "Context: I would like to ask some questions related to people and roles, and I would like the LLM to respond as a professional Biographer.\nRole: Biographer\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Geography and Locations": "Context: I would like to ask some questions related to geography and locations, and I would like the LLM to respond as a professional Geographer.\nRole: Geographer\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Education and Academia": "Context: I would like to ask some questions related to education and academia, and I would like the LLM to respond as a professional Educator.\nRole: Educator\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Media and Creative Works": "Context: I would like to ask some questions related to media and creative works, and I would like the LLM to respond as a professional Media Critic.\nRole: Media Critic\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Actions and Processes": "Context: I would like to ask some questions related to actions and processes, and I would like the LLM to respond as a professional Process Engineer.\nRole: Process Engineer\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Community and Society": "Context: I would like to ask some questions related to community and society, and I would like the LLM to respond as a professional Sociologist.\nRole: Sociologist\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Law and Legal Concepts": "Context: I would like to ask some questions related to law and legal concepts, and I would like the LLM to respond as a professional Lawyer.\nRole: Lawyer\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Weather and Environment": "Context: I would like to ask some questions related to weather and environment, and I would like the LLM to respond as a professional Meteorologist.\nRole: Meteorologist\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Food and Nutrition": "Context: I would like to ask some questions related to food and nutrition, and I would like the LLM to respond as a professional Nutritionist.\nRole: Nutritionist\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Spirituality and Religion": "Context: I would like to ask some questions related to spirituality and religion, and I would like the LLM to respond as a professional Theologian.\nRole: Theologian\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "Art and Entertainment": "Context: I would like to ask some questions related to art and entertainment, and I would like the LLM to respond as a professional Art Critic.\nRole: Art Critic\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.\nInstruction: Provide a direct answer to the question asked without requesting further information.",
    "General": "Please answer the question to the best of your ability.\nInstruction: Provide a direct answer to the question asked without requesting further information."
}

# Function to ask a question based on category
def role_answer_by_category(category, question):
    if category in categories:
        prompt = categories[category]
        return role_answer(prompt, question)
    else:
        return "Category not recognized."

def process_role_answer():
    # load and save to datasets
    queries = load_dataset("UKPLab/dapr", "MSMARCO-queries", split="test")

    # Initialize data structure with lists for each column
    new_data = {
        '_id': [],
        'text': [],
        'answers': []
    }

    for query in queries:
        _id, text = query['_id'], query['text']
        answers = {}
        for key in categories:
            prompt = categories[key]
            question = text
            answer = role_answer(prompt, question)
            answers[key] = answer

        # Append data to respective lists
        new_data['_id'].append(_id)
        new_data['text'].append(text)
        new_data['answers'].append(answers)

    # Convert to Huggingface Dataset
    new_dataset = Dataset.from_dict(new_data)
    # Push to Huggingface Hub directly from the Dataset object
    new_dataset.push_to_hub("elricwan/MSMARCO-queries-roleAns", private=False)




if __name__ == "__main__":
    # Example usage
    # category = "Health and Medicine"
    # question = "What are the symptoms and treatment options for diabetes?"
    # answer = ask_question_by_category(category, question)
    # print(answer)
    process_role_answer()
