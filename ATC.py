from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import words

# Download NLTK resources if not already downloaded
import nltk

nltk.download("punkt")
nltk.download("words")

# Create a set of valid English words for reference
valid_word_set = set(words.words())


def auto_correct(text):
    corrected_tokens = []
    tokens = word_tokenize(text)

    for token in tokens:
        # Check if the token is a valid word or needs correction
        if token.lower() in valid_word_set:
            corrected_tokens.append(token)
        else:
            # Use TextBlob for autocorrection
            corrected_word = TextBlob(token).correct()
            corrected_tokens.append(str(corrected_word))

    corrected_text = " ".join(corrected_tokens)
    return corrected_text


# Test the auto-correct tool
user_input = input("Enter a sentence: ")
corrected_sentence = auto_correct(user_input)

print(f"Auto-corrected sentence: {corrected_sentence}")
