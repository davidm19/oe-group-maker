import { TripsModule } from './trips.module';

describe('TripsModule', () => {
  let tripsModule: TripsModule;

  beforeEach(() => {
    tripsModule = new TripsModule();
  });

  it('should create an instance', () => {
    expect(tripsModule)
    .toBeTruthy();
  });
});
