import { Component, Input, Output, EventEmitter, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-button-sidebar',
  standalone: true,
  templateUrl: './button-sidebar.component.html',
  styleUrls: ['./button-sidebar.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class ButtonSidebarComponent {
  @Input() button_text: string = "Texto";
  @Output() buttonClick = new EventEmitter<string>();

  onClick() {
    this.buttonClick.emit(this.button_text);
  }
}
