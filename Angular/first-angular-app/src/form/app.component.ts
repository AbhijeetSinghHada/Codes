import { Component, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  suggestUserName() {
    const suggestedName = 'Superuser';
    // this is not the right way to update the form, as this will override the entire form
    // this.formData.setValue({
    //   userData: {
    //     username: 'Superuser',
    //     email: '',
    //   },
    //   secret: 'teacher',
    //   gender: 'Male',
    // });
    this.formData.form.patchValue({
      // patchValue is used to update only some of the form fields
      userData: {
        username: 'Superuser',
      },
    });
  }
  @ViewChild('f') formData: NgForm;
  defaultQuestion = 'pet';
  defaultSubscription = 'basic';
  genders = ['Male', 'Female'];
  user = {
    username: '',
    email: '',
    secret: '',
    gender: '',
  };
  submitted = false;
  ngOnInit() {
    console.log(this.formData);
    let newArr = this.mapPolly([1, 2, 3, 4, 5], (ele) => {
      return ele * 2;
    });

    console.log(newArr);
  }
  onSubmit(form: NgForm) {
    console.log(form);
    form.addFormGroup;
    this.submitted = true;
    this.user.username = this.formData.value.userData.username;
    this.user.email = this.formData.value.userData.email;
    this.user.secret = this.formData.value.secret;
    this.user.gender = this.formData.value.gender;

    this.formData.reset();
  }

  mapPolly = (arr, func: Function) => {
    let temp = [];
    for (let ele of arr) {
      temp.push(func(ele));
    }
    return temp;
  };

  onSubmitAssignment() {}
}
