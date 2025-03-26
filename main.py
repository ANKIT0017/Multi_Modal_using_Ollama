import json
import os
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

# Load Models
aaditya = OllamaLLM(model="llama3:latest")  # Verifies if the statement is True/False/None
ankur = OllamaLLM(model="deepseek-r1:1.5b")  # Generates False statements

# Define the prompt template for false statement generation
false_template = """
Forget previous conversations. You are tasked with generating an incorrect fact about the Valmiki Ramayana, its characters (like Ram, Sita, Ravan, Hanuman, Bali, Shrupnakha, Angad, Jatayu, Lakshman) and their moral values.
Your statement should sound plausible but must be historically inaccurate.
Only generate the false statement, nothing else.

Statement:
"""

# Define the prompt template for classification
verify_template = """
Forget previous conversations. You will classify the given statement about the Valmiki Ramayana.
If the statement is factually correct, reply with "True".
If the statement is incorrect, reply with "False".
If the statement is irrelevant or not about Ramayana, reply with "None".

Statement: {statement}

Answer:
"""

# Create prompt chains
false_prompt = ChatPromptTemplate.from_template(false_template)  # Generates False Data
verify_prompt = ChatPromptTemplate.from_template(verify_template)  # Classifies True/False/None

# Load existing dataset from JSON file if it exists
def load_existing_data():
    """Load existing false/none dataset from JSON file."""
    if os.path.exists("false_none_dataset.json"):
        try:
            with open("false_none_dataset.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Warning: JSON file is corrupted. Starting fresh.")
            return []
    return []

# Generate & Verify Data
def generate_false_none_data(num_samples=10):
    false_none_dataset = load_existing_data()  # Load existing data

    for _ in range(num_samples):
        # Step 1: Generate a false statement
        false_statement = ankur.invoke(false_prompt.format_prompt().to_string())  # ✅ Fixed input format
        false_statement = remove_think_blocks(false_statement).strip()
        print(f"Generated False Statement: {false_statement}")

        # Step 2: Verify the statement
        verification_result = aaditya.invoke(verify_prompt.format_prompt(statement=false_statement).to_string())  # ✅ Fixed input format
        verification_result = remove_think_blocks(verification_result).strip()
        print(f"Verification Result: {verification_result}")

        # Step 3: Store only if False or None
        if verification_result in ["False", "None"]:
            false_none_dataset.append({
                "instruction": "Verify the factual correctness of the following statement about the Ramayana.",
                "input": false_statement,
                "output": verification_result
            })

        # Save after each generation to prevent data loss
        save_dataset(false_none_dataset)

# Save dataset to JSON file
def save_dataset(dataset):
    """Save dataset to JSON file."""
    with open("false_none_dataset.json", "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=4, ensure_ascii=False)
    print("✅ False and None dataset saved as false_none_dataset.json")

# Function to remove unnecessary text from responses
def remove_think_blocks(response: str) -> str:
    """Removes any text within <think> and </think> blocks from the response."""
    while "<think>" in response and "</think>" in response:
        start = response.find("<think>")
        end = response.find("</think>") + len("</think>")
        response = response[:start] + response[end:]
    return response

# Run the data generation
if __name__ == "__main__":
    generate_false_none_data(num_samples=100)  # Adjust sample count as needed
