from flask import Flask, request, Response
from datetime import datetime
import base64

app = Flask(__name__)

# 1x1 transparent PNG
PIXEL = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO7Z0XcAAAAASUVORK5CYII="
)

@app.route("/log.png")
def log_png():
    print("\n========== IMAGE REQUEST RECEIVED ==========")
    print("Time:", datetime.utcnow())
    print("IP:", request.remote_addr)

    print("\nHeaders:")
    for k, v in request.headers.items():
        print(f"{k}: {v}")

    print("\nQuery Parameters:")
    print(dict(request.args))

    print("============================================\n")

    response = Response(PIXEL, mimetype="image/png")

    # Disable cache
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, proxy-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def log_request(path):
    print("\n========== NORMAL REQUEST RECEIVED ==========")
    print("Time:", datetime.utcnow())
    print("IP:", request.remote_addr)
    print("Path:", path)

    print("\nHeaders:")
    for k, v in request.headers.items():
        print(f"{k}: {v}")

    print("\nQuery Parameters:")
    print(dict(request.args))

    print("=============================================\n")

    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
