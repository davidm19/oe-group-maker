import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <!-- header -->
    <app-header></app-header>

    <!-- footer -->
    <app-footer></app-footer>
  `,
  styles: []
})

export class AppComponent {
  title = 'oe-group-maker-front-end';
}
