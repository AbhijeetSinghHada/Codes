import { Directive, ElementRef, HostListener, Renderer2 } from '@angular/core';

@Directive({
  selector: '[testingDir]',
})
export class TestingDirective {
  constructor(private elRef: ElementRef, private renderer: Renderer2) {}

  @HostListener('mouseover') onHover() {
    this.renderer.setProperty(
      this.elRef.nativeElement,
      'innerHTML',
      'HLWALSGEHDGS'
    );
    console.log(this.elRef);
  }
}
