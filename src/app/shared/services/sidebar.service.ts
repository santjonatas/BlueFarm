import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SidebarService {
  private sidebarVisible = new BehaviorSubject<boolean>(true); 
  sidebarVisibility$ = this.sidebarVisible.asObservable();

  toggleSidebar() {
    console.log('toggleSidebar chamado');
    this.sidebarVisible.next(!this.sidebarVisible.value);
  }
}
