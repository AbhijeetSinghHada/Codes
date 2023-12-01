import { Component } from '@angular/core';
import { AnalyticsService } from 'src/standalone-components-routing/shared/analytics.service';
import { HighlightDirective } from 'src/standalone-components-routing/shared/highlight.directive';
@Component({
  standalone: true,
  selector: 'app-details',
  imports: [HighlightDirective],
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css'],
})
export class DetailsComponent {
  constructor(private analyticsService: AnalyticsService) {}

  onClick() {
    this.analyticsService.registerClick();
  }
}
