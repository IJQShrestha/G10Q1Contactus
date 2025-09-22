from pyscript import display, document
# Header 
contact = "Contact Us"
text1 = "We'd love to hear from you"

# Location
location = "Our location"
street = "XXXX Mandala Street"
city = "Pasig City"

# Phone
text2 = "Phone Numbers"
main = "Main: (+63) 123-456"
mobile = "Mobile: (+63) 0926-639-4510"

# Email
text3 = "Email Addresses"
info = "info@Mandala.com"
support = "support@Mandala.com"
careers = "careers@Mandala.com"

# Footer
footer = "Open Daily: 11:00 AM - 10:00 PM"

# Display Header
display(f"{contact}", target="Contact")
display(f"{text1}", target="text1")

# Display Location
display(f"{location}", target="Location")
display(f"{street}", target="Street")
display(f"{city}", target="City")

# Display Phone
display(f"{text2}", target="Phone")
display(f"{main}", target="Main")
display(f"{mobile}", target="Mobile")

# Display Email
display(f"{text3}", target="Emailadd")
display(f"{info}", target="Info")
display(f"{support}", target="Support")
display(f"{careers}", target="Careers")

# Display Footer
display(f"{footer}", target="Footer")

