import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, InputLayer
from keras.optimizers import RMSprop

import matplotlib.pyplot as plt

(x_train2, y_train), (x_test2, y_test) = mnist.load_data()
print("x_train.shape(学習用の画像データ) : ", x_train2.shape)
print("y_train.shape(学習用の正解データ) : ", y_train.shape)
print("x_test.shape(検証用の画像データ) : ", x_test2.shape)
print("y_test.shape(検証用の正解データ) : ", y_test.shape)

x_train = x_train2.reshape(60000, 784)
x_test = x_test2.reshape(10000, 784)

print("x_train.shape(学習用の画像データ) : ", x_train.shape)
print("y_train.shape(学習用の正解データ) : ", y_train.shape)
print("x_test.shape(検証用の画像データ) : ", x_test.shape)
print("y_test.shape(検証用の正解データ) : ", y_test.shape)

# データをfloat型に変換
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# 0〜255までの範囲のデータを0〜1までの範囲に変換
x_train /= 255
x_test /= 255

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

print("x_train.shape(学習用の画像データ) : ", x_train.shape)
print("y_train.shape(学習用の正解データ) : ", y_train.shape)
print("x_test.shape(検証用の画像データ) : ", x_test.shape)
print("y_test.shape(検証用の正解データ) : ", y_test.shape)

# モデルの構築
model = Sequential()
model.add(InputLayer(input_shape=(784,)))
model.add(Dense(10, activation='softmax'))
#model.add(Dense(10, activation='relu'))

# モデルのコンパイル
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# 学習
epochs = 10
batch_size = 128
history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))

# 評価
score = model.evaluate(x_test, y_test, verbose=1)
print()
print('Test loss:', score[0])
print('Test accurancy:', score[1])

# 学習結果の保存
model_json_str = model.to_json()
open('mnist_mlp_model.json', 'w').write(model_json_str)
model.save_weights('mnist_mlp_weights.h5');


# 学習経過の可視化
loss = history.history['loss']
val_loss = history.history['val_loss']

nb_epoch = len(loss)
plt.plot(range(nb_epoch), loss, marker='.', label='loss')
plt.plot(range(nb_epoch), val_loss, marker='.', label='val_loss')
plt.legend(loc='best', fontsize=10)
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

