import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap, Router } from '@angular/router';
import { PreferencesApiService } from './preferences-api.service';
import { Student } from '../trips/students/student.model';

@Component({
  selector: 'app-preferences',
  templateUrl: './preferences.component.html',
  styleUrls: ['./preferences.component.css']
})
export class PreferencesComponent implements OnInit {

  preferenceList: Array<Student>;

  constructor(private route: ActivatedRoute,
              private preferencesApi: PreferencesApiService) { }

  ngOnInit() {
    this.getPreferences();
  }

  getPreferences(): void  {
    const STUDENT_ID = +this.route.snapshot.paramMap.get('id');
    this.preferencesApi.getStudentPreferences(STUDENT_ID)
    .subscribe(res => this.preferenceList = res);
  }



}
