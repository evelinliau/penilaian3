from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/IGS')
def IGS():
    data = [1, 2, 3, 4]
    kata = "CODING IGS"
    return render_template('IGS.html', data=data, kata=kata)

if __name__ == '__main__':
    app.run(debug=True)
