"""
Flask App
"""

import os
import boto3
from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
from mylib import query
from mylib import gemini


load_dotenv()  # Get AWS credentials from environment (optional if using AWS CLI config)
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION_NAME = "us-east-1"  # Use the region of the table
# Initialize DynamoDB resource using boto3
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=REGION_NAME,
)  # Define the table name (extracted from ARN)


# Configure the API key for Google Generative AI
genai.configure(api_key=os.getenv("API"))

# Initialize the Flask app
app = Flask(__name__)


# Home route
@app.route("/", methods=["GET"])
def home():
    """
    Render the homepage
    """
    return render_template("homepage.html")


# Project route (contains the form)
@app.route("/project", methods=["GET", "POST"])
def project():
    """
    Render the project page, and handle form submissions
    """
    return render_template("project.html")  # Render the form page on GET request


@app.route("/submit", methods=["POST"])
def submit():
    """
    Submit user input for query and generate content using Gemini API
    """
    user_input = request.form["userInput"]  # Get the user input from the form
    option = request.form["options"]  # Get the selected option

    # Logic for handling different options (if needed)
    if option == "Author":
        # DynamoDB query
        result = query.book_query(dynamodb, user_input)

    elif option == "Gemini":
        try:
            result = gemini.gemini_prompt(
                user_input
            )  # Call your gemini function with the user input
        except Exception as e:
            result = f"Error generating content: {str(e)}"

    else:
        result = "Invalid option selected."

    return render_template("result.html", result=result)  # Display result page


if __name__ == "__main__":
    app.run(debug=True)
