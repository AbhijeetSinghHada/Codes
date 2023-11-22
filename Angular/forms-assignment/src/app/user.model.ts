import { ReimburesmentModel } from './reimbursement.model';
export class UserModel {
  constructor(
    public name: string,
    public id: number,
    public designation: string,
    public reimburesment: ReimburesmentModel[]
  ) {}
}
