from flask import Flask,request,render_template
from pymongo import MongoClient
from flask_cors import CORS 
app = Flask(__name__ ,template_folder='templates')


CORS(app)
client = MongoClient("mongodb+srv://sarra:12345@cluster0.o5iaci8.mongodb.net/")
db = client.get_database('Forms')

@app.route('/')
def route():
    return render_template("home.html")


@app.route('/Forms-post', methods=['POST'])
def Forms_post ():
    if request.method == 'POST':
        full_name=request.get_json()['full_name']
        email=request.get_json()['email']
        phone_number=request.get_json()['phone_number']
        city=request.get_json()['city']
        state=request.get_json()['state']
        student_or_employed=request.get_json()['student_or_employed']
        field_of_study_or_work=request.get_json()['field_of_study_or_work']
        courses_to_study=request.json['courses_to_study']
        availability=request.json['availability']
        hourly_budget=request.get_json()['hourly_budget']
      

       
        db['Forms'].insert_one({
            "full_name":full_name,
            "email":email,
            "phone_number":phone_number,
            "city":city,
            "state":state,
            "student_or_employed":student_or_employed,
            "field_of_study_or_work":field_of_study_or_work,
            "courses_to_study":courses_to_study,
            "availability":availability,
            "hourly_budget":hourly_budget
            })
        
        return ('added to data base')

@app.route('/Forms-get', methods=['GET'])
def Forms_get():
    
    if request.method == 'GET':
        allData = db['Forms'].find()
        dataJson = []
        for data in allData:
            print(data)
            id = data['_id']
            full_name = data['full_name']
            email = data['email']
            phone_number = data['phone_number']
            city = data['city']
            state = data['state']
            student_or_employed = data['student_or_employed']
            field_of_study_or_work = data['field_of_study_or_work']
            courses_to_study = data['courses_to_study']
            print(courses_to_study)
            availability = data['availability']
            hourly_budget = data['hourly_budget']
            
            dataDict = {
                '_id': str(id),
                'full_name': full_name,
                'email': email,
                'phone_number':phone_number,
                'city':city,
                'state':state,
                'student_or_employed':student_or_employed,
                'field_of_study_or_work':field_of_study_or_work,
                'courses_to_study':courses_to_study,
                'availability':availability,
                'hourly_budget':hourly_budget
            }
            dataJson.append(dataDict)
        return dataJson
    


    
@app.route('/Forms-post-teacher', methods=['POST'])
def Forms_post_teacher ():
    if request.method == 'POST':
        full_name=request.get_json()['full_name']
        email=request.get_json()['email']
        phone_number=request.get_json()['phone_number']
        city=request.get_json()['city']
        state=request.get_json()['state']
        student_or_employed=request.get_json()['student_or_employed']
        field_of_study_or_work=request.get_json()['field_of_study_or_work']
        courses_to_teach=request.json['courses_to_teach']
        print(courses_to_teach)
        availability=request.json['availability']
        print(availability)
        hourly_budget=request.get_json()['hourly_budget']
        

       
        db['teacher-Forms'].insert_one({
            "full_name":full_name,
            "email":email,
            "phone_number":phone_number,
            "city":city,
            "state":state,
            "student_or_employed":student_or_employed,
            "field_of_study_or_work":field_of_study_or_work,
            "courses_to_teach":courses_to_teach,
            "availability":availability,
            "hourly_budget":hourly_budget
            })
        
        return ('added to data base')

@app.route('/Forms-get-teacher', methods=['GET'])
def Forms_get_teacher():
    
    if request.method == 'GET':
        allData = db['teacher-Forms'].find()
        dataJson = []
        for data in allData:
            print(data)
            id = data['_id']
            full_name = data['full_name']
            email = data['email']
            phone_number = data['phone_number']
            city = data['city']
            state = data['state']
            student_or_employed = data['student_or_employed']
            field_of_study_or_work = data['field_of_study_or_work']
            courses_to_teach = data['courses_to_teach']
            print(courses_to_teach)
            availability = data['availability']
            hourly_budget = data['hourly_budget']
            
            dataDict = {
                '_id': str(id),
                'full_name': full_name,
                'email': email,
                'phone_number':phone_number,
                'city':city,
                'state':state,
                'student_or_employed':student_or_employed,
                'field_of_study_or_work':field_of_study_or_work,
                'courses_to_teach':courses_to_teach,
                'availability':availability,
                'hourly_budget':hourly_budget
            }
            dataJson.append(dataDict)
            print(dataDict)
        return dataJson
    

    ##############################################################


@app.route('/Forms-post-contact', methods=['POST'])
def Forms_post_contact ():
    if request.method == 'POST':
        full_name=request.get_json()['full_name']
        email=request.get_json()['email']
        message=request.get_json()['message']
        
        
       
        db['contact-Forms'].insert_one({
            "full_name":full_name,
            "email":email,
            "message":message
            
            })
        
        return ('added to data base')
    
@app.route('/Forms-get-contact', methods=['GET'])
def Forms_get_contact ():
    
    if request.method == 'GET':
        allData = db['contact-Forms'].find()
        dataJson = []
        for data in allData:
            print(data)
            id = data['_id']
            full_name = data['full_name']
            email = data['email']
            message = data['message']
            
            
            dataDict = {
                '_id': str(id),
                'full_name': full_name,
                'email': email,
                'message':message
                
            }
            dataJson.append(dataDict)
        return dataJson

####################################################""

if __name__ == "__main__":
    app.run(debug=True)