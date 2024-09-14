import { Component, ViewEncapsulation } from '@angular/core';
import { CardModuloComponent } from "../../../core/components/card-modulo/card-modulo.component";

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CardModuloComponent],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css',
  encapsulation: ViewEncapsulation.None
})
export class DashboardComponent {

}
