from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open(r'models\model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_file', methods=['POST', 'GET'])
def create_file():
    data = request.json
    try:
        rnd = float(data.get('input1'))
        marketing = float(data.get('input2'))
    except Exception:
        return ''
    else:
        output = int(model.predict([[rnd, marketing]])[0])
        return f'{output}'

if __name__ == '__main__':
    app.run(debug=True)
