import { switchMap } from 'rxjs/operators';
import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { Observable } from 'rxjs';

import { TripsApiService }  from './trips-api.service';
import { Trip } from './trip.model';
import { TripsComponent } from './trips.component';
import { TripsModule } from './trips.module';

@Component({
  selector: 'app-trip-detail',
  templateUrl: './trip-detail.component.html',
  // styleUrls: ['./trip-detail.component.css']
})
export class TripDetailComponent implements OnInit {
  tripsListSubs: Subscription;
  tripsList: Trip[];
  trips: Observable<Trip[]>;
  trip: Observable<Trip>;

  constructor(
    private tripsApi: TripsApiService) {}

    ngOnInit() {
      this.getTrip();
    }

  getTrip() {
    this.tripsListSubs = this.tripsApi
      .getTrip(trip)
      .subscribe(res => {
          this.trip = res;
        },
        console.error
      );
  }

  goToTrips(trip: Trip) {
    let trip_id = trip ? trip.id : null;
    // Pass along the hero id if available
    // so that the HeroList component can select that hero.
    // Include a junk 'foo' property for fun.
    this.router.navigate(['/trips']);
  }
}
