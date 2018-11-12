import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';

import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { Routes, RouterModule} from '@angular/router';
import {AppComponent} from './app.component';
import {HeaderComponent} from './header/header.component';
import {TripsApiService} from './trips/trips-api.service';

import {TripsComponent} from './trips/trips.component';
import { HomeComponent } from './home/home.component';

const appRoutes: Routes = [
  { path: 'trips', component: TripsComponent }
]

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    TripsComponent,
    HomeComponent
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
