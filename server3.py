from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/ola/')
def ola():
   projeto = "Euprogramo!"
   return render_template('ola2.html', nome=projeto)
   
if __name__ == '__main__':
    app.run(debug=True)

