import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ButtonViewSidebarComponent } from './button-view-sidebar.component';

describe('ButtonViewSidebarComponent', () => {
  let component: ButtonViewSidebarComponent;
  let fixture: ComponentFixture<ButtonViewSidebarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ButtonViewSidebarComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ButtonViewSidebarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
