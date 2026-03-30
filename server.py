from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


def read():
    file = open("count.txt", "r")
    return int(file.read())

def write(num):
    file = open("count.txt", "w")
    file.write(str(num))

@app.route("/click", methods=["POST"])
def click():
    current = read() 
    current = current + 1
    write(current)
    return str(current)

@app.route("/score")
def score():
    return str(read())


if __name__ == "__main__":
    app.run(debug=True)
