class Flashcard:
    def __init__(self, word, meaning):
        self.word = meaning
        self.meaning = meaning
    def __str__(self):
        return f"{self.word} ({self.meaning})"
flashcards = []
print("Welcome to the Flashcard Application!")
while True:
    word = input("Enter the word: ").strip()
    meaning = input("Enter the meaning: ").strip()
    if word and meaning:
        flashcards.append(Flashcard(word, meaning))
    else:
        print("Blank entries are not allowed.")
    if input("Add another flashcard? (y/n): ").lower() != 'y':
        break
print("\nYour Flashcards:")
for card in flashcards:
    print(">", card)