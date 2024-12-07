"""
Query for recommender
"""

# import boto3
from boto3.dynamodb.conditions import Key


# def book_query(user_input, option):
#     """
#     Process the input and option here
#     """

#     # For demonstration purposes, we just return a string
#     return f"User input: {user_input}, Selected option: {option}"


# Lauren Oliver


def book_query(dynamodb, user_input):
    """
    Query DynamoDB based on user input and selected option.
    """
    table = dynamodb.Table("mystery")

    response = table.query(
        IndexName="name-title-index",  # The name of the GSI
        KeyConditionExpression=Key("name").eq(user_input),
    )

    # Extract items from the response
    items = response.get("Items", [])

    # Return result or message if no results
    if items:
        # Return only the titles
        return [item["title"] for item in items]
    else:
        return "No results found"
