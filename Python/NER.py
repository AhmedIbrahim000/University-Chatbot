import spacy
import random

# Set up the training data
training_data = [
    ("I am studying Computer Science at Harvard University.", {"entities": [(16, 32, "COURSE"), (36, 51, "ORG")]}),
    ("I am taking a Biology course this semester at MIT.", {"entities": [(16, 23, "COURSE"), (38, 41, "ORG")]}),
    ("I am learning Spanish at the language school downtown.", {"entities": [(16, 23, "COURSE"), (31, 45, "LOC")]}),
    # ... more examples ...
]

# Create a blank "en" model
nlp = spacy.blank("en")

# Add a new NER pipeline component to the blank model
ner = nlp.add_pipe("ner")

# Add the "COURSE" label to the NER pipeline
ner.add_label("COURSE")

# Start the training loop
n_iter = 100
for i in range(n_iter):
    # Shuffle the training data to avoid bias
    random.shuffle(training_data)
    losses = {}
    # Batch the training data into batches of 8 examples
    batches = spacy.util.minibatch(training_data, size=8)
    # Iterate over the batches
    for batch in batches:
        # Split the batch into texts and annotations
        texts, annotations = zip(*batch)
        # Update the NER model with the texts and annotations
        nlp.update(texts, annotations, drop=0.2, losses=losses)
    # Print the loss at the end of each iteration
    print("Iteration {} Loss: {:.3f}".format(i+1, losses["ner"]))

# Example test sentences
texts = [
    "I am studying Computer Science at Harvard University.",
    "I am taking a Biology course this semester at MIT.",
    "I am learning Spanish at the language school downtown.",
    "I just finished a course in Machine Learning.",
    "I want to enroll in a Physics class next semester."
]

# Process each test sentence with the NER model and print the detected entities
for text in texts:
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print(text)
    print("Entities:", entities)
