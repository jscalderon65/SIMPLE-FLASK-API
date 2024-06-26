from flask import Flask, jsonify

from services.system import system_service_blueprint

app = Flask(__name__)

app.register_blueprint(system_service_blueprint, url_prefix="/api")


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
