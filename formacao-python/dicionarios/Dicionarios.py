from collections import Counter

letra = """"
Where have you been?
Been searching all along
Came facing twilight on and on
Without a clue
Without a sign
Without grasping yet
The real question to be asked
Where have I been?
I'm a shape shifter
At Poe's masquerade
Hiding both face and mind
All free for you to draw
I'm a shape shifter
What else should I be?
Please don't take off my mask
Revealing dark
Moments of calm
Nothing left to be found
A mirror right in front of me
That's where I find
An empty glass
Reflecting the sad truth
It's telling words not to be told
I need the mask
I'm a shape shifter
At Poe's masquerade
Hiding both face and mind
All free for you to draw
I'm a shape shifter
Chained down to my core
Please don't take off my mask
My place to hide
I can't tell you
How to see me
Just a cage of bones
There's nothing inside
Will it unleash me?
Burning down the walls
Is there a way
For me to break?
I'm a shape shifter
At Poe's masquerade
Hiding both face and mind
All free for you to draw
I'm a shape shifter
Have no face to show
Please don't take off my mask
My disguise
"""
palavras = letra.title().split()
letras = [letraI.upper() for letraI in letra]
counter = Counter(letras)

for letraI, valor in counter.most_common():
    print(f'{letraI}: {valor}')

print("-"*200)

Url = {
    "protocolo": "https://",
    "base": "google.com/search",
    "parametros": "?query=palavraDaBusca",
}

print(Url)

resultadoBusca = Url.get("parametros", "valorDefault")
print(resultadoBusca)