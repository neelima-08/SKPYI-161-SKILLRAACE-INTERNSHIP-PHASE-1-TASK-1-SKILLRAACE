import demoji

demoji.download_codes()

def convert_emoji_to_text(text):
    return demoji.replace_with_desc(text, ":{desc}:")

text_with_emojis = "I love playing cricket 🏏 and dice🎲!"
text_with_emoji_desc = convert_emoji_to_text(text_with_emojis)

print(text_with_emoji_desc)