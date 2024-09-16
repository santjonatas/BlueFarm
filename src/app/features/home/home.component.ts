// import { Component } from '@angular/core';
// import { HeaderComponent } from "../../core/components/header/header.component";
// import { SidebarComponent } from "../../core/components/sidebar/sidebar.component";
// import { DashboardComponent } from "./dashboard/dashboard.component";

// @Component({
//   selector: 'app-home',
//   standalone: true,
//   imports: [HeaderComponent, SidebarComponent, DashboardComponent],
//   templateUrl: './home.component.html',
//   styleUrl: './home.component.css'
// })
// export class HomeComponent {

// }
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SidebarService } from '../../shared/services/sidebar.service';
import { HeaderComponent } from "../../core/components/header/header.component";
import { SidebarComponent } from "../../core/components/sidebar/sidebar.component";
import { DashboardComponent } from "./dashboard/dashboard.component";

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, HeaderComponent, SidebarComponent, DashboardComponent],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  sidebarVisible = true;

  constructor(private sidebarService: SidebarService) {}

  ngOnInit() {
    this.sidebarService.sidebarVisibility$.subscribe(visible => {
      this.sidebarVisible = visible;
    });
  }
}