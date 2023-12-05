'''
genérer le faux fichier pour les tests
'''
from faker import Faker

fake = Faker()

with open("fake_file.txt", "w") as f:
    for i in range(10):
        f.write(f"{fake.text()}\n")