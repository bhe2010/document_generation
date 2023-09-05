from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)

def create_payload():
    return "hello world"

@app.route('/')
def index():
    payload = create_payload()
    html = render_template(
        "packing_slip_template.html",
        payload=payload
    )

    path_wkhtmltopdf = r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    pdf = pdfkit.from_string(html, False, configuration=config)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    return response


if __name__ == '__main__':
    app.run(debug=True)