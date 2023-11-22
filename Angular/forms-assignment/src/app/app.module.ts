import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { InputDataComponent } from './input-data/input-data.component';
import { DisplayDataComponent } from './display-data/display-data.component';
import { UserService } from './user.service';

@NgModule({
  declarations: [AppComponent, InputDataComponent, DisplayDataComponent],
  imports: [BrowserModule, FormsModule],
  providers: [UserService],
  bootstrap: [AppComponent],
})
export class AppModule {}
