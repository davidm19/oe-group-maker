import {Component, OnDestroy, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {TripsApiService} from '../trips-api.service';
import {StudentsApiService} from './students-api.service';
import {Router, ActivatedRoute} from "@angular/router";
import {Subscription} from 'rxjs/Subscription';
import {Observable} from 'rxjs/Observable';


import { Trip } from '../trip.model';
import { TripsComponent } from '../trips.component';
import { TripsModule } from '../trips.module';
import { Student } from './student.model';

@Component({
  selector: 'add-student-trip-form',
  templateUrl: './add-student-trip-form.component.html',
  styles: [`
`]
})
export class AddStudentTripFormComponent {
  studentsListSubs: Subscription;
  studentGradeList: Student[];
  students: Observable<Student[]>;
  trip: Trip;


  constructor(
    private tripsApi: TripsApiService,
    private studentsApi: StudentsApiService,
    private route: ActivatedRoute,

  )
  { }

  ngOnInit() {
    this.getTrip();



  }

  getTrip(): void {
    const trip_id = +this.route.snapshot.paramMap.get('id');
    console.log(trip_id);
    this.tripsApi.getTrip(trip_id).subscribe(res => {
        this.trip = res;
        console.log("Printing trip");
        console.log(this.trip);
        this.getStudentsInGrade();

      },
      console.error
    );



  }

  getStudentsInGrade(): void {
  //   """I have absolutely no idea of how to implement this"""
  //   """Please help me"""
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
