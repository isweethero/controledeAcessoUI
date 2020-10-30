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
pode ser necessário mudar a entrada de vídeo:
```
linha 260:
self.capture=VideoStream(src=0).start()
mude o valor de src

para a câmera do pi:
self.capture=VideoStream(usePiCamera=True).start()

```
