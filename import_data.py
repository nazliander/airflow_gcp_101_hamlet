import re
import pandas as pd


HAMLET = "dags/data/hamlet_text.txt"
STOPWORDS_FILEPATH = "dags/data/stopwords.txt"
OUTPUT_PATH = "dags/data/hamlet_wordcounts.csv"


def simple_tokenizer(text: str) -> list:
    word_regex = re.compile(r"(\w+)")
    return re.findall(word_regex, text.lower())


def word_count(text: str) -> int:
    return len(simple_tokenizer(text))


def read_book(book_path: str) -> str:
    with open(book_path, 'r') as reader:
        book = reader.read()
    return book


def read_stopwords(file_path: str) -> list:
    with open(file_path, 'r') as fw:
        stopwords = fw.readlines()
    return list(map(lambda x: x.strip(), stopwords))


def word_count_with_dict(text: str, sw_filepath: str) -> dict:
    words = simple_tokenizer(text)
    stopwords = read_stopwords(sw_filepath)
    word_count = {}
    for w in words:
        if w not in stopwords:
            word_count[w] = word_count.get(w, 0) + 1
    return word_count


if __name__ == "__main__":

    book_text = read_book(HAMLET)
    word_counts_hamlet = word_count_with_dict(
        text=book_text,
        sw_filepath=STOPWORDS_FILEPATH
    )
    csv_ready_format = pd.DataFrame(
        {
            "words": [k for k in word_counts_hamlet.keys()],
            "counts": [v for v in word_counts_hamlet.values()]
        })
    csv_ready_format.to_csv(OUTPUT_PATH, sep="|", index=False)
