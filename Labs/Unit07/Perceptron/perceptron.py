"""
A class that creates a basic perceptron 
to perform binary classification.
"""

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=300):
        """
        Initializes a perceptron.
        Args:
            input_size (int): The number of features used for input
            learning_rate (float, optional): Defaults to 0.1.
            epochs (int, optional): Defaults to 300.
        """
        self.epochs = epochs
        self.learning_rate = learning_rate

        # Initialize weights to 0
        self.weights = [0] * input_size

        # Initialize bias to 0
        self.bias = 0
        
    
    def forward_propagation(self, features):
        """
        Uses forward propagation to make a prediction.
        Takes a single row as input (1 sample).

        Args:
            features (list): The features used as 
            inputs to the model (from a single row)

        Returns:
            int: Returns a prediction [0, 1]
        """
        sum = 0
        for i in range(0, len(features)):
            sum += self.weights[i] * features[i]
        return 1 if sum > self.bias else 0
    
    def back_propagation(self, features, label, prediction):
        """
        Updates the weights based off errors using
        backpropagation
        Args:
            features (list): The features used as 
            inputs to the model (from a single row)
            label (int): Actual label for the data [0, 1]
            prediction (int): The predicted value [0, 1]
        """
        for i in range(0, len(features)):
            self.weights[i] += self.learning_rate * (label - prediction) * features[i]
        self.bias += self.learning_rate * (label - prediction) * -1
    
    def run_epoch(self, training_data, labels):
        """
        Runs a single epoch
        Args:
            training_data (list): A list of lists of features 
            (multiple rows of data)
            labels (list): The true labels of the data
        """
        for i in range(0, len(labels)):
            prediction = self.forward_propagation(training_data[i])
            self.back_propagation(training_data[i], labels[i], prediction)
    
    def train(self, training_data, labels):
        """
        Runs multiple epochs to train the perceptron
        Args:
            training_data (list): A list of lists of features 
            (multiple rows of data)
            labels (list): The true labels of the data
        """
        for i in range(self.epochs):
            self.run_epoch(training_data, labels)
        
    def predict(self, data):
        """
        Makes predictions on multiple rows of data
        Args:
            data (list): A list of lists of features 
            (multiple rows of data)
        Returns:
            list: A list of predicted values
        """
        predictions = []
        for i in range(len(data)):
            predictions.append(self.forward_propagation(data[i]))
        
        return predictions
    
    def score(self, labels, predictions):
        """
        Calculates model accuracy based on 
        # correct predictions / # total predictions
        Args:
            labels (list): The true labels
            predictions (list): The predicted labels

        Returns:
            float: Accuracy
        """
        # Count rows where one column == 1 and the other == 0
        return 1 - sum(abs(predictions - labels)) / len(labels)
