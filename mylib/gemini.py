"""
Gemini Access & Query
"""

import os
import re
import google.generativeai as genai


def gemini_prompt(user_input):
    """
    Prompt Google's Gemini API to generate book titles for the provided input.
    Cleans and formats the output to make it more readable.
    """
    # Configure the API key
    genai.configure(api_key=os.getenv("API"))

    # Initialize the Generative AI model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Generate content using the user input
    response = model.generate_content(
        f"Please give me one paragraph bio for {user_input} as writer or author."
    )

    # Access and clean the response content
    if response and response.candidates:
        raw_output = response.candidates[0].content.parts[0].text

        # Clean up any unwanted formatting (e.g., extra asterisks, spaces)
        cleaned_output = raw_output.strip()  # Remove leading/trailing whitespace

        # Optionally, replace asterisks and extra spaces
        cleaned_output = re.sub(r"\*+", "", cleaned_output)  # Remove asterisks
        cleaned_output = re.sub(
            r"\s{2,}", " ", cleaned_output
        )  # Replace multiple spaces with one

        # Optional: Split into a list of book titles, assuming titles are separated by commas, newlines, or other delimiters
        book_titles = [
            title.strip()
            for title in re.split(r"[,\n]+", cleaned_output)
            if title.strip()
        ]

        # Format the list of book titles as a more readable string
        formatted_output = "\n".join(book_titles)

        return formatted_output

    return "No response generated."
