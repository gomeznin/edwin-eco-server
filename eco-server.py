from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def echo():
    if request.method == 'POST':
        message = request.form.get('message', '')
        return f"You said: {message}"
    else:
        return "Hello, please enter a message!"

if __name__ == '__main__':
    # Set the port number here
    port = 8000
    app.run(debug=True, port=port)
