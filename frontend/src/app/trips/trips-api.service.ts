import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import { catchError } from 'rxjs/operators';
import {API_URL} from '../env';
import {Trip} from './trip.model';

@Injectable()
export class TripsApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getTrips():
  Observable<Array<Trip>> {
    return this.http
    .get<Array<Trip>>(`${API_URL}/trips`);
  }

  saveTrip(trip: Trip): Observable<any> {
  return this.http
    .post(`${API_URL}/trips/new`, trip);
  }

  deleteTrip(trip_id: number) {
    return this.http
      .delete(`${API_URL}/trips/${trip_id}/delete`);
  }
}
