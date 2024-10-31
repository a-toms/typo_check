import language_tool_python
import re

tool = language_tool_python.LanguageTool("en-US")


def correct_text(text, location_info=None):
    """
    Corrects the text by addressing grammar, spelling, punctuation, 
    and standardizing naming and spelling.
    """
    errors = []
    matches = tool.check(text)
    
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
    text = "She don't like ice cream. She go to shcool every day. Weve tested HubSpot and hubspot for our organisation. Her favourite colour is blue. We realiesed the jewellery is stuning,."
    corrected, errors = correct_text(text)
    print("Corrected Text:\n", corrected)
    print("\nErrors Found:")
    for error in errors:
        print(error)