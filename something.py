from keras.dataset import mnist
import matplotlib.pyplot as plt

# load dataset, download if needed
(X_train, y_train), (X_test, y_test) = mnist.load_data()

plt.subplot(221)