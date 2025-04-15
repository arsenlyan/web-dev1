import { Component } from '@angular/core';
import { Company } from '../interfaces/company';
import { CompanyService } from '../company-service.service';
import { Vacancy } from '../interfaces/vacancy';
import { CommonModule} from '@angular/common';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  imports: [CommonModule]
})

export class CompaniesComponent {
  companies: Company[] = [];
  selectedVacancies: Vacancy[] = [];
  selectedCompanyId: number | null = null;
  selectedCompanyName: string | null = null;

  constructor(private companyService: CompanyService) {}

  ngOnInit(): void {
    this.companyService.getCompanies().subscribe(data => {
      this.companies = data;
      console.log(data);
    });
  }

  showVacancies(company : Company) {
    this.selectedCompanyId = company.id;
    this.selectedCompanyName = company.name;
    this.companyService.getCompanyVacancies(this.selectedCompanyId).subscribe(data => {
      this.selectedVacancies = data;
    });
  }
}
