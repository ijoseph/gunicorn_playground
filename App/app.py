from flask import Flask
app = Flask(__name__)

@app.route('/')
def hell_ow_orld():
    return "HELL OW WORLD"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
