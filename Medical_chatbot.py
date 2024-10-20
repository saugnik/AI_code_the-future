import gradio as gr
import pandas as pd
import re
from datetime import datetime

# Sample medical responses for various diseases and conditions, including symptoms, remedies, and medications
medical_responses = {
    "flu": {
        "symptoms": "Common symptoms of flu include fever, cough, sore throat, body aches, and fatigue.",
        "remedies": "For flu, remedies include rest, staying hydrated, and using over-the-counter medications like ibuprofen or acetaminophen.",
        "medications": "Preferred medications include Tamiflu (oseltamivir), ibuprofen, or acetaminophen."
    },
    "fever": {
        "symptoms": "Symptoms of fever can include chills, sweating, headache, muscle aches, and dehydration.",
        "remedies": "For a mild fever, remedies include staying hydrated, resting, and taking acetaminophen or ibuprofen to reduce the fever.",
        "medications": "Preferred medications include acetaminophen or ibuprofen."
    },
    "cough": {
        "symptoms": "Common symptoms associated with cough can include dry throat, fatigue, and discomfort in the chest.",
        "remedies": "Remedies for a cough include drinking warm fluids, honey, herbal teas, and using cough suppressants as needed.",
        "medications": "Preferred medications include dextromethorphan or guaifenesin."
    },
    "chickenpox": {
        "symptoms": "Symptoms of chickenpox include an itchy rash, fever, tiredness, and loss of appetite.",
        "remedies": "Remedies include calamine lotion for itching, oatmeal baths, and antihistamines to relieve symptoms.",
        "medications": "Preferred medications include antihistamines or acetaminophen for fever."
    },
    "diabetes": {
        "symptoms": "Diabetes symptoms may include increased thirst, frequent urination, extreme fatigue, and blurred vision.",
        "remedies": "Management includes regular blood sugar monitoring, a balanced diet with low sugar and carbs, and prescribed medications.",
        "medications": "Preferred medications include metformin or insulin, as prescribed by a doctor."
    },
    "hypertension": {
        "symptoms": "Common symptoms of hypertension may include headaches, shortness of breath, or nosebleeds.",
        "remedies": "Remedies include a low-sodium diet, regular exercise, maintaining a healthy weight, and prescribed medications.",
        "medications": "Preferred medications include ACE inhibitors or diuretics."
    },
    "asthma": {
        "symptoms": "Symptoms of asthma can include wheezing, coughing, chest tightness, and shortness of breath.",
        "remedies": "Management includes avoiding triggers, using inhalers as prescribed, and maintaining a healthy lifestyle.",
        "medications": "Preferred medications include albuterol inhalers and corticosteroids."
    },
    "allergies": {
        "symptoms": "Common allergy symptoms include sneezing, itching, and rashes.",
        "remedies": "Remedies include avoiding allergens, using over-the-counter antihistamines, and consulting a doctor for severe cases.",
        "medications": "Preferred medications include cetirizine or loratadine."
    },
    "heart disease": {
        "symptoms": "Symptoms may include chest pain, shortness of breath, and fatigue.",
        "remedies": "Management includes regular exercise, a heart-healthy diet low in saturated fats, and medication management.",
        "medications": "Preferred medications include statins or beta-blockers."
    },
    "cold": {
        "symptoms": "Symptoms of a cold include a runny or stuffy nose, sore throat, cough, and congestion.",
        "remedies": "Remedies include rest, hydration, and over-the-counter cold medications to alleviate symptoms.",
        "medications": "Preferred medications include phenylephrine or guaifenesin."
    },
    "migraine": {
        "symptoms": "Symptoms of a migraine can include severe headache, nausea, vomiting, and sensitivity to light or sound.",
        "remedies": "For migraines, remedies include resting in a dark room, applying a cold compress, and avoiding triggers.",
        "medications": "Preferred medications include triptans or NSAIDs."
    },
    "anxiety": {
        "symptoms": "Symptoms of anxiety may include excessive worry, restlessness, and physical symptoms like increased heart rate.",
        "remedies": "Management includes relaxation techniques, therapy, and lifestyle changes.",
        "medications": "Preferred medications include SSRIs or benzodiazepines, as prescribed."
    },
    "depression": {
        "symptoms": "Symptoms of depression can include persistent sadness, loss of interest in activities, and changes in appetite.",
        "remedies": "Management includes therapy, support from loved ones, and lifestyle changes.",
        "medications": "Preferred medications include SSRIs or SNRIs."
    },
}

def medical_chatbot_response(user_input):
    user_input_lower = user_input.lower()

    for key in medical_responses:
        if re.search(r'\b' + re.escape(key) + r'\b', user_input_lower):
            symptoms = medical_responses[key]["symptoms"]
            remedies = medical_responses[key]["remedies"]
            medications = medical_responses[key]["medications"]

            # Get the current date
            current_date = datetime.now().strftime("%Y-%m-%d")

            # Create a DataFrame for the output
            output_df = pd.DataFrame({
                "Date": [current_date],  # Add the current date
                "Disease": [key],
                "Symptoms": [symptoms],
                "Remedies": [remedies],
                "Medications": [medications]
            })

            # Save the DataFrame as a CSV file
            output_csv_file = "medical_advice.csv"
            output_df.to_csv(output_csv_file, index=False)

            return symptoms, remedies, medications, output_csv_file

    return "I'm not sure about that. Please consult a healthcare professional for accurate information.", "", "", None

# Create a Gradio interface for the medical chatbot
iface = gr.Interface(
    fn=medical_chatbot_response,
    inputs="text",
    outputs=["text", "text", "text", gr.File(label="Download Advice as CSV")],  # Include gr.File component
    title="Medical Chatbot",
    description="A comprehensive medical chatbot providing basic health information. Please consult a healthcare professional for serious concerns.",
)

# Launch the Gradio interface
iface.launch()
