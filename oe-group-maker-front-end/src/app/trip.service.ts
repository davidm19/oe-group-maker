import { Injectable } from '@angular/core';
import { FormGroup,  FormBuilder,  Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

@Injectable()
export class TripService {

  result: any;
  constructor(private http: HttpClient) {}

  addTrip(name, price) {
    const uri = 'http://localhost:4200/coins/add';
    const obj = {
      name: name,
      price: price
    };
    this
      .http
      .post(uri, obj)
      .subscribe(res =>
          console.log('Done'));
  }

  getTrips() {
    const uri = 'http://localhost:4200/trips';
    return this
            .http
            .get(uri)
            .map(res => {
              return res;
            });
  }

  editTrip(id) {
    const uri = 'http://localhost:4200/trips/edit/' + id;
    return this
            .http
            .get(uri)
            .map(res => {
              return res;
            });
  }

  updateCoin(name, id) {
    const uri = 'http://localhost:4200/trips/update/' + id;

    const obj = {
      name: name,
    };
    this
      .http
      .post(uri, obj)
      .subscribe(res => console.log('Done'));
  }

  deleteTrip(id) {
    const uri = 'http://localhost:4200/trips/delete/' + id;

        return this
            .http
            .get(uri)
            .map(res => {
              return res;
            });
  }
}
