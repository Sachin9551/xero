from flask import Flask, request, send_file
from datetime import datetime
import io

app = Flask(__name__)

# Pre-defined 1x1 pixel transparent PNG image in bytes
TRANSPARENT_1X1_PNG = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc`\x00\x00\x00\x02\x00\x01H\xaf\xa4q\x00\x00\x00\x00IEND\xaeB`\x82'

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def log_request(path):
    print("\n========== REQUEST RECEIVED ==========")
    print("Time:", datetime.utcnow())
    print("IP:", request.remote_addr)
    print("Path:", path)

    print("\nHeaders:")
    for k, v in request.headers.items():
        print(f"{k}: {v}")

    print("\nRaw Query String:")
    # Captures the unparsed text after '?' (e.g., '=[hi]')
    print(request.query_string.decode('utf-8'))

    print("\nParsed Query Parameters:")
    print(dict(request.args))

    print("======================================\n")

    # If the markdown link requests a PNG image, return the actual image bytes
    if path.endswith('.png'):
        return send_file(
            io.BytesIO(TRANSPARENT_1X1_PNG),
            mimetype='image/png'
        )

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
