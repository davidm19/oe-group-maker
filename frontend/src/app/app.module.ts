import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { MatButtonModule, MatCardModule, MatInputModule, MatSelectModule, MatToolbarModule } from '@angular/material';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { HttpModule } from '@angular/http';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { TripsApiService } from './trips/trips-api.service';
import { TripFormComponent } from './trips/trip-form.component';
import { StudentsApiService } from './trips/students/students-api.service';

import { TripsComponent } from './trips/trips.component';
import { HomeComponent } from './home/home.component';
import { TripDetailComponent } from './trips/trip-detail.component';
import { AddStudentTripFormComponent } from './trips/students/add-student-trip-form.component';
import { PreferencesComponent } from './preferences/preferences.component';

const appRoutes: Routes = [
  { path: 'trips', component: TripsComponent },
  { path: 'trips/new', component: TripFormComponent },
  { path: 'trips/:id/getStudentsInGrade', component: AddStudentTripFormComponent },
  { path: '', component: HomeComponent },
  { path: 'home', component: HomeComponent },
  { path: 'trips/:id/detail', component: TripDetailComponent },
  { path: 'trips/:id/assignStudentsToTrip', component: AddStudentTripFormComponent},
  { path: 'student/:id/preferences', component: PreferencesComponent}

]
;

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    TripsComponent,
    HomeComponent,
    TripFormComponent,
    TripDetailComponent,
    AddStudentTripFormComponent,
    PreferencesComponent,

  ],
  imports: [
    BrowserAnimationsModule,
    BrowserModule,
    FormsModule,
    HttpModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes),
    MatInputModule,
    MatCardModule,
    MatButtonModule,
    MatSelectModule,
    MatToolbarModule,
    ReactiveFormsModule

  ],
  providers: [TripsApiService, StudentsApiService, HttpModule],
  bootstrap: [AppComponent]
})
export class AppModule {
}
