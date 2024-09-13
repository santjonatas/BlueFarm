import { Component } from '@angular/core';
import { HeaderComponent } from "../../core/components/header/header.component";
import { SidebarComponent } from "../../core/components/sidebar/sidebar.component";

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [HeaderComponent, SidebarComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

}
