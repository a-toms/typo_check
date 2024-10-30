import language_tool_python
import re
import requests

# Initialize LanguageTool for American English
tool = language_tool_python.LanguageTool("en-US")


def uk_to_us(string):
    """
    Convert UK spelling to US spelling
    """
    print("Downloading British to American spelling mappings.")
    url ="https://raw.githubusercontent.com/hyperreality/American-British-English-Translator/master/data/british_spellings.json"
    british_to_american_mapping = requests.get(url).json()    

    for british_spelling, american_spelling in british_to_american_mapping.items():
        string = string.replace(british_spelling, american_spelling)
  
    return string


def standardize_naming(text, target_name, variants):
    pattern = re.compile(r"\b(" + "|".join(variants) + r")\b", re.IGNORECASE)
    return pattern.sub(target_name, text)


def standardize_spelling(text, mapping):
    pattern = re.compile(r"\b(" + "|".join(mapping.keys()) + r")\b", re.IGNORECASE)
    return pattern.sub(
        lambda match: mapping.get(match.group(0).lower(), match.group(0)), text
    )


def correct_text(text):
    # Step 1: Grammar, Spelling, and Punctuation Correction
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)

    # Step 2: Standardize Naming (e.g., "HubSpot")
    corrected_text = standardize_naming(
        corrected_text, "HubSpot", ["HubSpot", "hubspot"]
    )

    # Step 3: Standardize Spelling (UK to US)
    corrected_text = uk_to_us(corrected_text)

    return corrected_text


if __name__ == "__main__":
    text = "She don't like ice cream. Weve tested HubSpot and hubspot for our organisation. Her favourite colour is blue."
    corrected = correct_text(text)
    print(corrected)
