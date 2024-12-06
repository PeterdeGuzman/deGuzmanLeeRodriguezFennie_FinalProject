"""
Flask App
"""

import boto3
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from mylib import query

load_dotenv()  # Get AWS credentials from environment (optional if using AWS CLI config)
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION_NAME = (
    "us-east-1"  # Use the region of the table# Initialize DynamoDB resource using boto3
)
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=REGION_NAME,
)  # Define the table name (extracted from ARN)


# instance of the Flask class
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
    Submit user input for query
    """
    user_input = request.form["userInput"]  # Get the user input from the form
    option = request.form["options"]  # Get the selected option

    # Pass the dynamodb client to query.py
    result = query.book_query(dynamodb, user_input, option)  # Call function in query.py

    return render_template("result.html", result=result)  # Display result page


if __name__ == "__main__":
    app.run(debug=True)
