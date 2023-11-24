import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'sort',
})
export class SortPipe implements PipeTransform {
  transform(value: Array<any>) {
    console.log(value);

    const val = value.sort((a, b) => {
      const t1 = a.name;
      const t2 = b.name;
      if (t1 == t2) return 0;
      else if (t1 > t2) {
        return 1;
      } else return -1;
    });
    console.log(val);
    return value.sort();
  }
}
