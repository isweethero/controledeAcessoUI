# controledeAcessoUI - Python3
```
apt install libzbar0
pip install -r req.txt
```
crie um arquivo no direitorio com o nome de "db" contendo:
```
ip
usuário
senha
database
```
pode ser necessário mudar a entrada de video:
```
linha 260:
self.capture=VideoStream(src=0).start()
mude o valor de src

para a camera do pi:
self.capture=VideoStream(usePiCamera=True).start()

```
