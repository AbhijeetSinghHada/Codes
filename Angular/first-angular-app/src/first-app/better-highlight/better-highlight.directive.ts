import {
  Directive,
  ElementRef,
  HostBinding,
  HostListener,
  Renderer2,
} from '@angular/core';

@Directive({
  selector: '[appBetterHighlight]',
})
export class BetterHighlightDirective {
  constructor(private elRef: ElementRef, private renderer: Renderer2) {}

  @HostBinding('style.backgroundColor') backgroundColor: string = 'transparent';

  @HostListener('mouseenter') mouseOver(eventData: Event) {
    // this.renderer.setStyle(
    //   this.elRef.nativeElement,
    //   'background-color',
    //   'grey'
    // );
    this.backgroundColor = 'grey'; // Now we can use bg without renderer
    this.renderer.setStyle(this.elRef.nativeElement, 'color', 'white');
  }
  @HostListener('mouseleave') mouseOut(eventData: Event) {
    // this.renderer.setStyle(
    //   this.elRef.nativeElement,
    //   'background-color',
    //   'transparent'
    // );
    this.backgroundColor = 'pink'; // Now we can use bg without renderer
    this.renderer.setStyle(this.elRef.nativeElement, 'color', 'black');
  }
}
