export class DataService {
  getData() {
    const result = new Promise<string>((resolve, reject) => {
      setTimeout(() => {
        resolve('Data');
      }, 2000);
    });
    return result;
  }
}