def user_entity(item) -> dict:
    """ Esquema de un Usuario """
    return {
        "id": item["id"],
        "name": item["name"],
        "email": item["email"],
        "password": item["password"],
    }
