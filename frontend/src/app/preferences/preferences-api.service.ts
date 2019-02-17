import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { catchError } from 'rxjs/operators';
import { API_URL } from '../env';
import { Trip } from '../trips/trip.model';
import { Student } from '../trips/students/student.model';

@Injectable({
  providedIn: 'root'
})
export class PreferencesApiService {

  constructor(private http: HttpClient) { }

  getStudentPreferences(student_id: number):
  Observable<Array<Student>> {
    return this.http
    .get<Array<Student>>(`${API_URL}/student/${student_id}/preferences`);
  }
}
