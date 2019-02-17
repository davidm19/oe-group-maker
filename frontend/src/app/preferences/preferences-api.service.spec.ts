import { TestBed } from '@angular/core/testing';

import { PreferencesApiService } from './preferences-api.service';

describe('PreferencesApiService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: PreferencesApiService = TestBed.get(PreferencesApiService);
    expect(service).toBeTruthy();
  });
});
