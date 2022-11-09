import numpy as np


def split_data(x, y, validate_percent=.20, test_percent=.20, seed=None):
    if seed is None:
        random = np.random
    else:
        random = np.random.RandomState(seed=seed)

    length = len(x)
    indexs = random.permutation(length)
    train_end = int((1 - (validate_percent + test_percent)) * length)
    validation_end = int((1 - test_percent) * length)
    train_indexs = indexs[:train_end]
    validate_indexs = indexs[train_end:validation_end]
    test_indexs = indexs[validation_end:]
    x_train = x[train_indexs]
    y_train = y[train_indexs]
    x_validate = x[validate_indexs]
    y_validate = y[validate_indexs]
    x_test = x[test_indexs]
    y_test = y[test_indexs]
    return x_train, y_train, \
        x_validate, y_validate, \
        x_test, y_test, \
        train_indexs, validate_indexs, \
        test_indexs

