def user_entity(item) -> dict:
    """ Esquema de un Usuario """
    return {
        "_id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"],
    }

def users_entity(entity) -> list:
    """ esquema de usuarios """
    return [ user_entity(item) for item in entity ]
