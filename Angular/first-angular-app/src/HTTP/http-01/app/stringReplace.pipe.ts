import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'replaceString',
})
export class StringReplacePipe implements PipeTransform {
  transform(value: string, fromReplace: string, toReplace: string) {
    return value.replaceAll(fromReplace, toReplace);
  }
}
