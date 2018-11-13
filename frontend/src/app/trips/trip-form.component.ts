import {Component} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {TripsApiService} from "./trips-api.service";
import {Router} from "@angular/router";

@Component({
  selector: 'trip-form',
  template: `
    <div>
      <h2>New Trip</h2>
      <label for="trip_name">Name</label>
      <input id="trip_name" (keyup)="updateName($event)">
      <button (click)="saveTrip()">Save Trip</button>
    </div>
  `
})
export class TripFormComponent {
  trip = {
    trip_name: ''
  };

  constructor(private tripsApi: TripsApiService, private router: Router) { }

  updateName(event: any) {
    this.trip.trip_name = event.target.value;
  }


  saveTrip() {
    this.tripsApi
      .saveTrip(this.trip)
      .subscribe(
        () => this.router.navigate(['/']),
        error => alert(error.message)
      );
  }
}
