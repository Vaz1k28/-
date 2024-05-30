container = {}
data = [
    "Ivanenko paper 10",
    "Petrenko pen 5",
    "Ivanenko marker 3",
    "Ivanenko paper 7",
    "Petrenko envelope 20",
    "Ivanenko envelope 5"
]

for entry in data:
    buyer, item, quantity = entry.split()
    quantity = int(quantity)


    if buyer not in container:
        container[buyer] = {}
    if item not in container[buyer]:
        container[buyer][item] = 0

    container[buyer][item] += quantity


for buyer in sorted(container.keys()):
    print(buyer + ":")
    for item in sorted(container[buyer].keys()):
        print(item, container[buyer][item])

