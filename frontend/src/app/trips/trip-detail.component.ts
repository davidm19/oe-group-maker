import { switchMap } from 'rxjs/operators';
import { Component, OnInit, Input } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { Observable } from 'rxjs';

import { TripsApiService }  from './trips-api.service';
import { Trip } from './trip.model';
import { TripsComponent } from './trips.component';
import { TripsModule } from './trips.module';
import { Student } from './students/student.model';
import { StudentsApiService } from './students/students-api.service';


@Component({
  selector: 'app-trip-detail',
  templateUrl: './trip-detail.component.html',
  // styleUrls: ['./trip-detail.component.css']
})
export class TripDetailComponent implements OnInit {
  // tripsListSubs: Subscription;
  // tripsList: Trip[];
  // trips: Observable<Trip[]>;
  // trip: Observable<Trip>;
  studentGradeList: Student[];
  tripStudentList: Student[];
  trip: Trip;

  constructor(
    private tripsApi: TripsApiService,
    private route: ActivatedRoute,
    private studentsApi: StudentsApiService
   )
    { }

    ngOnInit() {
      this.getTrip();
      this.getStudentsInTrip();

    }


  getTrip(): void {
    const trip_id = +this.route.snapshot.paramMap.get('id');
    console.log(trip_id);
    this.tripsApi.getTrip(trip_id).subscribe(res => {
        this.trip = res;
      },
      console.error
    )
    console.log(this.trip);
  }

  getStudentsInTrip(): void {
    console.log("Calling getStudentsInTrip");
    const trip_id = +this.route.snapshot.paramMap.get('id');
    console.log(trip_id);
    this.tripsApi.getStudentsInTrip(trip_id).subscribe(
      res => {
      console.log("Students in trip " + this.trip.trip_name);
      console.log(res);
      this.tripStudentList = res;
    }
  );
}

  getStudentsInGrade(): void {
  console.log("Calling getStudentsInGrade");
  console.log(this.trip);
     this.studentsApi.getStudentsInGrade(this.trip.trip_grade).subscribe(
      result => {
        console.log("Students in grade" + this.trip.trip_grade);
        console.log(result);
        this.studentGradeList = result;
      }
   );

   }
}
