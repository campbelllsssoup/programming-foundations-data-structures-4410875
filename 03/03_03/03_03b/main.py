user_preferences = {
    "language": "English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format": "MM/DD/YYYY"
}

# Mutate the dictionary - change the value of a key
# overwrites the previous value

user_preferences["language"] = "Spanish"
user_preferences["volume_level"] = 50
user_preferences["highlight_color"] = "yellow"

# use del to delete a key in the dictionary
# destructive deletion, doesn't return the key's value

del user_preferences["currency"]

# we've provided N/A as a default value to be returned
# if the key doesn't exist in the dictionary
removed_item = user_preferences.pop("date_format", "N/A")


non_existent_item = user_preferences.pop("color", "N/A")