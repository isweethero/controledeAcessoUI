# controledeAcessoUI - Python3

requisitos:
```
python3
pyzbar
servidor mysql
```

instalando dependências:
```
apt install libzbar0
pip install -r req.txt
```
crie um arquivo no direitorio com o nome de "config" contendo:
```
ip
usuário
senha
nome da database
nome da tabela para ser usada como controle de usuários
nome da tabela para ser armazenada as entradas dos usuários
```
pode ser necessário mudar a entrada de vídeo:
```
linha 260:
self.capture=VideoStream(src=0).start()
mude o valor de src

para a câmera do pi:
self.capture=VideoStream(usePiCamera=True).start()

```
