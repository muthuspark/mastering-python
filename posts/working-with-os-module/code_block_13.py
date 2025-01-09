home_directory = os.getenv("HOME", "/tmp") #If HOME is not set, use /tmp
print(f"Home directory: {home_directory}")