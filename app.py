
from flask import Flask, render_template_string, request, jsonify
from google import genai

client = genai.Client(api_key="AIzaSyBjlVYQ4PJ2boRf_8Y_9eG1z82pQJ5j4rE")

app = Flask(__name__)
@app.route("/")
def home():
    return "App is running"
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>AI Learning Path</title>
</head>
<body>
<h2>AI Learning Path Generator</h2>

<input id="role" placeholder="Role"><br><br>
<input id="time" placeholder="Hours per day"><br><br>
<input id="duration" placeholder="Duration (days)"><br><br>

<button onclick="generate()">Generate</button>

<pre id="output"></pre>

<script>
function generate(){
 fetch("/generate", {
   method: "POST",
   headers: {"Content-Type":"application/json"},
   body: JSON.stringify({
     role: role.value,
     time: time.value,
     duration: duration.value
   })
 })
 .then(res => res.json())
 .then(data => output.innerText = data.roadmap)
}
</script>
</body>
</html>
"""

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json

    prompt = f"""
    Create a {data['duration']}-day learning roadmap for the role {data['role']}.
    Daily study time: {data['time']} hours.
    Use only free online resources.
    Make it week-wise and beginner-friendly.
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    return jsonify({
        "roadmap": response.text
    })
    if __name__ == "__main__":
    app.run()
 
