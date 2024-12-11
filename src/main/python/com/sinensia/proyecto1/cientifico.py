#/usr/bin/python
NITROGENO = -196

#Con listas
items = [35, 523, 56, 234, 1, -34, -53, -254, -48, -315]
temperaturas = []
temperaturas = [item for item in items if (item > NITROGENO)]
print(temperaturas)