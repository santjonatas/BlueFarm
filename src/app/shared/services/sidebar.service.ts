// import { Injectable } from '@angular/core';

// @Injectable({
//   providedIn: 'root'
// })
// export class SidebarService {

//   constructor() { }

// }
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root' // Certifique-se de que o serviço está disponível globalmente
})
export class SidebarService {
  private sidebarVisible = new BehaviorSubject<boolean>(true); // Inicialmente visível
  sidebarVisibility$ = this.sidebarVisible.asObservable();

  toggleSidebar() {
    console.log('toggleSidebar chamado'); // Adicione logs para verificação
    this.sidebarVisible.next(!this.sidebarVisible.value);
  }
}
