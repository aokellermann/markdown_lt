"""Tests for markdown_lt."""

from markdown_lt import check, matches_to_string

WORDS = ["insist", "pollution", "noncommittal", "implicit", "roll", "camp", "scream", "smile", "sketch", "band"]


def test_correct_spelling():
    """Ensures that spellcheck doesn't flag valid words."""
    md_text = " ".join(WORDS)
    matches = check(md_text, enabled_only=True, enabled_rules={'MORFOLOGIK_RULE_EN_US'})
    assert matches == [], matches_to_string(matches)


def test_incorrect_spelling():
    """Ensures that spellcheck flags invalid words."""
    incorrect_words = [word + "aaa" for word in WORDS]
    md_text = " ".join(incorrect_words)
    matches = check(md_text, enabled_only=True, enabled_rules={'MORFOLOGIK_RULE_EN_US'})
    assert len(matches) == len(incorrect_words), matches_to_string(matches)


def test_wordlist():
    """Ensures that spellcheck doesn't flag words added to the wordlist."""
    incorrect_words = [word + "aaa" for word in WORDS]
    wordlist = set(incorrect_words[:int((len(incorrect_words) / 2))])
    md_text = " ".join(incorrect_words)
    matches = check(md_text, enabled_only=True, enabled_rules={'MORFOLOGIK_RULE_EN_US'}, wordlist=wordlist)
    print(matches_to_string(matches))
    assert len(matches) == len(incorrect_words) / 2, matches_to_string(matches)
