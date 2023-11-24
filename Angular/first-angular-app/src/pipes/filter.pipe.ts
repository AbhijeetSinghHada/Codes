import { Pipe, PipeTransform } from '@angular/core';
@Pipe({
  name: 'filter',
  pure: false,
})
export class FilterPipe implements PipeTransform {
  transform(value: any, filterString: string, property: string) {
    if (value.length === 0 || filterString === '') return value;
    const resultArray = [];
    for (let i of value) {
      if (i[property] === filterString) {
        resultArray.push(i);
      }
    }
    return resultArray;
  }
}
