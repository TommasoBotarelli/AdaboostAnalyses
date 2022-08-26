import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import timeit

from AdaBoost import Adaboost


class Test:

    def __init__(self, data, name, n_random_choice):
        x_data = data.iloc[:, :data.shape[1] - 1]
        y_data = data.iloc[:, data.shape[1] - 1]

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x_data
                                                                                , y_data
                                                                                , train_size=0.8
                                                                                , random_state=25)
        self.name = name
        self.n_random_choice = n_random_choice

    def run_test_get_result(self, max_iteration, n_random_choice):
        adaboost = Adaboost(max_iter=max_iteration, n_random_choice=n_random_choice, categorical=False)
        start = timeit.default_timer()
        adaboost.training_predict(self.x_train, self.y_train, self.x_test)

        training_accuracy = []
        testing_accuracy = []

        for i in range(1, max_iteration):
            training_accuracy.append(self.accuracy(adaboost.training_pred[i], self.y_train))
            testing_accuracy.append(self.accuracy(adaboost.testing_pred[i], self.y_test))

        stop = timeit.default_timer()

        step = list(range(1, max_iteration))

        plt.plot(step, training_accuracy, color='tab:blue', label='Accuracy on training data')
        plt.plot(step, testing_accuracy, color='tab:orange', label='Accuracy on testing data')

        time = "{:.5f}".format(stop-start)

        plt.legend()
        plt.grid()
        plt.title(label=self.name + ' _ ' + 'Random choice: ' + str(self.n_random_choice) + ' _ ' + time + ' seconds')
        plt.show()

    def accuracy(self, predictions, expectations):
        return np.sum(predictions == expectations) / len(expectations)
