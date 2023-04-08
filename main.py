# - *- coding: utf- 8 - *-
from flask import Flask, send_file, request
from io import BytesIO
import qrcode

app = Flask(__name__)

def make_qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=1)
    qr.add_data(url); qr.make(fit=True)
    img = qr.make_image(fill_color="#152B42", back_color="transparent")
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()
    return img_bytes

@app.route('/api/make', methods=['POST'])
def get_data():
    url = request.form["url"]
    qrcode = make_qr_code(url)
    content_type = 'image/png'
    return send_file(BytesIO(qrcode), mimetype=content_type)

if __name__ == "__main__":
    app.run()