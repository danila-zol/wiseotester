class Preproc:
    def __init__(self, dataset=None):
        # Importing libraries
        import spacy
        # from nltk.corpus import stopword
        
        # Various utilities initialization
        self.nlp = spacy.load('en_core_web_sm')

        # Dataset initialization
        if dataset:
            self.dataset_full = dataset
        else:
            from datasets import load_dataset
            self.dataset_full = load_dataset("squad", split="train").to_pandas()
        
        # Dataset preprocessing
        self.preproc()

        # Tokenization
        self.dataset_full["context"] = self.dataset_full["context"].apply(self.nlp)
        self.dataset_full["question_tokenized"] = self.dataset_full["question"].apply(self.nlp)
        self.dataset_full["answers_tokenized"] = self.dataset_full["answers_text"].apply(self.nlp)
        
        # Vectorisation
        self.dataset_full["question_vectors"] = self.dataset_full["question_tokenized"].apply(lambda x: list(map(lambda y: y.vector, x)))
        self.dataset_full["question_vectors"] = self.dataset_full["answers_tokenized"].apply(lambda x: list(map(lambda y: y.vector, x)))

    def preproc(self):
        # Splitting "answers" in two columns
        self.dataset_full["answers_text"] = self.dataset_full["answers"].apply(lambda x: x["text"][0])
        self.dataset_full["answers_start_index"] = self.dataset_full["answers"].apply(lambda x: x["answer_start"][0])

        # Dropping the unnecessary columns
        self.dataset_full = self.dataset_full.drop(["answers", "id", "title"], axis=1)
    
if __name__ == "__main__":
    test = Preproc()