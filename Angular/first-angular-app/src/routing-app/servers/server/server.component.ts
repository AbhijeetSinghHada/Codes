import { Component, OnInit } from '@angular/core';

import { ServersService } from '../servers.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-server',
  templateUrl: './server.component.html',
  styleUrls: ['./server.component.css'],
})
export class ServerComponent implements OnInit {
  server: { id: number; name: string; status: string };
  id: any;
  constructor(
    private serversService: ServersService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit() {
    this.id = this.route.snapshot.params.id;
    this.server = this.serversService.getServer(parseInt(this.id));
    this.route.params.subscribe((params) => {
      this.server = this.serversService.getServer(+params.id);
    });
  }
  onEdit() {
    console.log(this.server);
    this.router.navigate(['edit'], {
      relativeTo: this.route,
      queryParamsHandling: 'preserve',
    });
  }
}
