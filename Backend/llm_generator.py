from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_NAME = "google/flan-t5-base"

print("Loading medical reasoning model... (first time takes time)")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def generate_text(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)

    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        temperature=0.3
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def analyze_with_llm(report_text, patient_context, structured_data):
    """
    Main AI analysis function used by backend_server
    """

    structured_summary = "\n".join(
        [f"{item['test']}: {item['value']} ({item['status']})" for item in structured_data]
    )

    prompt = f"""
You are a medical report explanation assistant.

Patient Information:
{patient_context}

Lab Results:
{structured_summary}

Explain the results in simple language and give recommendations.
"""

    try:
        analysis = generate_text(prompt)

        return {
            "analysis": analysis,
            "recommendations": [
                {
                    "title": "Consult a doctor",
                    "description": "Always confirm results with a healthcare professional.",
                    "priority": "high"
                }
            ],
            "uncertainties": []
        }

    except Exception as e:
        print("LLM Error:", e)
        return None