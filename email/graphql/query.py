import pprint
import schema


def query_url():
    q = """
    query something{
      email (email:"test@gmail.com") {
        email
        firstName
        lastName
        id
      }
    }
    """
    result = schema.schema.execute(q)
    if result.errors:
        if len(result.errors) == 1:
            raise Exception(result.errors[0])
        else:
            raise Exception(result.errors)
    return result.data


if __name__ == "__main__":
    results = query_url("https://lethain.com/migrations/")
    pprint.pprint(results)