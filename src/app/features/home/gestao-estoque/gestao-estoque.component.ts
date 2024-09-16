import { Component, ViewEncapsulation } from '@angular/core';
import { CardModuloComponent } from "../../../core/components/card-modulo/card-modulo.component";

@Component({
  selector: 'app-gestao-estoque',
  standalone: true,
  imports: [CardModuloComponent],
  templateUrl: './gestao-estoque.component.html',
  styleUrl: './gestao-estoque.component.css',
  encapsulation: ViewEncapsulation.None
})
export class GestaoEstoqueComponent {
  
}
