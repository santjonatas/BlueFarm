import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GestaoVendasComponent } from './gestao-vendas.component';

describe('GestaoVendasComponent', () => {
  let component: GestaoVendasComponent;
  let fixture: ComponentFixture<GestaoVendasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GestaoVendasComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GestaoVendasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
