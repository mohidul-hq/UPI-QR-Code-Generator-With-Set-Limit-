UPI QR Code Generator

This Python script generates a UPI payment QR code based on a fixed UPI ID and a user-specified amount.

Features

Accepts a fixed UPI ID for transactions.

Prompts the user to enter the amount to be received.

Generates a UPI payment URL.

Creates and saves a QR code image.

Optionally displays the QR code after generation.

Requirements

Ensure you have Python installed on your system along with the required dependencies:

pip install qrcode[pil]

Usage

Clone the repository or download the script.

Open a terminal or command prompt and run:

python upi_qr_generator.py

Enter the amount when prompted.

The generated QR code will be saved as QrCode.png and displayed.

Example Output

Enter the amount to be received: 100
QR code generated and saved as QrCode.png.

Customization

Change the upi_id variable to your own UPI ID.

Modify recipient_name to reflect the actual recipient's name.

Adjust the filename if needed.

License

This project is open-source and available under the MIT License.

Author

Mohidul Haque

