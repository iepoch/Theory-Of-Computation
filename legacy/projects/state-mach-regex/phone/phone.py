import re  # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# TODO Define your regex
pattern = r"[0-9]{3}[-][0-9]{3}[-][0-9]{4}|[0-9]{10}|[(][0-9]{3}[)]\s[0-9]{3}[-][0-9]{4}|[0-9]{3}\s[0-9]{3}\s[0-9]{4}"

while line != "exit":
    # TODO Find matches
    matches = re.findall(pattern, line)
    # TODO If no match found, print that no number was found
    if not matches:
        print(f'Phone number was not found')
        break
    # TODO Else, break number up into area code, prefix, and suffic
    else:
        phone = ''.join(num for num in line if num.isalnum())
        area = phone[:3]
        prefix = phone[3:6]
        suffix = phone[6:]
        print(
            f'Found phone Area Code: {area}, Prefix: {prefix}, Suffix: {suffix}')
    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!

    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")
