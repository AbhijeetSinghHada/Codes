import {
  Directive,
  ElementRef,
  HostBinding,
  HostListener,
  Renderer2,
} from '@angular/core';

@Directive({
  selector: '[appDropdown]',
})
export class DropdownDirective {
  constructor(
    private elementReference: ElementRef,
    private renderer: Renderer2
  ) {}
  @HostBinding('class.open') isOpen: boolean = false;
  @HostListener('document:click', ['$event']) toggleOpen(event: Event) {
    this.isOpen = this.elementReference.nativeElement.contains(event.target)
      ? !this.isOpen
      : false;
  }
  @HostListener('mouseover') onHover() {
    this.renderer.addClass(this.elementReference.nativeElement, 'open');
    console.log(this.elementReference);
  }
  @HostListener('mouseleave') onMouseOut() {
    this.renderer.removeClass(this.elementReference.nativeElement, 'open');
    console.log(this.elementReference);
  }
}
