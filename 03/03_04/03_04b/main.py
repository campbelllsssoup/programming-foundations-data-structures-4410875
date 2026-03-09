# input:
user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

# output:
# user_preferences = { 
#     "timezone": "GMT",
#     "language": "English",
#     "currency": "USD"
# }

# task: write a function update_preferences,
# that deletes the 'notifications' and 'theme' preferences



def update_preferences(user_pref):
    user_pref.pop("notifications", "N/A")
    user_pref.pop("theme", "N/A")
    return user_pref

user_preferences = update_preferences(user_preferences)
print(user_preferences)
