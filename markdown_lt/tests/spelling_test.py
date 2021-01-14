"""Tests for markdown_lt."""

from markdown_lt import check, matches_to_string

WORDS = ["insist", "pollution", "noncommittal", "implicit", "roll", "camp", "scream", "smile", "sketch", "band"]


def test_correct_spelling():
    md_text = " ".join(WORDS)
    matches = check(md_text, enabled_only=True, enabled_rules={'MORFOLOGIK_RULE_EN_US'})
    assert matches == [], matches_to_string(matches)


def test_incorrect_spelling():
    incorrect_words = [word + "aaa" for word in WORDS]
    md_text = " ".join(incorrect_words)
    matches = check(md_text, enabled_only=True, enabled_rules={'MORFOLOGIK_RULE_EN_US'})
    assert len(matches) == len(incorrect_words), matches_to_string(matches)


def test_wordlist():
    incorrect_words = [word + "aaa" for word in WORDS]
    wordlist = set(incorrect_words[:int((len(incorrect_words) / 2))])
    md_text = " ".join(incorrect_words)
    matches = check(md_text, enabled_only=True, enabled_rules={'MORFOLOGIK_RULE_EN_US'}, wordlist=wordlist)
    print(matches_to_string(matches))
    assert len(matches) == len(incorrect_words) / 2, matches_to_string(matches)
