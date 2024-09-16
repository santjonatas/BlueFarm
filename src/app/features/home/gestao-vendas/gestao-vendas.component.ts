import { Component, ViewEncapsulation } from '@angular/core';
import { CardModuloComponent } from "../../../core/components/card-modulo/card-modulo.component";

@Component({
  selector: 'app-gestao-vendas',
  standalone: true,
  imports: [CardModuloComponent],
  templateUrl: './gestao-vendas.component.html',
  styleUrl: './gestao-vendas.component.css',
  encapsulation: ViewEncapsulation.None
})
export class GestaoVendasComponent {

}
