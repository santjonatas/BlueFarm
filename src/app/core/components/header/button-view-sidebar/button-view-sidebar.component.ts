import { Component } from '@angular/core';
import { SidebarService } from '../../../../shared/services/sidebar.service';

@Component({
  selector: 'app-button-view-sidebar',
  standalone: true,
  templateUrl: './button-view-sidebar.component.html',
  styleUrls: ['./button-view-sidebar.component.css']
})
export class ButtonViewSidebarComponent {
  constructor(private sidebarService: SidebarService) {}

  onClick() {
    console.log('onClick chamado');
    this.sidebarService.toggleSidebar();
  }
}