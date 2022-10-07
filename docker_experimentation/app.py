import uvicorn
from fastapi import FastAPI
from inputText import InputText
import pickle

from keras.models import load_model
from keras_preprocessing.sequence import pad_sequences
from keras.models import load_model


def predict_class(input_text):
    '''Function to predict sentiment class of the passed text'''
    
    text = []
    text.append(input_text)

    sentiment_classes = ['Negative', 'Positive']
    max_len=50
    
    # Transforms text to a sequence of integers using a tokenizer object
    xt = tokenizer.texts_to_sequences(text)
    # Pad sequences to the same length
    xt = pad_sequences(xt, padding='post', maxlen=max_len)
    # Do the prediction using the loaded model
    yt = model.predict(xt).argmax(axis=1)
    # Print the predicted sentiment
    return ('The predicted sentiment is', sentiment_classes[yt[0]])


with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

app = FastAPI(title="A sentiment analysis API",
    description="An API which takes in a text from the user and responds with wheter the text is positive or negative.")

model = load_model('model.h5')


@app.get('/')
def index():
    return {'message':'Hello World!'}

@app.post('/predict')
def predict_sentiment(data:InputText):
    data = data.dict()
    text = data['text'] 
    prediction = predict_class(text)
    return prediction 


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# python -m uvicorn app:app --reload