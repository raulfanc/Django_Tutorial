import os

# specify the name of the app you just created
app_name = "my_new_app"

# specify the path to the project's settings.py file
settings_file = os.path.join(os.getcwd(), "my_project", "settings.py")

# read the contents of the settings file
with open(settings_file, "r") as f:
    contents = f.read()

# find the INSTALLED_APPS section
apps_index = contents.find("INSTALLED_APPS")
apps_end_index = contents.find("]", apps_index)
apps_section = contents[apps_index:apps_end_index]

# add the app name to the INSTALLED_APPS list
apps_section += f"\n    '{app_name}',"

# replace the old INSTALLED_APPS section with the new one
new_contents = contents[:apps_index] + apps_section + contents[apps_end_index:]

# write the new contents back to the settings file
with open(settings_file, "w") as f:
    f.write(new_contents)
