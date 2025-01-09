from ariadne import QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

type_defs = gql("""
    type Query {
        books: [Book]
        book(id: Int!): Book
    }
    type Book {
        id: Int!
        title: String!
        author: String!
    }
""")

query = QueryType()

@query.field("books")
def resolve_books(*_):
    return [
        {"id": 1, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
        {"id": 2, "title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams"},
    ]

@query.field("book")
def resolve_book(*_, id):
    books = [
        {"id": 1, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
        {"id": 2, "title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams"},
    ]
    for book in books:
        if book["id"] == id:
            return book
    return None


schema = make_executable_schema(type_defs, query)
app = GraphQL(schema)
