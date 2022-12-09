import numpy as np
import util

from p01b_logreg import LogisticRegression

# Character to replace with sub-problem letter in plot_path/pred_path
WILDCARD = 'X'


def main(train_path, valid_path, test_path, pred_path):
    """Problem 2: Logistic regression for incomplete, positive-only labels.

    Run under the following conditions:
        1. on y-labels,
        2. on l-labels,
        3. on l-labels with correction factor alpha.

    Args:
        train_path: Path to CSV file containing training set.
        valid_path: Path to CSV file containing validation set.
        test_path: Path to CSV file containing test set.
        pred_path: Path to save predictions.
    """
    pred_path_c = pred_path.replace(WILDCARD, 'c')
    pred_path_d = pred_path.replace(WILDCARD, 'd')
    pred_path_e = pred_path.replace(WILDCARD, 'e')

    # *** START CODE HERE ***
    # Part (c): Train and test on true labels

    x_train,t_train=util.load_dataset(train_path,label_col='t',add_intercept=True)
    x_test,t_test=util.load_dataset(test_path,label_col='t',add_intercept=True)
    model = LogisticRegression()
    model.fit(x_train,t_train)

    util.plot(x_test,t_test,model.theta,'output/p02c.png')
    t_predict = model.predict(x_test)
    # Make sure to save outputs to pred_path_c
    np.savetxt(pred_path_c,t_predict>0.5,fmt='%d')


    # Part (d): Train on y-labels and test on true labels
   
    x_train,y_train=util.load_dataset(train_path,label_col='y',add_intercept=True)
    x_test,y_test=util.load_dataset(test_path,label_col='y',add_intercept=True)
    model = LogisticRegression()
    model.fit(x_train,y_train)

    util.plot(x_test,y_test,model.theta,'output/p02d.png')
    y_predict = model.predict(x_test)
     # Make sure to save outputs to pred_path_d
    np.savetxt(pred_path_d,y_predict>0.5,fmt='%d')

    # Part (e): Apply correction factor using validation set and test on true labels
    x_valid,y_valid=util.load_dataset(valid_path,label_col='y',add_intercept=True)
    alpha= np.mean(model.predict(x_valid))
    
    util.plot(x_test,y_test,model.theta,'output/p02e.png',correction=1+np.log(2/alpha-1)/model.theta[0])#in regard of decision boundary
    y_predict = model.predict(x_test)
    t_predict=y_predict/ alpha
    # Plot and use np.savetxt to save outputs to pred_path_e
    np.savetxt(pred_path_e,t_predict>0.5,fmt='%d')
    # *** END CODER HERE
