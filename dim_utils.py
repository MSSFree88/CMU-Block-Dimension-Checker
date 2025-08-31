import re

def parse_input(s):
    """Parses a string like 6'4", 5'9, 6-4, or 72 into total inches (int)."""
    s = s.strip().lower().replace("’", "'").replace("“", "\"").replace("”", "\"")
    
    # Just digits? Assume inches
    if s.isdigit():
        return int(s)
    
    # Try to match combined feet-inches format (hyphen or apostrophe, optional symbols)
    pattern = r"""
        ^\s*
        (?:(\d+)\s*(?:'|ft)?\s*[-]?\s*)?    # Feet (optional), with optional apostrophe or hyphen
        (?:(\d+)\s*(?:\"|in)?)?             # Inches (optional), with or without quote
        \s*$
    """

    match = re.match(pattern, s, re.VERBOSE)
    if match:
        feet = int(match.group(1)) if match.group(1) else 0
        inches = int(match.group(2)) if match.group(2) else 0
        return feet * 12 + inches

    raise ValueError("Invalid format. Use formats like 6'4\", 5-9, or 76")

def check_block_dimension(dim):

    BLOCK_SIZE = 8

    if not isinstance(dim, int) or dim <= 0:
        raise ValueError("Input must be a positive integer.")

    is_block = dim % BLOCK_SIZE == 0
    next_block = ((dim // BLOCK_SIZE) + 1) * BLOCK_SIZE

    prev_block = (dim // BLOCK_SIZE) * BLOCK_SIZE
    if prev_block == dim:
        prev_block -= BLOCK_SIZE
    if prev_block <= 0:
        prev_block = None

    return is_block, next_block, prev_block

def format_inches_to_ft_in(total_inches):
    """Converts a total inches value to a string in #'-#" format."""
    if not isinstance(total_inches, int) or total_inches < 0:
        raise ValueError("Input must be a non-negative integer.")

    feet = total_inches // 12
    inches = total_inches % 12
    return f"{feet}' {inches}\""