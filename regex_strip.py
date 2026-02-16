import re


def regex_strip(text, pattern= " "):
    """
    Strips leading and trailing occurrences of a regex pattern.
    Default pattern strips whitespace.
    """
    pattern = re.escape(pattern)
    # Replace the pattern at the start of the string
    text = re.sub(f"^{pattern}*", "", text)
    # Replace the pattern at the end of the string
    text = re.sub(f"{pattern}*$", "", text)
    return text

# Example Usage
text_with_whitespace = "   hello world   "
result_whitespace = regex_strip(text_with_whitespace)
# Result: "hello world"
print(result_whitespace)

print()

text_with_markers = "*data*"
# Stripping asterisks specifically
result_markers = regex_strip(text_with_markers, pattern="*")
# Result: "data"
print(result_markers)

input()