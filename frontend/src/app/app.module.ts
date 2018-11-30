import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';

import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { Routes, RouterModule} from '@angular/router';
import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { TripsApiService } from './trips/trips-api.service';
import { TripFormComponent } from './trips/trip-form.component';

import {TripsComponent} from './trips/trips.component';
import { HomeComponent } from './home/home.component';

const appRoutes: Routes = [
  { path: 'trips', component: TripsComponent },
  { path: 'new-trip', component: TripFormComponent },
  { path: '', component: HomeComponent },
  { path: 'home', component: HomeComponent }

]

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    TripsComponent,
    HomeComponent,
    TripFormComponent

  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [TripsApiService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
