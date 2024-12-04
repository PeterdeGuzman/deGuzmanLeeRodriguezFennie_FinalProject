"""
Load Functions
"""

import requests
import gzip
import json
import csv
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os


# Create Table

dynamodb = boto3.client("dynamodb", region_name="us-east-1")


def create_table(table_name="mystery"):
    """
    Creates a DynamoDB table with 'name' as the partition key.
    """
    load_dotenv()
    # Get AWS Credentials from .env file
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    # Intialize DynamoDB Resource
    dynamodb = boto3.resource(
        "dynamodb",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name="us-east-1",
    )

    try:
        # Create the table with `name` as partition key
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    "AttributeName": "authors",
                    "KeyType": "HASH",
                },  # 'authors' as partition key
            ],
            AttributeDefinitions=[
                {
                    "AttributeName": "authors",
                    "AttributeType": "S",
                },  # `authors` is a string
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )

        # Wait for the table to be created
        table.meta.client.get_waiter("table_exists").wait(TableName=table_name)
        print(f"Table '{table_name}' created successfully.")

    except ClientError as e:
        print(f"Error creating table: {e}")


# Load into DynamoDB


def load_csv_to_dynamodb(csv_file_path, table_name="mystery"):
    """
    Load data from a CSV file into DynamoDB.

    :param csv_file_path: The path to the CSV file to load.
    :param table_name: The name of the DynamoDB table to insert data into.
    """
    # Connect to DynamoDB (LocalStack in this case)
    dynamodb = boto3.resource(
        "dynamodb",
        region_name="us-east-1",
    )
    table = dynamodb.Table(table_name)

    try:
        # Open the CSV file and read the data
        with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            insert_count = 0  # Counter to track the number of records inserted

            # Iterate over each row in the CSV file
            for row in reader:
                if insert_count >= 500:
                    print("Reached 500 authors. Stopping the insert process.")
                    break

                # Create the item to be inserted into DynamoDB
                item = {
                    "authors": row["authors"],  # 'name' is the partition key
                    "title": row["title"],  # Optional: sort key if needed
                    "isbn": row["isbn"],
                    "text_reviews_count": row["text_reviews_count"],
                    "series": row["series"],
                    "country_code": row["country_code"],
                    "language_code": row["language_code"],
                    "popular_shelves": row["popular_shelves"],
                    "asin": row["asin"],
                    "is_ebook": row["is_ebook"],
                    "average_rating": row["average_rating"],
                    "kindle_asin": row["kindle_asin"],
                    "similar_books": row["similar_books"],
                    "description": row["description"],
                    "format": row["format"],
                    "link": row["link"],
                    "publisher": row["publisher"],
                    "num_pages": row["num_pages"],
                    "publication_day": row["publication_day"],
                    "isbn13": row["isbn13"],
                    "publication_month": row["publication_month"],
                    "edition_information": row["edition_information"],
                    "publication_year": row["publication_year"],
                    "url": row["url"],
                    "image_url": row["image_url"],
                    "book_id": row["book_id"],
                    "ratings_count": row["ratings_count"],
                    "work_id": row["work_id"],
                    "title_without_series": row["title_without_series"],
                }

                # Insert the item into DynamoDB
                try:
                    table.put_item(Item=item)
                    insert_count += 1
                    print(
                        f"Inserted item for {row['authors']} (author_id: {row['author_id']})"
                    )
                except ClientError as e:
                    print(f"Error inserting item: {e}")

    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":

    create_table(table_name="mystery")
    # load_csv_to_dynamodb(
    #     csv_file_path="/Users/pdeguz01/Documents/git/deGuzmanLeeRodriguezFennie_FinalProject/mylib/mystery.csv",
    # )
