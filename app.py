from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="POST" action="/predict">
            <input type="text" name="sentence">
            <input type="submit" value="Predict">
        </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    sentence = request.form['sentence']
    # Do something with the sentence, such as passing it to a machine learning model for prediction
    return f'You entered: {sentence.lower()}'

if __name__ == '__main__':
    app.run()
