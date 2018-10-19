from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import flask
from flask import Flask, request
# from server.dao import engine
from database_setup import Base, Student, engine
import cgi
import cgitb
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

cgitb.enable()
Session = sessionmaker(bind=engine)
app = Flask(__name__)


engine = create_engine('sqlite:///database.db')
Base.metadata.bind = create_engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/students/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Add a New Student</h1>"
                output += "<form method = 'POST' enctype='multipart/form-data' action = '/students/new'>"
                output += "<input name = 'newStudentFirstName' type = 'text' placeholder = 'New Student First Name' > "
                output += "<input name = 'newStudentLastName' type = 'text' placeholder = 'New Student Last Name' > "
                output += "<input type='submit' value='Create'>"
                output += "</form></body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                studentID = self.path.split("/")[2]
                student = session.query(Student).filter_by(id=studentID).one()
                if student:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = "<html><body>"
                    output += "<h1>"
                    output += student.first_name
                    output += student.last_name
                    output += "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action = '/students/%s/edit' >" % studentID
                    output += "<input name = 'newStudentFirstName' type='text' placeholder = '%s' >" % student.first_name
                    output += "<input name = 'newStudentLastName' type='text' placeholder = '%s' >" % student.last_name
                    output += "<input type = 'submit' value = 'Rename'>"
                    output += "<input type = 'cancel' value = 'Cancel'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)

            if self.path.endswith("/delete"):
                studentID = self.path.split("/")[2]
                student = session.query(Student).filter_by(id=studentID).one()
                if student:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>Are you sure you want to delete %s " % student.first_name+student.last_name+"?"
                    output += "<form method='POST' enctype = 'multipart/form-data' action = '/students/%s/delete'>" % studentID
                    output += "<input type = 'submit' value = 'Delete'>"
                    output += "<input type = 'cancel' value = 'Cancel'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)

            if self.path.endswith("/students"):
                students = session.query(Student).all()
                output = ""
                output += "<a href = '/students/new' > Add a New Student </a></br></br>"
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output += "<html><body>"
                for student in students:
                    output += student.first_name
                    output += " "
                    output += student.last_name
                    output += "</br></br></br>"
                    output += "<a href ='/students/%s/edit' >Edit </a> " % student.id
                    output += "</br>"
                    output += "<a href ='/students/%s/delete'> Delete </a>" % student.id
                    output += "</br></br></br>"

                output += "</body></html>"
                self.wfile.write(output)
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            if self.path.endswith("/delete"):
                studentID = self.path.split("/")[2]
                student = session.query(Student).filter_by(id=studentID).one()
                if student:
                    session.delete(student)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/students')
                    self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newStudentFirstName')
                    messagecontent += fields.get('newStudentLastName')
                    studentID = self.path.split("/")[2]
                    student = session.query(Student).filter_by(id=studentID).one()
                    if student != []:
                        student.first_name = messagecontent[0]
                        student.last_name = messagecontent[1]
                        session.add(student)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/students')
                        self.send_header('Location', '/students')
                        self.end_headers()

            if self.path.endswith("/students/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get('newStudentFirstName')
                    messagecontent += fields.get('newStudentLastName')
                    newStudent = Student(first_name = messagecontent[0], last_name = messagecontent[1])
                    session.add(newStudent)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/students')
                    self.send_header('Location', '/students')
                    self.end_headers()

        except:
            pass

def main():
    try:
        port = 8000
        server = HTTPServer(('', port), WebServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print "^C entered, stopping web server...."
        server.socket.close()


if __name__ == '__main__':
        main()
