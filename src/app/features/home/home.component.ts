// import { Component, OnInit } from '@angular/core';
// import { CommonModule } from '@angular/common';
// import { SidebarService } from '../../shared/services/sidebar.service';
// import { HeaderComponent } from "../../core/components/header/header.component";
// import { SidebarComponent } from "../../core/components/sidebar/sidebar.component";
// import { DashboardComponent } from "./dashboard/dashboard.component";

// @Component({
//   selector: 'app-home',
//   standalone: true,
//   imports: [CommonModule, HeaderComponent, SidebarComponent, DashboardComponent],
//   templateUrl: './home.component.html',
//   styleUrls: ['./home.component.css']
// })
// export class HomeComponent implements OnInit {
//   sidebarVisible = true;

//   constructor(private sidebarService: SidebarService) {}

//   ngOnInit() {
//     this.sidebarService.sidebarVisibility$.subscribe(visible => {
//       this.sidebarVisible = visible;
//     });
//   }
// }
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SidebarService } from '../../shared/services/sidebar.service';
import { HeaderComponent } from "../../core/components/header/header.component";
import { SidebarComponent } from "../../core/components/sidebar/sidebar.component";
import { DashboardComponent } from "./dashboard/dashboard.component";
import { ControleProducaoComponent } from "./controle-producao/controle-producao.component";
import { GestaoEstoqueComponent } from "./gestao-estoque/gestao-estoque.component";
import { GestaoVendasComponent } from "./gestao-vendas/gestao-vendas.component";
import { ConfiguracoesComponent } from "./configuracoes/configuracoes.component";

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, HeaderComponent, SidebarComponent, DashboardComponent, ControleProducaoComponent, GestaoEstoqueComponent, GestaoVendasComponent, ConfiguracoesComponent],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  sidebarVisible = true;
  currentModule: string = '';

  constructor(private sidebarService: SidebarService) {}

  ngOnInit() {
    this.sidebarService.sidebarVisibility$.subscribe(visible => {
      this.sidebarVisible = visible;
    });
  }

  onModuleSelect(module: string) {
    this.currentModule = module;
  }
}
