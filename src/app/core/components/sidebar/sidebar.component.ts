// import { Component } from '@angular/core';
// import { ButtonSidebarComponent } from "./button-sidebar/button-sidebar.component";

// @Component({
//   selector: 'app-sidebar',
//   standalone: true,
//   imports: [ButtonSidebarComponent],
//   templateUrl: './sidebar.component.html',
//   styleUrl: './sidebar.component.css'
// })
// export class SidebarComponent {

// }
import { Component, Output, EventEmitter } from '@angular/core';
import { ButtonSidebarComponent } from './button-sidebar/button-sidebar.component';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [ButtonSidebarComponent],
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent {
  @Output() moduleSelect = new EventEmitter<string>();

  onButtonClick(buttonText: string) {
    this.moduleSelect.emit(buttonText);
  }
}
