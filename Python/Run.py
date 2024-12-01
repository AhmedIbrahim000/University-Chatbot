import tflearn
import numpy
import pickle
import json
import random
import nltk
from nltk.stem.lancaster import LancasterStemmer
from autocorrect import Speller
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import re


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


stemmer = LancasterStemmer()
spell = Speller(lang='en')

with open('intents.json') as file:
    data = json.load(file)

with open("data.pickle", "rb") as f:
    words, labels, training, output = pickle.load(f)


net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)
model = tflearn.DNN(net)
model.load("model.tflearn")


def extract_course_names(text):
    # List of course names
    course_names = ['Mathematics-1', 'Electronics', 'Physics', 'Communication and Presentation Skills', 'Sociology',
                    'Introduction to Computer', 'Psychology', 'Scientific Thinking', 'Mathematics-2', 'Mathematics-3',
                    'Probability and Statistics', 'Report Writing', 'Human Rights', 'Discrete Mathematics', 'Logic Design',
                    'Computer Programming-1', 'Database System-1', 'Computer Programming-2', 'Data Structures',
                    'Computer Networks-1', 'Computer Organization and Assembly Language', 'Advanced Programming',
                    'Operating systems-1', 'Software Engineering-1', 'Modeling and Simulation', 'Introduction to Information Systems',
                    'Database System-2', 'Systems Analysis and Design', 'Management Information Systems', 'Internet Technology',
                    'Operations Research', 'Summer Training', 'Information Storage and Retrieval', 'Artificial Intelligence',
                    'Software Engineering-2', 'Geographical Information Systems', 'Expert Systems', 'Computers and Information Security',
                    'Decisions Support Systems', 'Data Warehousing', 'Data Mining', 'Software Project Management', 'Mobile Applications',
                    'Business Intelligence', 'Selected Topics in Information Systems-1', 'Enterprise Resource Planning',
                    'Design of Web-Based Applications', 'Project-1', 'Project-2', 'English Ket', 'English Pet B1-B2', 'English Ket Advanced',
                    'English Pet Advanced', 'Environmental Sciences', 'Data Communication', 'E-Learning', 'E-business and Digital Firms',
                    'Health Care Information Systems', 'Computer and Society', 'Selected Topics in Information Systems-2']
    """
    coll_ref = db.collection('Faculty').document('B').collection('Course')
    docs = coll_ref.stream()
    for doc in docs:
            name_value = coll_ref.document(doc.id).get().to_dict()['name']
            course_names.append(name_value)
    """
    
    # Define the regular expression pattern
    pattern = '|'.join(course_names)
    pattern = re.compile(pattern, re.IGNORECASE)  # Make pattern case-insensitive

    # Find all occurrences of the pattern in the text
    matches = re.findall(pattern, text)
    return matches


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)


def process(message):
    input = message
    corrected_input = spell(input)
    course_names = extract_course_names(corrected_input)
    results = model.predict([bag_of_words(corrected_input, words)])[0]
    results_index = numpy.argmax(results)
    tag = labels[results_index]

    if results[results_index] > 0.8:
        for tg in data["intents"]:
            if tg['tag'] == tag:
                # get from firestore
                if course_names:
                    responses = tg['responses']
                    bot = random.choice(responses)
                    return [bot, tag]
                else:
                    responses = tg['responses']
                    bot = random.choice(responses)
                    return [bot, tag]

    # elif 0.7 > results[results_index] > 0.6:
    else:
        return ["I didn't understand that, try again please.", ""]


"""
                    if tag == 'get_one_final_grade':
                        response_list = []
                        for course_name in course_names:
                            response_list.append(get_final_grade(user_id, course_name))
                        return response_list

                    elif tag == 'get_one_mid_grade':
                        # s_id = input('Please, enter your Id: ')
                        response_list = []
                        for course_name in course_names:
                            response_list.append(get_final_grade(user_id, course_name))
                        return response_list

                    elif tag == 'get_one_class_work':
                        # s_id = input('Please, enter your Id: ')
                        response_list = []
                        for course_name in course_names:
                            response_list.append(get_final_grade(user_id, course_name))
                        return response_list

                    elif tag == 'get_one_course_attendance':
                        # s_id = input('Please, enter your Id: ')
                        response_list = []
                        for course_name in course_names:
                            response_list.append(get_final_grade(user_id, course_name))
                        return response_list
"""

"""
                    elif tag == 'oral_location':
                    get from firestore
                    if tag == 'cs_location':
                    elif tag == 'en_location':
                    elif tag == 'ph_location':
                    elif tag == 'buss_location':
                    elif tag == 'pol_location':
                    else:
                    """

"""
elif tag == 'buss_location':
                        coll_ref = db.collection('Faculty').document("B")
                        location_value = coll_ref.get().to_dict()['location']
                        latitude = location_value.latitude
                        longitude = location_value.longitude
                        return latitude, longitude
"""