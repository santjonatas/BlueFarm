import { NgOptimizedImage } from '@angular/common';
import { Component, Input, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-card-modulo',
  standalone: true,
  imports: [NgOptimizedImage],
  templateUrl: './card-modulo.component.html',
  styleUrl: './card-modulo.component.css',
  encapsulation: ViewEncapsulation.None
})
export class CardModuloComponent {
  @Input() card_text: string="";
}
