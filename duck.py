import random

# Lists of duck phrases, facts, and quacks
duck_advice = [
    "Just keep paddling!",
    "Quack it off and move on!",
    "If it fits, you sits. If it doesn’t fit, just waddle.",
    "Remember, bread is a sometimes snack!",
    "When in doubt, just flap it out!",
    "Why fly south when you can stay here and quack together?"
]

duck_facts = [
    "Did you know? Ducks have waterproof feathers!",
    "Fun fact: Ducks don’t echo. It’s a mystery.",
    "Ducks can sleep with one eye open.",
    "Some ducks can dive as deep as 20 feet underwater!",
    "Baby ducks are called 'ducklings,' and they are too cute for words!"
]

random_quacks = ["Quack!", "Quackity-quack!", "Qwaaaack!", "QUACK QUACK!"]

def consult_duck():
    advice = random.choice(duck_advice)
    fact = random.choice(duck_facts)
    quack = random.choice(random_quacks)
    return f"{advice} {quack} Here's a fun fact: {fact}"

# Consult the Emotional Support Duck
print(consult_duck())
