from Run import process, db
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/process_message', methods=['POST'])
def process_message():
    message = request.json["message"]
    bot_response = process(message)
    res = str(bot_response[0])
    tag = str(bot_response[1])

    # Check if the bot response requires user input
    if "Please, enter your Id" in res:
        # Return a response that asks the user for input
        response = {"response": res, "tag": tag, "requires_input": "True"}
    else:
        # Return the bot response
        response = {"response": res}

    return jsonify(response)


@app.route('/get_all_final_grade', methods=['POST'])
def get_all_final_grade():
    message = request.json["message"]

    if check_student_doc_id(message):
        l = []
        coll_ref = db.collection('Faculty').document('B').collection('Student').document(message).collection('Attending')
        query = coll_ref.where('semester', '==', 'Fall 2022')
        docs = query.stream()
        for doc in docs:
            name_value = coll_ref.document(doc.id).get().to_dict()['name']
            final_grade_value = coll_ref.document(doc.id).get().to_dict()['finalGrade']
            l.append([name_value, final_grade_value])
        bot_response = str(l)

        response = {"response": bot_response}
        return jsonify(response)
    else:
        response = {"response": "The ID is not correct, please enter your ID again", 'tag': "get_all_final_grade",
                    "requires_input": "True"}
        return jsonify(response)


@app.route('/get_all_mid_grade', methods=['POST'])
def get_all_mid_grade():
    message = request.json["message"]

    if check_student_doc_id(message):
        l = []
        coll_ref = db.collection('Faculty').document('B').collection('Student').document(message).collection('Attending')
        query = coll_ref.where('semester', '==', 'Fall 2022')
        docs = query.stream()
        for doc in docs:
            name_value = coll_ref.document(doc.id).get().to_dict()['name']
            mid_grade_value = coll_ref.document(doc.id).get().to_dict()['midGarde']
            l.append([name_value, mid_grade_value])
        bot_response = str(l)

        response = {"response": bot_response}
        return jsonify(response)
    else:
        response = {"response": "The ID is not correct, please enter your ID again", 'tag': "get_all_mid_grade",
                    "requires_input": "True"}
        return jsonify(response)


@app.route('/get_all_class_work', methods=['POST'])
def get_all_class_work():
    message = request.json["message"]

    if check_student_doc_id(message):
        l = []
        coll_ref = db.collection('Faculty').document('B').collection('Student').document(message).collection(
            'Attending')
        query = coll_ref.where('semester', '==', 'Fall 2022')
        docs = query.stream()
        for doc in docs:
            name_value = coll_ref.document(doc.id).get().to_dict()['name']
            class_work_value = coll_ref.document(doc.id).get().to_dict()['classWork']
            l.append([name_value, class_work_value])
        bot_response = str(l)

        response = {"response": bot_response}
        return jsonify(response)
    else:
        response = {"response": "The ID is not correct, please enter your ID again", 'tag': "get_all_class_work",
                    "requires_input": "True"}
        return jsonify(response)


@app.route('/get_all_courses_attendance', methods=['POST'])
def get_all_courses_attendance():
    message = request.json["message"]

    if check_student_doc_id(message):
        l = []
        coll_ref = db.collection('Faculty').document('B').collection('Student').document(message).collection(
            'Attending')
        query = coll_ref.where('semester', '==', 'Fall 2022')
        docs = query.stream()
        for doc in docs:
            name_value = coll_ref.document(doc.id).get().to_dict()['name']
            attendance_value = coll_ref.document(doc.id).get().to_dict()['attendance']
            l.append([name_value, attendance_value])
        bot_response = str(l)

        response = {"response": bot_response}
        return jsonify(response)
    else:
        response = {"response": "The ID is not correct, please enter your ID again", 'tag': "get_all_courses_attendance",
                    "requires_input": "True"}
        return jsonify(response)


@app.route('/get_schedule', methods=['POST'])
def get_schedule():
    message = request.json["message"]

    if check_student_doc_id(message):
        l = []
        coll_ref = db.collection('Faculty').document('B').collection('Student').document(message).collection(
            'Attending')
        query = coll_ref.where('semester', '==', 'Fall 2022')
        docs = query.stream()
        for doc in docs:
            name_value = coll_ref.document(doc.id).get().to_dict()['name']
            day_value = coll_ref.document(doc.id).get().to_dict()['day']
            time_value = coll_ref.document(doc.id).get().to_dict()['time']
            room_value = coll_ref.document(doc.id).get().to_dict()['room']
            l.append([name_value, day_value, time_value, room_value])
        bot_response = str(l)

        response = {"response": bot_response}
        return jsonify(response)
    else:
        response = {"response": "The ID is not correct, please enter your ID again",
                    'tag': "get_schedule",
                    "requires_input": "True"}
        return jsonify(response)


@app.route('/get_cgpa', methods=['POST'])
def get_cgpa():
    message = request.json["message"]

    if check_student_doc_id(message):
        cgpa_value = db.collection('Faculty').document('B').collection('Student').document(message).get().to_dict()[
            'CGPA']
        bot_response = str(cgpa_value)

        response = {"response": bot_response}
        return jsonify(response)
    else:
        response = {"response": "The ID is not correct, please enter your ID again",
                    'tag': "get_cgpa",
                    "requires_input": "True"}
        return jsonify(response)


@app.route('/get_gpa', methods=['POST'])
def get_gpa():
    message = request.json["message"]

    if check_student_doc_id(message):
        gpa_value = db.collection('Faculty').document('B').collection('Student').document(message).get().to_dict()['GPA']
        bot_response = str(gpa_value)

        response = {"response": bot_response}
        return jsonify(response)
    else:
        response = {"response": "The ID is not correct, please enter your ID again",
                    'tag': "get_gpa",
                    "requires_input": "True"}
        return jsonify(response)


@app.route('/get_webmail', methods=['POST'])
def get_webmail():
    message = request.json["message"]

    if check_student_doc_id(message):
        webmail_value = db.collection('Faculty').document('B').collection('Student').document(message).get().to_dict()[
            'webmail']
        bot_response = str(webmail_value)

        response = {"response": bot_response}
        return jsonify(response)
    else:
        response = {"response": "The ID is not correct, please enter your ID again",
                    'tag': "get_webmail",
                    "requires_input": "True"}
        return jsonify(response)


@app.route('/get_final_grade', methods=['POST'])
def get_final_grade(course_name):
    message = request.json["message"]

    if check_student_doc_id(message):
        if check_attending_course_doc_id(message, course_name):
            c_doc_id = get_course_code(course_name)
            ref = get_attending_course_ref(message, c_doc_id)
            final_grade_value = ref.get().to_dict()['finalGrade']
            bot_response = str(final_grade_value)

            response = {"response": bot_response}
            return jsonify(response)
        else:
            response = {"response": "The course you entered is not registered before",
                        'tag': "get_one_final_grade"}
            return jsonify(response)
    else:
        response = {"response": "The ID is not correct, please enter your ID again",
                    'tag': "get_one_final_grade",
                    "requires_input": "True"}
        return jsonify(response)


@app.route('/get_mid_grade', methods=['POST'])
def get_mid_grade(student_id, course_name):
    s_doc_id = check_student_doc_id(student_id)
    c_doc_id = get_attending_course_doc_id(student_id, course_name)
    ref = get_attending_course_ref(s_doc_id, c_doc_id)
    mid_grade_value = ref.get().to_dict()['midGarde']
    return mid_grade_value


@app.route('/get_class_work', methods=['POST'])
def get_class_work(student_id, course_name):
    s_doc_id = check_student_doc_id(student_id)
    c_doc_id = get_attending_course_doc_id(student_id, course_name)
    ref = get_attending_course_ref(s_doc_id, c_doc_id)
    class_work_value = ref.get().to_dict()['classWork']
    return class_work_value


@app.route('/get_course_attendance', methods=['POST'])
def get_course_attendance(student_id, course_name):
    s_doc_id = check_student_doc_id(student_id)
    c_doc_id = get_attending_course_doc_id(student_id, course_name)
    coll_ref = get_attending_course_ref(s_doc_id, c_doc_id)
    name_value = coll_ref.get().to_dict()['name']
    attendance_value = coll_ref.get().to_dict()['attendance']
    return name_value, attendance_value


def get_course_code(course_name):
    code = ''
    coll_ref = db.collection('Faculty').document('B').collection('Course')
    docs = coll_ref.stream()
    for doc in docs:
        doc_ref = coll_ref.document(doc.id)
        name_value = doc_ref.get().to_dict()['name']
        if name_value == course_name:
            code = doc_ref.get().to_dict()['code']
            break
    return code


def check_student_doc_id(student_id):
    doc_ref = db.collection('Faculty').document('B').collection('Student').document(student_id)
    doc = doc_ref.get()
    if doc.exists:
        return True
    else:
        return False


def check_attending_course_doc_id(student_id, course_name):
    course_id = get_course_code(course_name)
    doc_ref = db.collection('Faculty').document('B').collection('Student').document(student_id).collection('Attending')
    doc = doc_ref.document(course_id).get()
    if doc.exists:
        return True
    else:
        return False


def get_attending_course_doc_id(student_id, course_name):
    course_doc_id = ''
    course_id = get_course_code(course_name)
    coll_ref = db.collection('Faculty').document('B').collection('Student').document(student_id).collection('Attending')
    course_docs = coll_ref.stream()
    for doc in course_docs:
        if doc.id == course_id:
            course_doc_id = doc.id
            break
    return course_doc_id


def get_attending_course_ref(s_doc_id, c_doc_id):
    course_doc_ref = db.collection('Faculty').document('B').collection('Student').document(s_doc_id).collection(
        'Attending').document(c_doc_id)
    return course_doc_ref
 

if __name__ == "__main__":
    app.run(debug=True)
