query_string = """
    query {
        hello {
            message
        }
    }
"""

result = schema.execute(query_string)
print(result.data['hello']['message']) # Output: Hello, GraphQL!