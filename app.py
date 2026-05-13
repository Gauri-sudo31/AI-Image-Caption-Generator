from flask import Flask, render_template, request
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

app = Flask(__name__)

KEY = "YOUR_AZURE_KEY"
ENDPOINT = "YOUR_AZURE_ENDPOINT"

client = ComputerVisionClient(
    ENDPOINT,
    CognitiveServicesCredentials(KEY)
)

@app.route("/", methods=["GET", "POST"])
def home():
    caption = ""

    if request.method == "POST":
        image = request.files["image"]

        result = client.describe_image_in_stream(image)

        if result.captions:
            caption = result.captions[0].text

    return render_template("index.html", caption=caption)

if __name__ == "__main__":
    app.run(debug=True)