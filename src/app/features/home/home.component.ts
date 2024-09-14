import { Component } from '@angular/core';
import { HeaderComponent } from "../../core/components/header/header.component";
import { SidebarComponent } from "../../core/components/sidebar/sidebar.component";
import { DashboardComponent } from "./dashboard/dashboard.component";

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [HeaderComponent, SidebarComponent, DashboardComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

}
