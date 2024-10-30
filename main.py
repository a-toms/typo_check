import language_tool_python
import re

# Initialize LanguageTool for American English
tool = language_tool_python.LanguageTool("en-US")


def standardize_naming(text, target_name, variants, errors, location_info=None):
    """
    Standardize naming by replacing variants with the target name.
    Records each replacement as an error.
    """
    pattern = re.compile(r"\b(" + "|".join(map(re.escape, variants)) + r")\b", re.IGNORECASE)
    
    def replacer(match):
        original = match.group(0)
        corrected = target_name
        # Record the error
        errors.append({
            "value": original,
            "error_type": "inconsistent naming",
            "corrected_value": corrected,
            "location": location_info
        })
        return corrected
    
    return pattern.sub(replacer, text)

def standardize_spelling(text, mapping, errors, location_info=None):
    """
    Standardize spelling by replacing UK spellings with US spellings.
    Records each replacement as an error.
    """
    pattern = re.compile(r"\b(" + "|".join(map(re.escape, mapping.keys())) + r")\b", re.IGNORECASE)
    
    def replacer(match):
        original = match.group(0)
        # Preserve the case of the original word
        corrected = mapping.get(original.lower(), original)
        if original != corrected:
            errors.append({
                "value": original,
                "error_type": "inconsistent spelling",
                "corrected_value": corrected,
                "location": location_info
            })
        return corrected
    
    return pattern.sub(replacer, text)

def correct_text(text, location_info=None):
    """
    Corrects the text by addressing grammar, spelling, punctuation, 
    and standardizing naming and spelling.
    """
    errors = []
    matches = tool.check(text)
    
    # Sort matches by offset in reverse order to apply corrections from end to beginning
    matches.sort(key=lambda x: x.offset, reverse=True)
    
    corrected_text = text
    for match in matches:
        original = corrected_text[match.offset : match.offset + match.errorLength]
        corrected = match.replacements[0] if match.replacements else original
        
        errors.append({
            "value": original,
            "error_type": match.ruleId,
            "corrected_value": corrected,
            "location": location_info
        })
        
        # Apply correction
        corrected_text = corrected_text[:match.offset] + corrected + corrected_text[match.offset + match.errorLength:]
    
    return corrected_text, errors

if __name__ == "__main__":
    text = "She don't like ice cream. She goes to shcool every day. Weve tested HubSpot and hubspot for our organisation. Her favourite colour is blue. We realiesed the jewellery is stuning,."
    corrected, errors = correct_text(text)
    print("Corrected Text:\n", corrected)
    print("\nErrors Found:")
    for error in errors:
        print(error)