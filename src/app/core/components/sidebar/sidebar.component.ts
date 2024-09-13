import { Component } from '@angular/core';
import { ButtonSidebarComponent } from "./button-sidebar/button-sidebar.component";

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [ButtonSidebarComponent],
  templateUrl: './sidebar.component.html',
  styleUrl: './sidebar.component.css'
})
export class SidebarComponent {

}
