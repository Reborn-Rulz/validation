# Import the Validate class
from Untitled-1 import Validate

# Create an instance of the Validate class with your API key
v = Validate(API_KEY)

# Validate a phone number
phone_number = '18007132618'

# Specify the country code (optional)
country_code = 'US'

# Validate the phone number
response = v.phone_number_validation_api(phone_number, country_code)

# Print the response
print(response)
