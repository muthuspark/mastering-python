import graphene

class Hello(graphene.ObjectType):
    message = graphene.String()

class Query(graphene.ObjectType):
    hello = graphene.Field(Hello)

    def resolve_hello(self, info):
        return Hello(message="Hello, GraphQL!")

schema = graphene.Schema(query=Query)