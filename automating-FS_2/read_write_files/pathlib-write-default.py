import pathlib

default = """
from datetime import datetime

def get_current_time():
    # Get the current date and time
    current_time = datetime.now()
    
    # Format the time as a string
    time_str = current_time.strftime("%H:%M:%S")
    
    return time_str

# Call the function to get and print the current time
current_time = get_current_time()
print(f"The current time is: {current_time}")

"""

path = pathlib.Path("sp.config.py")

result = path.write_text(default)

print(f"File written to {result}")
