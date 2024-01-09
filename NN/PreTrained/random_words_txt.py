import random
import spacy
nlp = spacy.load("en_core_web_sm")
def extract_random_meaningful_words(text, count=1):
    doc = nlp(text)
    # Выбор случайных осмысленных слов
    meaningful_words = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    if len(meaningful_words) >= count:
        # Выбираем случайные слова из отфильтрованного массива
        selected_words = random.sample(meaningful_words, count)
        return selected_words
    else:
        return None

sample_text = "Shostakovich v. Twentieth Century-Fox Film Corp. is a landmark 1948 New York Supreme Court decision. It was the first case in the United States dealing with moral rights in authorship. The Soviet composers Dmitri Shostakovich (pictured), Aram Khachaturian, Sergei Prokofiev, and Nikolai Myaskovsky sued Twentieth Century-Fox Film Corporation for using their compositions in the film The Iron Curtain. Although their compositions were in the public domain in the United States, the composers argued that the film violated their moral rights by using their works in a manner contrary to their beliefs. The court rejected the composers' argument, holding that there was no clear standard for adjudicating moral rights and that moral rights conflict with free use of public domain works. The decision has been criticized for misunderstanding moral rights and praised for upholding the right of the public to use public domain works over the rights of authors to censor uses that they disagree with."
random_words = extract_random_meaningful_words(sample_text, count=3)

if random_words:
    print(f"Случайные осмысленные слова: {random_words}")
else:
    print("В тексте нет подходящих осмысленных слов.")


