import { Component } from '@angular/core';
import { ButtonViewSidebarComponent } from "./button-view-sidebar/button-view-sidebar.component";

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [ButtonViewSidebarComponent],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {

}
