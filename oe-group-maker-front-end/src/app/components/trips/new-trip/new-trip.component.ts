import { Component, OnInit, ViewChild} from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-new-trip',
  templateUrl: './new-trip.component.html',
  styleUrls: ['./new-trip.component.css']
})
export class NewTripComponent implements OnInit {

  @ViewChild('f') newTripForm: NgForm;

  constructor() { }

  ngOnInit() {
  }

  onSubmit() {
    console.log(this.newTripForm);
  }
}
