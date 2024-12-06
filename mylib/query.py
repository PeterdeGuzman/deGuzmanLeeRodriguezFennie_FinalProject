"""
Query for recommender
"""

import boto3
from boto3.dynamodb.conditions import Key, Attr


# def book_query(user_input, option):
#     """
#     Process the input and option here
#     """

#     # For demonstration purposes, we just return a string
#     return f"User input: {user_input}, Selected option: {option}"


def book_query(dynamodb, user_input, option):
    """
    Query DynamoDB based on user input and selected option.
    """
    table = dynamodb.Table("mystery")
    if option == "author":
        # Query DynamoDB for books by author
        response = table.query(KeyConditionExpression=Key("author").eq(user_input))
    # elif option == "title":
    #     # Query DynamoDB for books by title
    #     response = table.query(KeyConditionExpression=Key("title").eq(user_input))
    else:
        return "Invalid option"

    # Extract items from the response
    items = response.get("Items", [])

    # Return result or message if no results
    if items:
        return items
    else:
        return "No results found"
