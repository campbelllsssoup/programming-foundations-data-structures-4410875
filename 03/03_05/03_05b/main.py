user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

# task; clean the dictionary by removing keys with empty values
# O(n) linear time complexity

# def update_preferences(user_pref):
#     updated_preferences = {}
#     for key, value in user_pref.items():
#         if value is not None:
#             updated_preferences[key] = value
#     return updated_preferences

# dictionary comprehensions
# a concise way to create new dictionaries from an iterable object
# three parts: setting the key & value, the iterable, and the condition
def update_preferences(user_pref):
    return {key: value for key, value in user_pref.items() if value is not None}

print(update_preferences(user_preferences))

# On dictionaries:
# dictionaries have fast search operations, but they take up more space
# Lookup, insertion, and deletion all take O(1) or constant time
# useful for storing mapping relationships
# grow and shrink in size dynamically - flexible
# to keep the keys in order, used an ordered dictionary or sort it explicity
# limitation: keys in a dictionary must be immutable
