import { Component } from '@angular/core';
import { DetailsComponent } from 'src/standalone-components-routing/welcome/details/details.component';

@Component({
  standalone: true,
  selector: 'app-welcome',
  imports: [DetailsComponent],
  templateUrl: './welcome.component.html',
})
export class WelcomeComponent {}
