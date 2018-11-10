import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {TripsApiService} from './trips/trips-api.service';
import {Trip} from './trips/trip.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  tripsListSubs: Subscription;
  tripsList: Trip[];

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
}
