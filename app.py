from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    ascii_banner = "Impact Players"
    return ascii_banner

if __name__ == '__main__':
    app.run(debug=True)
