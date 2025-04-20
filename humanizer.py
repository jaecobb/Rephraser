import random

# Word replacement dictionary for rephrasing
REPLACEMENTS = {
    "I think": "In my opinion",
    "because": "since",
    "also": "additionally",
    "but": "however",
    "so": "therefore",
    "very": "extremely",
    "difficult": "challenging"
}

# Optional intro phrases to add human-like tone
HUMAN_PHRASES = ["honestly", "to be real", "I guess", "in my case"]

def rephrase(text):
    """Replace predefined words/phrases with alternatives."""
    for target, replacement in REPLACEMENTS.items():
        text = text.replace(target, replacement)
    return text

def add_human_intro(text):
    """Randomly prepend a casual phrase for a natural tone."""
    if random.random() > 0.5:
        intro = random.choice(HUMAN_PHRASES)
        return f"{intro}, {text}"
    return text

def split_into_sentences(text, word_counts):
    """Split the text into sentences with given word counts."""
    words = text.split()
    sentences = []
    idx = 0

    for count in word_counts:
        end = idx + count
        if end <= len(words):
            sentence = " ".join(words[idx:end]).capitalize()
            sentences.append(sentence)
            idx = end
        else:
            break  # Not enough words left
    return '. '.join(sentences) + '.'

def main():
    user_input = input("Enter text to rephrase:\n> ").strip()
    word_counts_input = input("Enter the word counts for each sentence (space-separated):\n> ")
    word_counts = list(map(int, word_counts_input.strip().split()))

    modified = rephrase(user_input)
    humanized = add_human_intro(modified)
    normalized = " ".join(humanized.split())  # Clean up spaces
    result = split_into_sentences(normalized, word_counts)

    print("\nHumanized output (custom word counts):\n", result)

if __name__ == "__main__":
    main()
