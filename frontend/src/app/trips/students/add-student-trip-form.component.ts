import {Component} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {TripsApiService} from '../trips-api.service';
import {StudentsApiService} from './students-api.service';
import {Router} from "@angular/router";

@Component({
  selector: 'add-student-trip-form',
  templateUrl: './add-student-trip-form.component.html',
  styles: [`
`]
})
export class AddStudentTripFormComponent {
  trip = {
    trip_name: '',
    trip_grade: '',
  };

  constructor(private tripsApi: TripsApiService, private router: Router) { }

  // updateName(event: any) {
  //   this.trip.trip_name = event.target.value;
  // }
  //
  // updateGrade(event: any) {
  //   this.trip.trip_grade = event.target.value;
  // }
  //
  //
  // saveTrip() {
  //   this.tripsApi
  //     .saveTrip(this.trip)
  //     .subscribe(
  //       () => this.router.navigate(['/trips']),
  //       error => alert(error.message)
  //     );
  // }
}
