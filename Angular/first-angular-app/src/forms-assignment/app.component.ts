import { Component, OnChanges, ViewChild } from '@angular/core';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  @ViewChild('assignmentForm') formData: NgForm;
  dataTemplate = {
    reimbursement_id: null,
    reimbursement_name: '',
    reimbursement_amount: 0,
    reimbursement_type: 'cash',
  };
  showTable: boolean = false;
  userDataArray: any = [
    {
      reimbursement_id: 1,
      reimbursement_name: 'Chair',
      reimbursement_amount: 300,
      reimbursement_type: 'cheque',
    },
    {
      reimbursement_id: 2,
      reimbursement_name: 'Table',
      reimbursement_amount: 700,
      reimbursement_type: 'cash',
    },
  ];

  updateData() {
    console.log(this.formData.form.value);
    this.userDataArray = [];
    for (let group of Object.values(this.formData.form.value)) {
      this.userDataArray.push(group);
    }
  }

  onSubmit() {
    this.updateData();
    this.showTable = !this.showTable;
  }
  onDelete(index: number) {
    this.userDataArray.splice(index, 1);
  }
  onAdd() {
    this.userDataArray.push(this.dataTemplate);
  }
}
