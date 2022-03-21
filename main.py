from typing import List


def find_longest_mutual_word(first_sentence: List[str], second_sentence: List[str]):
    longest_mutual_word = ""
    for first_word in first_sentence:
        for second_word in second_sentence:
            if first_word == second_word and len(first_word) > len(longest_mutual_word):
                longest_mutual_word = first_word

    if longest_mutual_word:
        print(f"Longest mutual word: {longest_mutual_word}")
    else:
        print(f"Longest mutual word wasn't found")


def optimized_find_longest_mutual_word(first_sentence: List[str], second_sentence: List[str]):
    mutual_words = set(first_sentence).intersection(set(second_sentence))

    sorted_mutual_words = sorted(mutual_words, key=lambda x: len(x), reverse=True)

    if sorted_mutual_words:
        longest_mutual_word = sorted_mutual_words[0]
        print(f"Longest mutual word: {longest_mutual_word}")
    else:
        print(f"Longest mutual word wasn't found")


if __name__ == "__main__":
    # first_sentence = "предложение один два три".strip().split()
    # second_sentence = "мама солнце два".strip().split()

    print(f"Program will find longest mutual word from 2 sentence")
    first_sentence = input("Input first sentence:\n").strip().split()
    second_sentence = input("Input second sentence:\n").strip().split()

    find_longest_mutual_word(first_sentence, second_sentence)
    # optimized_find_longest_mutual_word(first_sentence, second_sentence)
