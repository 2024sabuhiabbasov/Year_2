class ipv4machine:

    @property
    def generator(self):
        return [f"{i}.{j}.{k}.{l}" for i in range(256) for j in range(256) for k in range(256) for l in range(256)]


ipv4 = ipv4machine()
output = ipv4.generator
print(output)
