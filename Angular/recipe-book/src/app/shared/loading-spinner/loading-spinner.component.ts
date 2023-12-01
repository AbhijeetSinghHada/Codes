import { Component } from '@angular/core';

@Component({
  selector: 'app-loading-spinner',
  template: '<div class="lds-spinner"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>', // prettier-ignore
  styleUrls: ['./loading-spinner.component.css'],
})
export class LoadingSpinner {}
