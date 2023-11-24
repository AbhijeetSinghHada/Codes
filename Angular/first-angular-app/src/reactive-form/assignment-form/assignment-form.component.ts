import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-assignment-form',
  templateUrl: './assignment-form.component.html',
})
export class AssignmentFormComponent {
  projectForm: FormGroup;
  constructor() {
    this.projectForm = new FormGroup({
      name: new FormControl(
        null,
        [Validators.required],
        this.asyncProjectNameValidator
      ),
      mail: new FormControl(null, [Validators.required, Validators.email]),
      status: new FormControl(null),
    });
  }
  onSubmit() {
    console.log(this.projectForm);
  }
  projectNameValidator(control: FormControl): { [s: string]: boolean } {
    if (control.value === 'Test') {
      return { invalidProjectName: true };
    }
    return null;
  }
  asyncProjectNameValidator(
    control: FormControl
  ): Promise<any> | Observable<any> {
    let promise = new Promise((resolve, reject) => {
      setTimeout(() => {
        if (control.value === 'test') {
          resolve({ invalidProjectName: true });
        } else {
          resolve(null);
        }
      }, 2000);
    });
    return promise;
  }
}
