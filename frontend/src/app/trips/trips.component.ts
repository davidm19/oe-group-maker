import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs/Subscription';
import { Trip } from './trip.model';
import { TripsApiService } from './trips-api.service';
import { Observable } from 'rxjs/Observable';

@Component({
  selector: 'app-trips',
  templateUrl: './trips.component.html',
  styles: [`
    div.trips {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 15px;
}

button.new-trip {
  position: fixed;
  bottom: 15px;
  right: 15px;
}

@media (max-width: 720px) {
  div.trips {
    grid-template-columns: 1fr;
  }

`]
})
export class TripsComponent implements OnInit, OnDestroy {
  tripsListSubs: Subscription;
  tripsList: Array<Trip>;
  trips: Array<Trip>;

  constructor(private tripsApi: TripsApiService) {
  }

  ngOnInit() {
    this.tripsListSubs = this.tripsApi
      .getTrips()
      .subscribe(res => {
          this.tripsList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.tripsListSubs.unsubscribe();
  }

  delete(TRIP_ID: number) {
  this.tripsApi
    .deleteTrip(TRIP_ID)
    .subscribe(() => {
      this.tripsListSubs = this.tripsApi
        .getTrips()
        .subscribe(res => {
            this.tripsList = res;
          },
          console.error
        );
    }, console.error);
}
}
