import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TripDetailComponent } from './trip-detail.component';
import { TripDetailbrewComponent } from './trip-detailbrew/trip-detailbrew.component';


@NgModule({
  imports: [
    CommonModule,
  ],
  declarations: [TripDetailComponent, TripDetailbrewComponent]
})
export class TripsModule { }
