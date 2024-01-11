import torch
import numpy as np

lista = [[1,2,3],[4,5,6]]
tensor = torch.tensor(lista)
print(tensor)
print(tensor.dtype)

tensor = torch.DoubleTensor(lista)
print(tensor)
print(tensor.dtype)

tensor = torch.FloatTensor(lista)
print(tensor)
print(tensor.dtype)

arr = np.random.rand(3,4)
tns = torch.from_numpy(arr)
print(tns)

print(torch.ones(3,3))
print(torch.zeros(2,3))
print(torch.randn(2,3))

tnsr = torch.randn(2,3)
tns = torch.ones(3,3)
arr = tns.data.numpy()
print(arr)
print(type(tns))
print(type(arr))

#estrutura mutavel
tns[0,2] = 0
print(tns)

print(tns[0:2])
print(tns[:,2])

#operacoes
print(tns.shape)
print(tnsr.shape)

tns = tns[0:2,:]

print(tns.shape)
print(tnsr.shape)
print(tns)
print(tnsr)
print(tns + tnsr)
print(tns * tnsr)

tns = torch.randn(2,2,3)
print(tns)
print(tns.size())
print(tns.view(12))
print(tns.view(4,3))

if torch.cuda.is_available():
    print('GPU disponivel')
    device = torch.device('cuda')
else:
    print('GPU indisponivel')
    device = torch.device('cpu')
print(device)

tns = tns.to(device)
print(tns)

tnsr = torch.randn(2,2,3)
tns_out = torch.cat( (tns, tnsr), dim=0 )

print(tns_out)

tns = torch.randn(9, 12)
tns1 = tns[0:5, 0:4]
tns2 = tns[5:, 4:]
print(tns1)
print(tns2)
resultado = torch.mm(tns1, tns2)
print(resultado.size())
print(resultado)

tns1 = torch.randn(7,7,3)
tns2 = torch.randn(147, 1)

print(tns1)
print(tns2)
tns1 = tns1.view(-1, 1)
soma = tns1 + tns2
print(soma)