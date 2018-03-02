import tensorflow as tf
import numpy as np
import os
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten, Activation, GlobalMaxPooling2D
from keras.layers.core import Flatten, Dense, Dropout
from keras.layers.convolutional import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.applications.vgg19 import VGG19

import matplotlib.pyplot as plt

input_shape = (405, 270, 3)
batch_size = 8
epochs = 10

# training_directory = os.getcwd() + '\DataSubset\TrainImages'
# test_directory = os.getcwd() + '\DataSubset\TestImages'
# num_classes = 70
# train_samples = 27992
# test_samples = 7000

training_directory = os.getcwd() + '\SmallDataSubset\TrainImages'
test_directory = os.getcwd() + '\SmallDataSubset\TestImages'
num_classes = 3
train_samples = 9578
test_samples = 2415
target_shape = (405, 270)
# target_shape = (244, 244)

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

train_generator = train_datagen.flow_from_directory(training_directory, target_size=target_shape, batch_size=batch_size)

test_generator = ImageDataGenerator(rescale=1./255).flow_from_directory(test_directory, target_size=target_shape,
                                                                        batch_size=batch_size)


def create_short_model():
    model = Sequential()
    model.add(Conv2D(128, (3, 3), padding='same', activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(128, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='sigmoid'))

    return model


# def vgg_19(weights_path=None, include_top=False):
#     model = Sequential()
#     model.add(Conv2D(64, (3, 3), padding='same', activation='relu', input_shape=input_shape))
#     model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
#     model.add(MaxPooling2D((2,2), strides=(2,2)))
#
#     model.add(Conv2D(128, (3, 3), padding='same', activation='relu'))
#     model.add(Conv2D(128, (3, 3), padding='same', activation='relu'))
#     model.add(MaxPooling2D((2,2), strides=(2,2)))
#
#     model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
#     model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
#     model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
#     model.add(Conv2D(256, (3, 3), padding='same', activation='relu'))
#     model.add(MaxPooling2D((2,2), strides=(2,2)))
#
#     model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))
#     model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))
#     model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))
#     model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))
#     model.add(MaxPooling2D((2,2), strides=(2,2)))
#
#     model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))
#     model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))
#     model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))
#     model.add(Conv2D(512, (3, 3), padding='same', activation='relu'))
#     model.add(MaxPooling2D((2,2), strides=(2,2)))
#
#     if include_top:
#         model.add(Flatten())
#         model.add(Dense(4096, activation='relu'))
#         model.add(Dropout(0.5))
#         model.add(Dense(4096, activation='relu'))
#         model.add(Dropout(0.5))
#         model.add(Dense(num_classes, activation='softmax'))
#     else:
#         model.add(GlobalMaxPooling2D())
#
#     if weights_path:
#         model.load_weights(weights_path)
#
#     return model


# model = create_model()
model = create_short_model()
# model = vgg_19()
# model = VGG19()

print(model.summary())

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit_generator(train_generator,
                              steps_per_epoch=train_samples // batch_size,
                              epochs=epochs,
                              validation_data=test_generator,
                              validation_steps=test_samples // batch_size)

model.save_weights('brandon2.h5')

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
