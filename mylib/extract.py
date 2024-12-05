"""
Extract and Transform Functions
"""

import requests
import gzip
import json
import csv
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os
import pandas as pd


# Parse JSON to CSV
def parse_json_to_csv(input_json_file, output_csv_file):
    """
    Parse a JSON file and save its contents into a CSV file.

    :param input_json_file: Path to the input JSON file (can contain a list of objects).
    :param output_csv_file: Name of the output CSV file (default is 'output.csv').
    """
    try:
        # Step 1: Open and load the JSON data
        with open(input_json_file, "r", encoding="utf-8") as f:
            data = []
            for line in f:
                try:
                    # Attempt to load each line as a separate JSON object
                    data.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"Skipping line due to error: {e}")

        # Check if the data is a list of records
        if not data or not isinstance(data, list):
            print("No valid data found or unexpected format.")
            return

        # Step 2: Extract headers (keys) from the first item
        headers = data[0].keys() if data else []

        # Step 3: Write to CSV
        with open(output_csv_file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()

            # Write each item (row) in the JSON as a CSV row
            for row in data:
                writer.writerow(row)

        print(f"CSV file '{output_csv_file}' has been created successfully.")

    except Exception as e:
        print(f"Error processing the JSON file: {e}")


# left join author names on mystery dataset

mystery = pd.read_csv(
    "/Users/pdeguz01/Documents/git/deGuzmanLeeRodriguezFennie_FinalProject/mylib/mystery.csv"
)


# extract author_id for first authors of mystery books
# Function to extract 'author_id' from the 'authors' column
def extract_author_id(authors):
    try:
        # Convert string representation of list to a Python object
        authors_list = ast.literal_eval(authors)
        if isinstance(authors_list, list) and len(authors_list) > 0:
            return authors_list[0].get(
                "author_id", ""
            )  # Get the first author's 'author_id'
    except (ValueError, SyntaxError):
        pass  # Return None if there's an error in parsing
    return ""  # Default to empty string if no valid author_id


# Apply the function to the 'authors' column
mystery["author_id"] = mystery["authors"].apply(extract_author_id)

mystery["author_id"] = pd.to_numeric(mystery["author_id"], errors="coerce")

authors = pd.read_csv(
    "/Users/pdeguz01/Documents/git/deGuzmanLeeRodriguezFennie_FinalProject/mylib/authors.csv"
)

merged_df = pd.merge(mystery, authors, on="author_id", how="left", indicator=True)

# clean column names


# Example usage
if __name__ == "__main__":
    input_json_file_mystery = "/Users/pdeguz01/Documents/git/Data/goodreads/goodreads_books_mystery_thriller_crime.json"  # JSON file for mystery books
    parse_json_to_csv(input_json_file_mystery, output_csv_file="mystery.csv")
    input_json_file_authors = "/Users/pdeguz01/Documents/git/Data/goodreads/goodreads_book_authors.json"  # JSON file for authors
    parse_json_to_csv(input_json_file_authors, output_csv_file="authors.csv")
    mystery = pd.read_csv(
        "/Users/pdeguz01/Documents/git/deGuzmanLeeRodriguezFennie_FinalProject/mylib/mystery.csv"
    )
    mystery["author_id"] = mystery["authors"].apply(extract_author_id)
    mystery["author_id"] = pd.to_numeric(mystery["author_id"], errors="coerce")
    authors = pd.read_csv(
        "/Users/pdeguz01/Documents/git/deGuzmanLeeRodriguezFennie_FinalProject/mylib/authors.csv"
    )
    merged_df = pd.merge(mystery, authors, on="author_id", how="left", indicator=True)
    rename_dict = {
        "text_reviews_count_x": "text_reviews_count_book",
        "average_rating_x": "average_rating_book",
        "average_rating_y": "average_rating_author",
        "ratings_count_x": "ratings_count_book",
        "ratings_count_y": "ratings_count_author",
    }
    merged_df = merged_df.rename(columns=rename_dict)
    merged_df = merged_df.drop(
        columns=[
            "text_reviews_count_y",
            "_merge",
        ]
    )
    merged_df.to_csv("merged_mysteryauthors.csv", index=False)
