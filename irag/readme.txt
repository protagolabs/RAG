# MSMARCO benchmark

# Dataset: 

questions: around 2000, 
relavant documents: around 4000,
whole documents: around 6000000.

# Goal:

Find the relavant documents from whole documents based on questions.


# Method:

Step 1: 
LLM play different roles to generate answers. Roles cover the categories of the dataset.

categories = {
    "Definitions and Concepts": "Context: I would like to ask some questions related to definitions and concepts, and I would like the LLM to respond as a professional Lexicographer.\nRole: Lexicographer\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.'and 'I do not know.' only, no other information.",
    "Events and History": "Context: I would like to ask some questions related to events and history, and I would like the LLM to respond as a professional Historian.\nRole: Historian\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Health and Medicine": "Context: I would like to ask some questions related to health and medicine, and I would like the LLM to respond as a professional Medical Doctor.\nRole: Medical Doctor\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Business and Finance": "Context: I would like to ask some questions related to business and finance, and I would like the LLM to respond as a professional Financial Analyst.\nRole: Financial Analyst\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Products and Services": "Context: I would like to ask some questions related to products and services, and I would like the LLM to respond as a professional Product Manager.\nRole: Product Manager\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Science and Technology": "Context: I would like to ask some questions related to science and technology, and I would like the LLM to respond as a professional Scientist.\nRole: Scientist\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "People and Roles": "Context: I would like to ask some questions related to people and roles, and I would like the LLM to respond as a professional Biographer.\nRole: Biographer\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Geography and Locations": "Context: I would like to ask some questions related to geography and locations, and I would like the LLM to respond as a professional Geographer.\nRole: Geographer\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Education and Academia": "Context: I would like to ask some questions related to education and academia, and I would like the LLM to respond as a professional Educator.\nRole: Educator\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Media and Creative Works": "Context: I would like to ask some questions related to media and creative works, and I would like the LLM to respond as a professional Media Critic.\nRole: Media Critic\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Actions and Processes": "Context: I would like to ask some questions related to actions and processes, and I would like the LLM to respond as a professional Process Engineer.\nRole: Process Engineer\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Community and Society": "Context: I would like to ask some questions related to community and society, and I would like the LLM to respond as a professional Sociologist.\nRole: Sociologist\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Law and Legal Concepts": "Context: I would like to ask some questions related to law and legal concepts, and I would like the LLM to respond as a professional Lawyer.\nRole: Lawyer\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Weather and Environment": "Context: I would like to ask some questions related to weather and environment, and I would like the LLM to respond as a professional Meteorologist.\nRole: Meteorologist\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Food and Nutrition": "Context: I would like to ask some questions related to food and nutrition, and I would like the LLM to respond as a professional Nutritionist.\nRole: Nutritionist\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Spirituality and Religion": "Context: I would like to ask some questions related to spirituality and religion, and I would like the LLM to respond as a professional Theologian.\nRole: Theologian\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
    "Art and Entertainment": "Context: I would like to ask some questions related to art and entertainment, and I would like the LLM to respond as a professional Art Critic.\nRole: Art Critic\nConstraint: If the question is outside the professional level of the role, please respond with 'I do not know.' and 'I do not know.' only, no other information.",
}

Step 2: 
embedding the generated answers and its questions.
embedding the whole documents.
Find top 1000 similar document.
Use LLM to filter and select 100 document.

Note that the number 1000 and 100 are trade-off between effeiciency and accuracy.

Step 3:
Evaluate the result.
