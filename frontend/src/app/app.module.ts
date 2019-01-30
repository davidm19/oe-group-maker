import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { MatButtonModule, MatCardModule, MatInputModule, MatToolbarModule } from '@angular/material';
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

const appRoutes: Routes = [
  { path: 'trips', component: TripsComponent },
  { path: 'trips/new', component: TripFormComponent },
  { path: 'trips/:id/getStudentsInGrade', component: AddStudentTripFormComponent },
  { path: '', component: HomeComponent },
  { path: 'home', component: HomeComponent },
  { path: 'trips/:id/detail', component: TripDetailComponent }

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
    AddStudentTripFormComponent

  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes),
    MatInputModule,
    MatCardModule,
    MatButtonModule,
    MatToolbarModule,
    ReactiveFormsModule

  ],
  providers: [TripsApiService, StudentsApiService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
