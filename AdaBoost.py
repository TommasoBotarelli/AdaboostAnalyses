import numpy as np


class DecisionStump:

    def __init__(self):
        self.feature_id = None
        self.threshold = None
        self.alpha = None
        self.polarity = 1

    def predict(self, x):
        n_samples = x.shape[0]
        x_column = x.iloc[:, self.feature_id]

        predictions = np.ones(n_samples)
        if self.polarity == 1:
            predictions[x_column < self.threshold] = -1
        else:
            predictions[x_column > self.threshold] = -1

        return predictions


class Adaboost:

    def __init__(self, max_iter, n_random_choice, categorical):
        self.max_iter = max_iter
        self.n_random_choice = n_random_choice
        self.weak_learners = []
        self.training_pred = []
        self.testing_pred = []
        self.categorical = categorical

    def training_predict(self, x_train, y_train, x_test):
        n_samples, n_feature = x_train.shape
        n_feature += -1

        w = np.full(n_samples, (1/n_samples))
        for i in range(self.max_iter):
            decision_stump, error = self.get_decision_stump(x_train, y_train, w)

            eps = 1e-15

            decision_stump.alpha = 0.5 * np.log((1 - error) / (error + eps))

            predictions = decision_stump.predict(x_train)

            w = w * (np.exp(-decision_stump.alpha * y_train.astype(float) * predictions))
            w = w / (np.sum(w))

            self.weak_learners.append(decision_stump)
            self.training_pred.append(self.predict(x_train))
            self.testing_pred.append(self.predict(x_test))

    def get_decision_stump(self, x, y, w):
        decision_stump = DecisionStump()
        error = 0

        n_samples, n_feature = x.shape

        min_error = float('inf')

        for feature_i in range(n_feature):
            x_column = x.iloc[:, feature_i]

            if self.categorical:
                thresholds = np.unique(x_column)
            else:
                thresholds = self.get_random_numerical_threshold(x_column)

            for threshold in thresholds:
                p = 1
                predictions = np.ones(n_samples)
                predictions[x_column < threshold] = -1

                weighed_miss = w[y != predictions]
                error = sum(weighed_miss)

                if error > 0.5:
                    error = 1-error
                    p = -1

                if error < min_error:
                    min_error = error
                    decision_stump.polarity = p
                    decision_stump.threshold = threshold
                    decision_stump.feature_id = feature_i

        return decision_stump, min_error

    def predict(self, x):
        predictions = [weak_learner.alpha * weak_learner.predict(x) for weak_learner in self.weak_learners]
        predictions_y = np.sign(sum(predictions))
        return predictions_y

    def get_random_numerical_threshold(self, x_column):
        all_threshold = np.unique(x_column)
        np.random.seed(self.n_random_choice)
        return np.random.choice(all_threshold, self.n_random_choice)
