import { Component, Input, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-button-sidebar',
  standalone: true,
  imports: [],
  templateUrl: './button-sidebar.component.html',
  styleUrl: './button-sidebar.component.css',
  encapsulation: ViewEncapsulation.None
})
export class ButtonSidebarComponent {
  @Input() button_text: string = "Texto";
}
