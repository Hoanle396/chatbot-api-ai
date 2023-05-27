import numpy as np
import pickle
import json

class Model(object):
    def __init__(self):
        self.vocab = []
        self.word2index = {}
        self.index2word = {}
        self.weights_1 = None
        self.weights_2 = None

    def train(self, training_data, learning_rate=0.1, epochs=1000):
        self.build_vocab(training_data)
        training_inputs, training_outputs = self.convert_data(training_data)
        input_size = len(self.vocab)
        hidden_size = 16
        output_size = len(self.vocab)

        np.random.seed(42)
        self.weights_1 = 2 * np.random.random((input_size, hidden_size)) - 1
        self.weights_2 = 2 * np.random.random((hidden_size, output_size)) - 1

        for epoch in range(epochs):
            for input_vector, output_vector in zip(training_inputs, training_outputs):
                hidden_layer, output_layer = self.forward(input_vector)

                output_error = output_vector - output_layer
                output_delta = output_error * self.sigmoid_derivative(output_layer)

                hidden_error = np.dot(output_delta, self.weights_2.T)
                hidden_delta = hidden_error * self.sigmoid_derivative(hidden_layer)

                self.backward(
                    input_vector,
                    hidden_layer,
                    output_delta,
                    hidden_delta,
                    learning_rate,
                )

    def predict(self, input_text):
        input_vector = np.zeros(len(self.vocab))
        tokens = input_text.lower().split()
        for token in tokens:
            if token in self.word2index:
                input_vector[self.word2index[token]] = 1

        hidden_layer, output_layer = self.forward(input_vector)

        output_vector = output_layer.tolist()
        predicted_indices = [i for i, v in enumerate(output_vector) if v > 0.5]
        predicted_words = [self.index2word[index] for index in predicted_indices]
        return predicted_words

    def forward(self, input_vector):
        hidden_layer = self.sigmoid(np.dot(input_vector, self.weights_1))
        output_layer = self.sigmoid(np.dot(hidden_layer, self.weights_2))

        return hidden_layer, output_layer

    def backward(
        self, input_vector, hidden_layer, output_delta, hidden_delta, learning_rate
    ):
        self.weights_2 += learning_rate * np.outer(hidden_layer, output_delta)
        self.weights_1 += learning_rate * np.outer(input_vector, hidden_delta)

    def build_vocab(self, training_data):
        for data in training_data:
            patterns = data["patterns"]
            for pattern in patterns:
                tokens = pattern.split()
                for token in tokens:
                    if token.lower() not in self.vocab:
                        self.vocab.append(token.lower())

            responses = data["responses"]
            for response in responses:
                tokens = response.split()
                for token in tokens:
                    if token.lower() not in self.vocab:
                        self.vocab.append(token.lower())

        self.word2index = {word: index for index, word in enumerate(self.vocab)}
        self.index2word = {index: word for index, word in enumerate(self.vocab)}

    def convert_data(self, training_data):
        training_inputs = []
        training_outputs = []

        for data in training_data:
            patterns = data["patterns"]
            responses = data["responses"]

            for pattern in patterns:
                input_vector = np.zeros(len(self.vocab))
                tokens = pattern.split()
                for token in tokens:
                    if token.lower() in self.word2index:
                        input_vector[self.word2index[token.lower()]] = 1
                training_inputs.append(input_vector)

            for response in responses:
                output_vector = np.zeros(len(self.vocab))
                tokens = response.split()
                for token in tokens:
                    if token.lower() in self.word2index:
                        output_vector[self.word2index[token.lower()]] = 1
                training_outputs.append(output_vector)

        return training_inputs, training_outputs

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def save_model(self, file_path):
        model_data = {
            'vocab': self.vocab,
            'word2index': self.word2index,
            'index2word': self.index2word,
            'weights_1': self.weights_1.tolist(),
            'weights_2': self.weights_2.tolist()
        }

        with open(file_path, 'wb') as file:
            pickle.dump(model_data, file)

    def load_model(self, file_path):
        with open(file_path, 'rb') as file:
            model_data = pickle.load(file)

        self.vocab = model_data['vocab']
        self.word2index = model_data['word2index']
        self.index2word = model_data['index2word']
        self.weights_1 = np.array(model_data['weights_1'])
        self.weights_2 = np.array(model_data['weights_2'])

# train model
# chatbot = Model()

# with open("D:/Code/final/src/models/data/data.json", "r") as file:
#     training_data = json.load(file)["intents"]


# chatbot.train(training_data)
# chatbot.save_model('models.pkl')