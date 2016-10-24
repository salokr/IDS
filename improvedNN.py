import numpy
import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD, Adam, RMSprop
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt

seed = 1337
numpy.random.seed(seed)

############################################################
dataframe = pandas.read_csv("OHEncodedTrain.txt", header=None,delimiter='\t')
dataset = dataframe.values
X_train=dataset[:,0:130].astype(float)
Ytrain=dataset[:,130]
encoder = LabelEncoder()
encoder.fit(Ytrain)
encoded_Ytrain = encoder.transform(Ytrain)
dummy_ytrain = np_utils.to_categorical(encoded_Ytrain)

############################################################

dataframe1 = pandas.read_csv("OHEncodedTest.txt", header=None,delimiter='\t')
dataset1 = dataframe1.values
X_test=dataset1[:,0:130].astype(float)
Yy_test=dataset1[:,130]
tencoder = LabelEncoder()
tencoder.fit(Yy_test)
encoded_Ytest = encoder.transform(Yy_test)
Y_test= np_utils.to_categorical(encoded_Ytest)

############################################################
batch_size=15000
nb_classes=5
nb_epoch=20


model = Sequential()
model.add(Dense(512, input_shape=(130,)))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(5))
model.add(Activation('softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])
              
              
history = model.fit(X_train, dummy_ytrain,
                    batch_size=batch_size, nb_epoch=nb_epoch,
                    verbose=1, validation_data=(X_test, Y_test))


score = model.evaluate(X_test, Y_test, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()