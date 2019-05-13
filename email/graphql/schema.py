"""
GraphQL schema for extracting infor from grpc service.
"""
import graphene


class UserInfo(graphene.ObjectType):
    email = graphene.String(required=True)
    firstName = graphene.String()
    lastName = graphene.String()
    id = graphene.ID()


class Query(graphene.ObjectType):

    email = graphene.Field(UserInfo,email=graphene.String())

    def resolve_email(self, info, email):
        # inside this function, we will call the grpc function (the stub.xyz) to get info about email
        # for now, returning hard coded values
        return UserInfo(email=email, firstName="testFirstName", lastName="testlastName", id=1)


schema = graphene.Schema(query=Query)


###  This is example of query (`query something` is optional, can be removed )
query = """
    query something{
      email (email:"test@gmail.com") {
        email
        firstName
        lastName
        id
      }
    }
"""








# """
# GraphQL schema for extracting results from a website.
# """
# import graphene
# import extraction
# import requests

# def extract(url):
#     html = requests.get(url).text
#     extracted = extraction.Extractor().extract(html, source_url=url)
#     print(extracted)
#     return extracted

# class Website(graphene.ObjectType):
#     email = graphene.String(required=True)

    
# class Query(graphene.ObjectType):
#     website = graphene.Field(Website, url=graphene.String())

#     def resolve_website(self, info, url):
#         extracted = extract(url)
#         return Website(url=url,
#                        id=extracted.id,
#                        firstName=extracted.first_name,
#                        lastName=extracted.last_name,
#                        email=extracted.email
#         )

# schema = graphene.Schema(query=Query)
