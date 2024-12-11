"""
Load Functions
"""

import csv
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

# Create Table

dynamodb = boto3.client("dynamodb", region_name="us-east-1")


def create_table(table_name="mystery"):
    """
    Creates a DynamoDB table with 'bookid' as the partition key.
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
        # Create the table with `bookid` as partition key
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    "AttributeName": "book_id",
                    "KeyType": "HASH",
                },  # 'bookid' as partition key
            ],
            AttributeDefinitions=[
                {
                    "AttributeName": "book_id",
                    "AttributeType": "S",
                },  # `bookid` is a string
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )

        # Wait for the table to be created
        table.meta.client.get_waiter("table_exists").wait(TableName=table_name)
        print(f"Table '{table_name}' created successfully.")

    except ClientError as e:
        print(f"Error creating table: {e}")


# Load into DynamoDB


def load_csv_to_dynamodb(csv_file_path, table_name="mystery", max_workers=5):
    """
    Load data from a CSV file into DynamoDB using batch write and threading for concurrency.
    Allows duplicates without any checks for existing items in the table.

    :param csv_file_path: The path to the CSV file to load.
    :param table_name: The name of the DynamoDB table to insert data into.
    :param max_workers: The maximum number of concurrent threads for batch processing.
    """
    load_dotenv()

    # Get AWS Credentials from .env file
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    # Initialize DynamoDB Resource
    dynamodb = boto3.resource(
        "dynamodb",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name="us-east-1",
    )

    table = dynamodb.Table(table_name)

    try:
        # Open the CSV file and read the data
        with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)  # Read all rows at once to improve performance

        insert_count = 0
        batch = []

        def process_batch(batch):
            nonlocal insert_count
            try:
                with table.batch_writer() as batch_writer:
                    for item in batch:
                        batch_writer.put_item(Item=item)  # Allows duplicates
                insert_count += len(batch)
                print(f"Successfully inserted {len(batch)} items.")
            except ClientError as e:
                print(f"Error inserting batch: {e}")

        # Prepare items to be inserted into DynamoDB
        def create_item(row):
            return {
                "book_id": row["book_id"],
                "title": row["title"],
                "isbn": row["isbn"],
                "text_reviews_count_book": row["text_reviews_count_book"],
                "series": row["series"],
                "country_code": row["country_code"],
                "language_code": row["language_code"],
                "popular_shelves": row["popular_shelves"],
                "asin": row["asin"],
                "is_ebook": row["is_ebook"],
                "average_rating_book": row["average_rating_book"],
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
                "name": row["name"],
                "ratings_count_book": row["ratings_count_book"],
                "work_id": row["work_id"],
                "title_without_series": row["title_without_series"],
                "author_id": row["author_id"],
                "ratings_count_author": row["ratings_count_author"],
                "average_rating_author": row["average_rating_author"],
            }

        # Using ThreadPoolExecutor to process the CSV rows in parallel
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            batch_size = 1000  # This is the number of items per batch
            for i in range(0, len(rows), batch_size):
                batch = [create_item(row) for row in rows[i : i + batch_size]]
                futures.append(executor.submit(process_batch, batch))

            # Wait for all futures to complete
            for future in as_completed(futures):
                future.result()

        print(f"Finished processing. Total items inserted: {insert_count}")

    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    load_dotenv()

    # Get AWS Credentials from .env file
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    dynamodb = boto3.client(
        "dynamodb",
        region_name="us-east-1",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )
    dynamodb.update_table(
        TableName="mystery",
        ProvisionedThroughput={
            "ReadCapacityUnits": 50,  # Increase this value
            "WriteCapacityUnits": 1000,  # Increase this value
        },
    )
    # create_table(table_name="mystery")
    load_csv_to_dynamodb(
        csv_file_path="/Users/pdeguz01/Documents/git/deGuzmanLeeRodriguezFennie_FinalProject/mylib/merged_mysteryauthors.csv",
    )
