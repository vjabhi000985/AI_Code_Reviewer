import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load the environment variable
load_dotenv()

# Initialize the Google Generative AI API Key
api_key=os.getenv("GOOGLE_API_KEY")

# Initialize the AI Model and System Prompt
def initialize(api_key):
  """
  Initialize the Generative AI model and system prompt for analyzing code.

  Returns:
  dict: A dictionary containing the initialized Generative AI model and the system prompt.
  """
  # Initialize an empty dictionary to store configurations
  cors = {}
  
  # Configure the Generative AI API
  genai.configure(api_key=api_key)

  # Initialize the GenAI model
  llm = genai.GenerativeModel("gemini-1.5-flash")

  # Define the system prompt
  sys_prompt = """
  You are an expert AI code reviewer integrated into a user-friendly application designed to analyze JavaScript,Python, and Java code submitted by users. Your role is to perform the following:
  1. ## Bug Report: Identify potential bugs, syntax errors, and logical flaws in the code.
  2. ## Fixed Code: Return fixed or optimized code snippets alongside explanations of the changes made.
  3. ## User Guidance: Ensure feedback is concise, easy to understand, and helpful for developers of varying experience levels.
  Maintain a professional tone while keeping explanations simple and accessible. Focus on accuracy, efficiency, and improving the user's understanding of best coding practices.
  ### Important Note:
  If the input is not a JavaScript, Python, or Java coding question, you must reply with:
  "Please ask me a coding-related question in JavaScript, Python, or Java. I can only analyze and provide feedback on code snippets or related queries. Other than that, I am unable to assist."
  """

  # Store the model and the prompt as a dictionary
  cors = {
    "model"  : llm,
    "prompt" : sys_prompt
  }

  # Returns the configuration stored as a dictionary
  return cors

# Function to get a response from the model
def get_response(sys_prompt, code, model):
  """
  Generate a response from the GenAI model based on the system prompt and user input code.
  """
  try:
    response = model.generate_content([sys_prompt, code])
    return response.text
  except Exception as e:
    return f"An error occurred: {str(e)}"
  
def main():
  """
  Main function to run the Streamlit app for the AI Code Reviewer.
  """
  # Initialize the AI model and system prompt
  config = initialize(api_key=api_key)

  # Extract the model and prompt from the configuration
  model = config["model"]
  prompt = config["prompt"]

  # Set up the Streamlit app
  st.set_page_config(page_title="AI Code Reviewer", layout="centered")
  st.title(":page_facing_up: AI Code Reviewer")

  # Text area for code input
  code = st.text_area("Enter your code here...", height=200)

  # Create columns for Generate and Clear buttons
  col1, col2 = st.columns(2)

  # Generate response button
  with col1:
    generate_btn = st.button("Generate")

  # Clear input and output button
  with col2:
    clear_btn = st.button("Clear")

  # Button to generate code review
  if generate_btn:
      if code.strip():  # Check if the input is not empty
          with st.spinner("Analyzing your code..."):
              response = get_response(sys_prompt=prompt, code=code, model=model)
          st.header("Code Review Results")
          st.write(response)
      else:
          st.error("Please enter your code before clicking 'Generate'.")

  # Handle the Clear button action
  if clear_btn:
    st.experimental_rerun()  # Refresh the app to clear inputs and outputs

# Entry point of the application
if __name__ == '__main__':
  main()