import qrcode

def generate_qr_code(link, file_name='qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')


    img.save(file_name)

link = ""  #Your Link Goes Here
generate_qr_code(link, 'qrcode.png') #Name of the file (png)

print("QR code generated successfully!")
