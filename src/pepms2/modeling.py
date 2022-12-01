import keras.backend as K
from keras.models import load_model as keras_load_model
from keras.models import Sequential
from keras.regularizers import l2

try:
    from keras.layers import Conv1D, \
        Dense, Dropout, Masking, LSTM, Bidirectional, TimeDistributed, Flatten, Reshape, Activation
except ImportError:
    from keras.layers.convolutional import Conv1D
    from keras.layers.core import Dense, Dropout, Masking
    from keras.layers.recurrent import LSTM
    from keras.layers.wrappers import Bidirectional, TimeDistributed


def cosine_similarity(y_true, y_pred):
    length = K.int_shape(y_pred)[1]
    y_true = K.batch_flatten(y_true)
    y_pred = K.batch_flatten(y_pred)
    y_true = K.l2_normalize(y_true, axis=-1)
    y_pred = K.l2_normalize(y_pred, axis=-1)
    cos = K.sum(y_true * y_pred, axis=-1, keepdims=True)
    result = -K.repeat_elements(cos, rep=length, axis=1)
    return result


def build_model(options, metrics=[cosine_similarity]):
    model = Sequential()
    model.add(Flatten())
    model.add(Dense((options.max_sequence_length-1)*options.intensity_size(), kernel_regularizer=l2(0.01)))
    model.add(Reshape(((options.max_sequence_length-1), options.intensity_size())))
    model.add(Activation('linear'))
    model.compile(
        loss='squared_hinge',
        optimizer="adadelta",
        metrics=metrics
    )
    return model


def load_model(file, custom_objects={'cosine_similarity': cosine_similarity},
               **kwargs):
    model = keras_load_model(file, custom_objects=custom_objects, **kwargs)
    return model


def build_model_from_weights(options, weights_path, **kwargs):
    model = build_model(options=options, **kwargs)
    model.load_weights(weights_path)
    return model

