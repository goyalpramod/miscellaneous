import numpy as np # linear algebra
import pandas as pd # data wrangling

#For Preprocessing
import re    # RegEx for removing non-letter characters
import nltk  # natural language processing
nltk.download("stopwords") # list of most common english words like a,an,the etc
from nltk.corpus import stopwords
from nltk.stem.porter import *

# For Building the model
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Embedding, Conv1D, MaxPooling1D, Bidirectional, LSTM, Dense, Dropout
from keras.metrics import Precision, Recall
from keras.optimizers import SGD

# Additional libraries 
import string
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import pickle
import keras.backend as K
from keras.models import load_model

max_words = 5000
max_len=50


class DataCleaner:
    def clean_text(self,text):
        # Remove non-letters
        self.tokens= nltk.word_tokenize(re.sub("[^a-zA-Z]", " ",text))
        # Convert to lower case
        self.tokens = [self.token.lower() for self.token in self.tokens]
        return ' '.join(self.tokens[2:])

    def process_text(self,msg):
        # Removing words with @ in them
        self.nopunc =[char for char in msg if char not in string.punctuation]
        self.nopunc=''.join(self.nopunc)
        # Return with stopwords removed
        return ' '.join([word for word in self.nopunc.split() if word.lower() not in stopwords.words('english')])

    def split_text(self,text):
        # Spliting a single sentence into a list of words
        return text.split()



class ProcessDataframe:    
    def process_dataframe(self):
        # Drops the redundant column from the dataframe
        self.df = self.df.iloc[: , 1:]
        # Converts labels from positive, negative to 1 and 0 respectively
        self.df['airline_sentiment'] = self.df['airline_sentiment'].apply(lambda x: 1 if x =='positive' else 0)
        # Preprocesses each text present in the 'text' column and stores it in a new column named 'final_text'
        self.df['final_text'] = self.df['text'].apply(self.clean_text).apply(self.process_text).apply(self.split_text)
        
        
    def split_dataframe(self,X,test_size_train = 0.2,test_size_val = 0.25):
        # Splits the dataframe into train, test and val set
        y = pd.get_dummies(self.df['airline_sentiment'])
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=test_size_train, random_state=1)
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(self.X_train, self.y_train, test_size=test_size_val, random_state=42) 



class Token:
    def tokenize_pad_sequences(self,text):
        '''
        Used to tokenize the input text into sequnences of intergers and then
        pad each sequence to the same length
        '''
        # Text tokenization
        self.tokenizer = Tokenizer(num_words=max_words, lower=True, split=' ')
        self.tokenizer.fit_on_texts(text)
        # Transforms text to a sequence of integers
        self.X = self.tokenizer.texts_to_sequences(text)
        # Pad sequences to the same length
        self.X = pad_sequences(self.X, padding='post', maxlen=max_len)
        # return sequences
        return self.X, self.tokenizer

    def get_tokens(self):
        self.X,self.tokenizer = self.tokenize_pad_sequences(self.df['final_text'])
        return self.X, self.tokenizer
    
    def save_tokens(self): 
        # saving
        with open('tokenizer.pickle', 'wb') as handle:
            pickle.dump(self.tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
            print("succesfuly saved")
        
    def load_tokens(self):
        # loading
        with open('tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)



class Model(DataCleaner,Token,ProcessDataframe):
    def __init__(self, datafile = "airline_sentiment_analysis.csv"):
        self.df = pd.read_csv(datafile)

    def f1_score(self,precision, recall):
        ''' Function to calculate f1 score '''
    
        self.f1_val = 2*(self.precision*self.recall)/(self.precision+self.recall+K.epsilon())
        return self.f1_val
    
    def build_model(self,vocab_size = 5000,embedding_size = 32,epochs=20,learning_rate = 0.1,momentum = 0.8):
        decay_rate = learning_rate / epochs
        self.sgd = SGD(lr=learning_rate, momentum=momentum, decay=decay_rate, nesterov=False)
        
        # Build model
        self.model= Sequential()
        self.model.add(Embedding(vocab_size, embedding_size, input_length=max_len))
        self.model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
        self.model.add(MaxPooling1D(pool_size=2))
        self.model.add(Bidirectional(LSTM(32)))
        self.model.add(Dropout(0.4))
        self.model.add(Dense(2, activation='sigmoid'))
        print(self.model.summary())
           
    def compile_model(self):
        self.model.compile(loss='categorical_crossentropy', optimizer=self.sgd, 
               metrics=['accuracy', Precision(), Recall()])

    def train_model(self,batch_size = 64, epochs = 20):
        history = self.model.fit(self.X_train, self.y_train,
                            validation_data=(self.X_val, self.y_val),
                            batch_size=batch_size, epochs=epochs, verbose=1)

    def evaluate_model(self):
        # Evaluate model on the test set
        loss, accuracy, self.precision, self.recall = self.model.evaluate(self.X_test, self.y_test, verbose=0)
        # Print metrics
        print('')
        print('Accuracy  : {:.4f}'.format(accuracy))
        print('Precision : {:.4f}'.format(self.precision))
        print('Recall    : {:.4f}'.format(self.recall))
        print('F1 Score  : {:.4f}'.format(self.f1_score(self.precision, self.recall)))

    def save_model(self):
        # Save the model architecture & the weights
        self.model.save('model.h5')
        print('Model saved')

    def load_model(self):
        # Load the saved model
        self.model = load_model('model.h5')

    def predict_class(self,text):
        '''Function to predict sentiment class of the passed text'''

        sentiment_classes = ['Negative', 'Positive']
        max_len=50

        # Transforms text to a sequence of integers using a tokenizer object
        xt = self.tokenizer.texts_to_sequences(text)
        # Pad sequences to the same length
        xt = pad_sequences(xt, padding='post', maxlen=max_len)
        print(xt)
        # Do the prediction using the loaded model
        yt = self.model.predict(xt).argmax(axis=1)
        # Print the predicted sentiment
        print('The predicted sentiment is', sentiment_classes[yt[0]])

if __name__ == '__main__':
    model_instance = Model()
    model_instance.process_dataframe()
    x, tokens = model_instance.get_tokens()
    model_instance.split_dataframe(x)
    model_instance.save_tokens()
    model_instance.build_model()
    model_instance.compile_model()
    model_instance.train_model()
    model_instance.evaluate_model()
    model_instance.save_model()
    # model_instance.predict_class(['it was a bad experience, This flight is not recommended'])