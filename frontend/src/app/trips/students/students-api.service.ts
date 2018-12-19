import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import { catchError } from 'rxjs/operators';
import {API_URL} from '../../env';
import {Trip} from '../trip.model';
import {Student} from './student.model';

@Injectable()
export class StudentsApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  getStudentsInGrade(grade: string):
  Observable<Array<Student>> {
    return this.http
    .get<Array<Student>>(`${API_URL}/students/gradeLevel/${grade}`);
  }

}
