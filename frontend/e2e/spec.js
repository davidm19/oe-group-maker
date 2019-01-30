describe('OE new trip function', function(){
    beforeEach(function(){
        browser.get('localhost:4200/');
    })

    // var newTrip = element.all(by.css('mat-button-ripple mat-ripple mat-button-ripple-round'));
    // var EC = protractor.ExpectedConditions;
    // var tripName = element(by.css('mat-input-element mat-form-field-autofill-control cdk-text-field-autofill-monitored'));
    // var tripGrade = element(by.css('mat-form-field-infix'));


    it('should have a title', function(){
        browser.getCurrentUrl('localhost:4200/');
        expect(browser.getCurrentUrl()).toBe('localhost:4200/');
    })
    // it('should show new trip functions', function(){
    //     newTrip.click();
    //     broswer.wait(EC.urlContains('/trips/new'), 5000);
    //     // expect(EC.presenceOf('tripGrade'));
    // })
    // it('should add a new trip', function(){
    //     tripName.sendKeys('Test Trip');
    //     tripGrade.sendKeys('7');
    //     browser.wait(EC.urlContains('/trips'), 5000);
    //     expect(element.all(by.css('mat-elevation-z5 mat-card')).getText()).toContain('Test Trip');
    // })
});
