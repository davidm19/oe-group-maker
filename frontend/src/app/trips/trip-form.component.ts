import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { TripsApiService } from './trips-api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'trip-form',
  templateUrl: './trip-form.component.html',
  styles: [`
  .full-width {
    width: 100%;
  }
`]
})

export class TripFormComponent {
  trip = {
    trip_name: '',
    trip_grade: ''
  };

  grades = [
    { id: 7, value: '7' },
    { id: 8, value: '8' },
    { id: 9, value: '9' },
    { id: 10, value: '10' },
    { id: 11, value: '11' },
    { id: 12, value: '12' }
  ];

  constructor(private tripsApi: TripsApiService, private router: Router) { }

  updateName(event: any) {
    this.trip.trip_name = event.target.value;
  }

  updateGrade(event: any) {
    this.trip.trip_grade = event.target.value;
    console.log("updating grade")
    console.log(event.target.value)
  }

  saveTrip() {
    this.tripsApi
      .saveTrip(this.trip)
      .subscribe(
        () => this.router.navigate(['/trips']),
        error => alert(error.message)
      );
      console.log("Trip grade is " + this.trip.trip_grade)
  }
}
