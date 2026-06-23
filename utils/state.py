USER_STATES = {}


def set_state(user_id: int, state: str, data=None):
    USER_STATES[user_id] = {
        "state": state,
        "data": data
    }


def get_state(user_id: int):
    return USER_STATES.get(user_id)


def clear_state(user_id: int):
    USER_STATES.pop(user_id, None)


def has_state(user_id: int, state: str):
    user = USER_STATES.get(user_id)

    if not user:
        return False

    return user["state"] == state
