from flask import Flask, render_template
app = Flask(__name__)
@app.route('/ola/')

def ola():
    return render_template('ola.html')

if __name__ == '__main__':
    app.run(debug=True)

