comi=["combo","sawich","pizza"]
comi.append("gaseosa")
comi.extend(["malteada","perro","perro caliente"])
comi.sort()
print(comi)
print(len(comi))
for i, e in enumerate(comi):
    print(i,e)
comi.insert(2,"empanada")
for i, e in enumerate(comi):
    print(i,e)
print(comi)
comi.remove("gaseosa")
comi.reverse()
print(comi)
del comi[0]
comi.sort(reverse=True)
print(comi)
comi.pop()

print(comi)
#posision
print(comi.index("malteada"))
#borrar
comi.clear()
print(comi)

