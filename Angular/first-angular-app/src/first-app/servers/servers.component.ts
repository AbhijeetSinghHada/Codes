import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-servers',
  templateUrl: './servers.component.html',
  styles: [
    `
      .colorItems {
        color: black;
        background-color: pink;
      }
    `,
  ],
})
export class ServersComponent implements OnInit {
  allowNewServer: boolean = false;
  serverCreationStatus = 'No Server was Created';
  serverName = 'Apache';
  serverStatus = false;
  servers = ['Hello', 'Hello2'];
  constructor() {
    setTimeout(() => {
      this.allowNewServer = true;
    }, 2000);
  }
  ngOnInit() {}
  onCreateServer() {
    this.servers.push(this.serverName);
    this.serverStatus = true;
    this.serverCreationStatus =
      'Server Created Successfully : ' + this.serverName;
  }
  onUpdateServerName(event: any) {
    console.log(event);
    this.serverName = event.target.value;
  }

  // username = '';
  // allowButton = false;
  // modifyButton(event) {
  //   if (event.target.value == '') {
  //     this.allowButton = false;
  //   } else {
  //     this.allowButton = true;
  //   }
  // }
  // resetUserName() {
  //   this.username = '';
  // }
  clickCounter = 0;
  arrayClicks = [];
  passwordVisibility = false;
  afterClick() {
    this.passwordVisibility = !this.passwordVisibility;
    this.arrayClicks.push(++this.clickCounter);
  }
}
