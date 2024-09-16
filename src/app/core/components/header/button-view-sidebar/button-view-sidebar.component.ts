// import { Component } from '@angular/core';
// import { SidebarService } from '../../../../shared/services/sidebar.service';

// @Component({
//   selector: 'app-button-view-sidebar',
//   standalone: true,
//   imports: [],
//   templateUrl: './button-view-sidebar.component.html',
//   styleUrl: './button-view-sidebar.component.css'
// })
// export class ButtonViewSidebarComponent {

// }
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
    console.log('onClick chamado'); // Adicione logs para verificação
    this.sidebarService.toggleSidebar();
  }
}