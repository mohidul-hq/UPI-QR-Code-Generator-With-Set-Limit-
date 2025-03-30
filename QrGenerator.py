import qrcode

# Fixed UPI ID
#Enter your upi id 
upi_id = "example@upi"

# Prompt user for the amount to be received
amount = input("Enter the amount to be received: ")

# Define the recipient's name (optional but recommended)
recipient_name = "Mohidul Haque"  # Replace with the actual recipient's name

# Define the currency code (INR for Indian Rupees)
currency = "INR"

# Construct the UPI payment URL with the amount and currency parameters
upi_url = f"upi://pay?pa={upi_id}&pn={recipient_name}&am={amount}&cu={currency}"

# Generate the QR code
upi_qr = qrcode.make(upi_url)

# Save the QR code as an image file
upi_qr_filename = "QrCode.png"
upi_qr.save(upi_qr_filename)

# Display the QR code (optional)
upi_qr.show()
print(f"QR code generated and saved as {QrCode.png}.")
