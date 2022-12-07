import numpy as np
import util

from linear_model import LinearModel


def main(train_path, eval_path, pred_path):
    """Problem 1(e): Gaussian discriminant analysis (GDA)

    Args:
        train_path: Path to CSV file containing dataset for training.
        eval_path: Path to CSV file containing dataset for evaluation.
        pred_path: Path to save predictions.
    """
    # Load dataset
    x_train, y_train = util.load_dataset(train_path, add_intercept=False)
    # *** START CODE HERE ***
    model=GDA()
    model.fit(x_train,y_train)
    util.plot(x_train, y_train, model.theta,'output/p01e_{}.png'.format(pred_path[-5]))
    x_eval,_=util.load_dataset(eval_path,add_intercept=False)
    y_predict=model.predict(x_eval)
    np.savetxt(pred_path,y_predict>0.5,fmt="%d")

    # *** END CODE HERE ***


class GDA(LinearModel):
    """Gaussian Discriminant Analysis.

    Example usage:
        > clf = GDA()
        > clf.fit(x_train, y_train)
        > clf.predict(x_eval)
    """

    def fit(self, x, y):
        """Fit a GDA model to training set given by x and y.

        Args:
            x: Training example inputs. Shape (m, n).
            y: Training example labels. Shape (m,).

        Returns:
            theta: GDA model parameters.
        """
        # *** START CODE HERE ***
        m, n = x.shape  # dimensions
        self.theta = np.zeros(n+1) #Initial guess for theta
        y_1= sum(y==1)
        phi= y_1/m
        mu_0=np.sum(x[y==0],axis=0)/(m-y_1)
        mu_1=np.sum(x[y==1],axis=0)/y_1
        Sigma=((x[y == 0] - mu_0).T.dot(x[y == 0] - mu_0) + (x[y == 1] - mu_1).T.dot(x[y == 1] - mu_1)) / m

        Sigma_inv=np.linalg.inv(Sigma)
        self.theta[0]=0.5 * (mu_0 + mu_1).dot(Sigma_inv).dot(mu_0 - mu_1) - np.log((1 - phi) / phi)
        self.theta[1:] = Sigma_inv.dot(mu_1 - mu_0)
        return self.theta
        # *** END CODE HERE ***

    def predict(self, x):
        """Make a prediction given new inputs x.

        Args:
            x: Inputs of shape (m, n).

        Returns:
            Outputs of shape (m,).
        """
        # *** START CODE HERE **
        return 1 / (1+np.exp(-x.dot(self.theta)))
        # *** END CODE HERE
