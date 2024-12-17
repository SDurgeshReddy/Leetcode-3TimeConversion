def timeConversion():
    # Take input as a single string
    s = input().strip()
    
    # Extract hour, minute, second, and AM/PM from the string
    period = s[-2:]  # AM or PM
    hour, minute, second = map(int, s[:-2].split(":"))  # Extract hours, minutes, seconds
    
    # Convert hour based on AM/PM
    if period == "AM":
        if hour == 12:  # 12 AM is 00 in 24-hour format
            hour = 0
    else:  # PM case
        if hour != 12:  # Add 12 to the hour if it's not already 12 PM
            hour += 12
    
    # Format the time in 24-hour format (zero-padded)
    result = f"{hour:02}:{minute:02}:{second:02}"
    
    # Print the result
    print(result)

# Call the function
timeConversion()
