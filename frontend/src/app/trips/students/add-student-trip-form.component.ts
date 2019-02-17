import { Component } from '@angular/core';
import { FormArray, FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs/Subscription';

import { TripsApiService } from '../trips-api.service';
import { StudentsApiService } from './students-api.service';
import { Trip } from '../trip.model';
import { Student } from './student.model';

@Component({
  selector: 'add-student-trip-form',
  templateUrl: './add-student-trip-form.component.html',
  styles: [``]
})
export class AddStudentTripFormComponent {
  studentsListSubs: Subscription;
  studentGradeList: Array<Student>;
  students: Array<Student>;
  trip: Trip;
  form: FormGroup;
  assignStudents: Student;
  orders: Array<Student>;
  studentAssignList: Array<Student>;

  constructor(
    private tripsApi: TripsApiService,
    private studentsApi: StudentsApiService,
    private route: ActivatedRoute,
    private formBuilder: FormBuilder
  ) {
    // have to call getTrip in the constructor because we need the dependency
    // injection of FormBuilder
    this.getTrip();
  }

  setUpForm(): void {
    this.orders = this.studentGradeList;
    const controls = this.orders.map(() => new FormControl(true));
    this.form = this.formBuilder.group({
      orders: new FormArray(controls)
    });
  }
  getTripID(): void {
    const trip_id = +this.route.snapshot.paramMap.get('id');
    this.tripsApi
      .getTrip(trip_id)
      .subscribe(res => {
        this.trip = res;
      });
  }

  submit() {
    const trip_id = +this.route.snapshot.paramMap.get('id');
    const selectedOrderIds = this.form.value.orders
      .map((v, i) => v ? this.orders[i].id : null)
      .filter(v => v !== null);

    // use the selectedOrderIds to build the selectedStudents list
    this.studentsApi
      .assignStudentsToTrip(trip_id, selectedOrderIds);

  }

  ngOnInit() {
    // set default form to load the page properly
    this.form = new FormGroup({
      defaultControl: new FormControl()
    });
  }

  getStudentsInGrade(): void {
    this.studentsApi
      .getStudentsInGrade(this.trip.trip_grade)
      .subscribe(
        result => {
          this.studentGradeList = result;
          this.setUpForm(); // call set up form only after the student grade list
        }
      );
  }

  getTrip(): void {
    const TRIP_ID = +this.route.snapshot.paramMap.get('id');
    this.tripsApi
      .getTrip(TRIP_ID)
      .subscribe(res => {
        this.trip = res;
        this.getStudentsInGrade();
      });
  }

}
