desecribe('OE new trip function', function(){
var newTrip = element(by.class($('btn new')));
var EC = protractor.ExpectedConditions;
var tripName = element(by.class('mat-input-element mat-form-field-autofill-control cdk-text-field-autofill-monitored'))
var tripGrade = element(by.class('mat-form-field-infix'))
beforeEach(function(){
    browser.get('localhost:4200/');
})

it('should have a title', function(){
    expect(browser.getTitle().isPresent()).toBe(true);
})
it('should show new trip functions', function(){
    newTrip.click();
    expect(EC.presenceOf('tripName'));
    expect(EC.presenceOf('tripGrade'));
})
it('should fail', function(){
    tripName.sendKeys('Test Trip');
    tripGrade.sendKeys('7');
    expect(EC.alertIsPresent(), 5000);
})
});
