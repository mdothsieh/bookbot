def get_book_text(filepath: str) -> str:
    """Read the entire file and return it as one big string."""
    with open(filepath, 'r') as f:
        return f.read()

def get_num_words(text: str) -> int:
    """Return how many words are in text (split on whitespace)."""
    return len(text.split())

def get_char_count(text: str)->dict[str,int]:
    counts: dict[str,int] = {}
    for ch in text.lower():
        counts[ch]=counts.get(ch,0)+1
    return counts

def get_sorted_char_report(counts: dict[str, int]) -> list[dict[str, int]]:
    report = [
        {"char": ch, "num": n}
        for ch, n in counts.items()
        if ch.isalpha()          
    ]
    report.sort(key=lambda d: d["num"], reverse=True)
    return report


