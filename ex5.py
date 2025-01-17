import json
import os



def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    student_list=[]
    with open(input_json_path, 'r') as f:
        loaded_dict = json.load(f)
        key_list = loaded_dict.keys()
        for student in key_list:
            if(course_name in loaded_dict[student]["registered_courses"]):
                student_list.append(loaded_dict[student]["student_name"])

    return student_list

def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    course_list = []
    with open(input_json_path, 'r') as f:
        loaded_dict = json.load(f)
        key_list = loaded_dict.keys()
        for student in key_list:
            course_list = list(set(loaded_dict[student]["registered_courses"])| set(course_list))

        course_dict = dict(zip(course_list,[0 for x in range(0,len(course_list))]))
        #Creating the dict containing the number of students in every course
        for student in key_list:
            for course in loaded_dict[student]["registered_courses"]:
                course_dict[course]+=1

    #Creating alphbetic list of courses
    course_list.sort()

    #Writing to the output file
    with open(output_file_path, 'w') as f:
        for course in course_list:
            f.write('"' + course+ '" '+str(course_dict[course])+"\n")
#d
def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    #creating lecturers list
    lecturers_list=[]
    for file_name in os.listdir(json_directory_path):
        file_to_read = os.path.join(json_directory_path, file_name)
        if (len(file_name)<6):
            continue
        if (file_name[-5:]!=".json"):
            continue
        with open(file_to_read,"r") as f:
            loaded_dict = json.load(f)
            key_list = loaded_dict.keys()
            for course_id in key_list:
                lecturers_list = list(set(loaded_dict[course_id]["lecturers"]) | set(lecturers_list))
    lecturers_dict=dict(zip(lecturers_list,[[] for x in range(0,len(lecturers_list))]))
    #adding courses to each lecturer
    for file_name in os.listdir(json_directory_path):
        file_to_read = os.path.join(json_directory_path, file_name)
        if (len(file_name)<6):
            continue
        if (file_name[-5:]!=".json"):
            continue
        with open(file_to_read,"r") as f:
            loaded_dict = json.load(f)
            key_list = loaded_dict.keys()
            for course_id in key_list:
                for lecturer in lecturers_list:
                    if (lecturer in loaded_dict[course_id]["lecturers"] and (not loaded_dict[course_id]["course_name"] in lecturers_dict[lecturer])):
                        lecturers_dict[lecturer].append(loaded_dict[course_id]["course_name"])
    #writing to the output file
    with open(output_json_path, 'w') as f:
        json.dump(lecturers_dict, f, indent=4)

#

