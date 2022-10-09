from time import sleep
import requests
import json
from tqdm import tqdm
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import random
import subprocess

inp = input("The Ingredients you have(for multiple separate them with a space): ").split()
inp = ",+".join(inp)
r = requests.get("https://api.spoonacular.com/recipes/findByIngredients",params={"ingredients":inp,"apiKey":"Your spoonacular API Kay","number":1})
data = json.loads(r.text)
print()
url = data[0]['image']
filename = url.split('/')[-1]
r = requests.get(url, allow_redirects=True)
open(filename, 'wb').write(r.content)
print("Using CPU\nPrinting System info:")
Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
new = [str(item.split("\r")[:-1]) for item in Id]
for i in new:
    print(i[2:-2])

for _ in tqdm(range(random.randint(250,1000))):
	sleep(0.01)

print(f"\nYou Can make : {data[0]['title']}")

imgplot = plt.imshow(mpimg.imread(filename))
print("You just need to get: \n")
for i in range(data[0]["missedIngredientCount"]):
	print("\t- "+data[0]['missedIngredients'][i]['name'])
plt.ion()
plt.show()
input("\nPress Enter to exit: ")
plt.close()
os.remove(filename)
