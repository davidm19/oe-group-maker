import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { TripsApiService } from './trips-api.service';
import { Trip } from './trip.model';
import { Student } from './students/student.model';
import { StudentsApiService } from './students/students-api.service';

@Component({
  selector: 'app-trip-detail',
  templateUrl: './trip-detail.component.html'
  // styleUrls: ['./trip-detail.component.css']
})
export class TripDetailComponent implements OnInit {
  studentGradeList: Array<Student>;
  tripStudentList: Array<Student>;
  trip: Trip;

  constructor(
    private tripsApi: TripsApiService,
    private route: ActivatedRoute,
    private studentsApi: StudentsApiService
  ) {

  }

  ngOnInit() {
    this.getTrip();
    this.getStudentsInTrip();
  }

  getTrip(): void {
    const trip_id = +this.route.snapshot.paramMap.get('id');
    this.tripsApi
      .getTrip(trip_id)
      .subscribe(res => {
        this.trip = res;
      });
  }

  getStudentsInTrip(): void {
    const TRIP_ID = +this.route.snapshot.paramMap.get('id');
    this.tripsApi
      .getStudentsInTrip(TRIP_ID)
      .subscribe(
        res => {
          this.tripStudentList = res;
        }
      );
  }

  getStudentsInGrade(): void {
    this.studentsApi
      .getStudentsInGrade(this.trip.trip_grade)
      .subscribe(
        result => {
          this.studentGradeList = result;
        }
      );

  }
}
