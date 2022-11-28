import numpy as np
import util

from linear_model import LinearModel


def main(train_path, eval_path, pred_path):
    """Problem 1(b): Logistic regression with Newton's Method.

    Args:
        train_path: Path to CSV file containing dataset for training.
        eval_path: Path to CSV file containing dataset for evaluation.
        pred_path: Path to save predictions.
    """
    x_train, y_train = util.load_dataset(train_path, add_intercept=True)
    # np.savetxt(pred_path, x_train, fmt='%d')
    # *** START CODE HERE ***
    model = LogisticRegression(eps=1e-5)
    model.fit(x_train, y_train)

    util.plot(x_train, y_train, model.theta,
              'output/p01b_{}.png'.format(pred_path[-5]))

    x_eval, y_eval = util.load_dataset(eval_path, add_intercept=True)
    y_predict = model.predict(x_eval)
    np.savetxt(pred_path, y_predict > 0.5, fmt='%d')
    # *** END CODE HERE ***


class LogisticRegression(LinearModel):
    """Logistic regression with Newton's Method as the solver.

    Example usage:
        > clf = LogisticRegression()
        > clf.fit(x_train, y_train)
        > clf.predict(x_eval)
    """

    def fit(self, x, y):
        """Run Newton's Method to minimize J(theta) for logistic regression.

        Args:
            x: Training example inputs. Shape (m, n). (800, 3)
            y: Training example labels. Shape (m,).   (800,)
        """
        # *** START CODE HERE ***
        m, n = x.shape  # dimensions
        self.theta = np.zeros(n) #Initial guess for theta

        # Hessian Matrix
        # Quoted from Lecture Note1 P21
        while True:
            theta_ = np.copy(self.theta)
            g_x = 1/(1+np.exp(-x.dot(theta_)))
            H = (g_x * (1-g_x) * x.T).dot(x) / m
            gradient_J_theta = x.T.dot(g_x-y) / m

            self.theta -= np.linalg.inv(H).dot(gradient_J_theta)

            if np.linalg.norm(self.theta-theta_, ord=1) < self.eps:
                break


# *** END CODE HERE ***

    def predict(self, x):  # indent
        """Make a prediction given new inputs x.

            Args:
                x: Inputs of shape (m, n).

            Returns:
                Outputs of shape (m,).
            """
        # *** START CODE HERE ***

        return 1 / (1+np.exp(-x.dot(self.theta)))

        # *** END CODE HERE ***
