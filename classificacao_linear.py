from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
import numpy as np

np.random.seed(46)

X, Y = make_classification(
    n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1
)
print(X)
print(Y)
plt.scatter(X[:, 0], X[:, 1], marker='o', c=Y)

#setar xmin, xmax, ymin, ymax usando os axis
xmin, xmax, ymin, ymax = plt.axis()
plt.xlim(xmin=xmin, xmax=xmax)
plt.ylim(ymin=ymin, ymax=ymax)

plt.savefig('imagem_classificacao.png')

p = X[10]
plt.plot(p[0], p[1], marker='o', markersize=20, color="red")
plt.savefig('imagem_classificacao2.png')


def plotline(w1, w2, b):
    #ax +bx +c = 0
    x = np.linspace(-2,4,50)

    #y = (-a*x -c)/b
    y = (-w1*x -w2)/w2
    print(x)

    plt.axvline(0, color='black')
    plt.axhline(0, color='black')
    plt.plot(x,y)
    plt.grid(True)

w1 = 3
w2 = 1
b = 0

plotline(w1, w2, b)
plt.savefig('imagem_classificacao3.png')

def classify(ponto, w1, w2, b):
    ret = w1*ponto[0] + w2*ponto[1] + b

    if ret >= 0:
        return 1, "red"
    else:
        return 0, "blue"

p = (2, -1)
classe, cor = classify(p, w1, w2, b)
plt.plot(p[0], p[1], marker='o', markersize=20, color=cor)
plt.savefig('imagem_classificacao4.png')

acertos = 0
for k in range(len(X)):
    p = X[k]
    classe, cor = classify(p, w1, w2, b)
    plt.plot(p[0], p[1], marker='o', markersize=20, color=cor)
    if classe == Y[k]:
        acertos +=1
    
print('Acurácia: %d' % (100*acertos/len(X)))
