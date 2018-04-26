#import keras
#from keras.datasets import mnist
from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np
import glob as gb

'''
保存したモデルと学習結果を再評価する為のロジックだが、通常は不要
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_test = x_test.reshape(10000, 784)

# データをfloat型に変換
x_test = x_test.astype('float32')

# 0〜255までの範囲のデータを0〜1までの範囲に変換
x_test /= 255

y_test = keras.utils.to_categorical(y_test, 10)
'''
# モデルを読み込む
model = model_from_json(open('mnist_mlp_model.json').read())

# 学習結果を読み込む
model.load_weights('mnist_mlp_weights.h5')

# モデルのコンパイル
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

'''
保存したモデルと学習結果を再評価する為のロジックだが、通常は不要
# 評価
score = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', score[0])
print('Test accurancy:', score[1])
'''

# 手描き数字の読み込み、予測
for predict_file in gb.glob('data/pngBold/*.*'):

    # 手描き数字の画像ファイルをグレースケールで、28×28ピクセルで読み込み配列変換する。
    img = image.load_img(predict_file, grayscale=True, target_size=(28, 28))
    x = image.img_to_array(img)
    # MNISTデータ同様の変換を行うが、白（255）黒（0）の値がMNISTと反対なので、逆転させる。
    x = x.astype('float32')
    x = abs(x - 255)
    x = x.reshape(1, 784)
    x /= 255
    
    # 手描き数字の予測
    features = model.predict(x, verbose=0)
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format}) #桁を揃える
    # 予測結果の表示
    print()
    print("予測する画像は:", predict_file)
    print("予測結果（0〜9の確率）は:", features)
    print("予測した数字は:", np.argmax(features))
