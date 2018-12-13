import { switchMap } from 'rxjs/operators';
import { Component, OnInit, Input } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { Observable } from 'rxjs';

import { TripsApiService }  from './trips-api.service';
import { Trip } from './trip.model';
import { TripsComponent } from './trips.component';
import { TripsModule } from './trips.module';
import { Student } from './students/student.model';


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
  trip: Trip;

  constructor(
    private tripsApi: TripsApiService,
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
      },
      console.error
    )
    console.log(this.trip);
    // this.tripsListSubs = this.tripsApi
    //   .getTrip(trip)
    //   .subscribe(res => {
    //       this.trip = res;
    //     },
    //     console.error
    //   );
  }
}
