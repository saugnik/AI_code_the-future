Youtube link if you want to see the code workings =https://youtu.be/3f7_KANOzkY

Participated for: AI-Powered Virtual Health Assistant
problem statement: Challenge Description: In remote areas, patients face challenges accessing healthcare due to geographical limitations and lack of medical personnel. There is a need for an AI-powered virtual health assistant capable of providing preliminary consultations, answering health-related queries, and guiding patients on when to seek further medical assistance. This solution will help bridge the healthcare gap for underserved populations. Users: Patients in remote areas needing medical advice, healthcare providers managing large caseloads, and administrators seeking to improve access to healthcare services. Expected Outcomes: An AI assistant that can provide accurate, basic medical advice, reduce patient dependency on in-person visits, and offer data-driven insights to healthcare providers about patient needs. Potential Impact: Improved healthcare access for remote populations, reduced burden on healthcare providers, and scalable solutions that can be adapted for various regions and medical needs



Medical Chatbot
Overview:
The Medical Chatbot is a simple application designed to provide users with information about various diseases, their symptoms, remedies, and preferred medications. This chatbot uses a Gradio interface for easy interaction and provides a downloadable CSV file with the user's query details.

Features:
Disease Information: Users can inquire about common diseases.
Symptoms & Remedies: The chatbot provides symptoms and suggested remedies for various conditions.
Preferred Medications: Users can also receive information on medications associated with specific diseases.
CSV Download: After each query, users can download a CSV file containing the date of the inquiry, the disease queried, symptoms, remedies, and medications.
Technologies Used
Python: The core programming language for the chatbot.
Gradio: A library for building user interfaces for machine learning models.
Pandas: Used for data manipulation and to create the CSV file.
Regular Expressions: To match user queries with disease names.
Installation:
Clone this repository to your local machine:

bash
Copy code
git clone <repository-url>
cd medical-chatbot
Install the required Python libraries:

bash
Copy code
pip install gradio pandas
Usage
Run the chatbot script:

bash
Copy code
python medical_chatbot.py
Open your web browser and go to http://localhost:7860 to interact with the chatbot.

Type your query in the input box (e.g., "What are the symptoms of flu?") and press Enter.

Review the chatbot's response, which includes symptoms, remedies, and preferred medications.

Download the CSV file for your records.

Example Queries
"What are the symptoms of fever?"
"Tell me about cough remedies."
"What medications are available for flu?"
Additional Diseases Included for now will add if needed:
Flu
Fever
Cough
Chickenpox
Diabetes
Hypertension
Asthma
Allergies
Heart Disease
Cold
Migraine
Anxiety
Depression
Notes
This chatbot is not a substitute for professional medical advice. Always consult a healthcare professional for serious health concerns.
The responses provided by the chatbot are based on predefined data and should be used for informational purposes only.
