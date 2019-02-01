describe('OE new trip function', function(){
    beforeEach(function(){
        browser.get('http://localhost:4200/');
    })

    var newTrip = element.all(by.css('button'));
    var EC = protractor.ExpectedConditions;
    var tripAdder = element.all(by.css('i'));
    var tripName = element.all(by.css('input'));
    var tripGrade = element(by.css('input'));
    var saveTrip = element(by.css('button')).filter(function());

    it('should have a title', function(){
        browser.get('http://localhost:4200/');
        expect(browser.getCurrentUrl()).toBe('http://localhost:4200/');
    })
    it('should show new trip functions', function(){
        newTrip.click();
        expect(browser.getCurrentUrl()).toBe('http://localhost:4200/trips');
        // expect(EC.presenceOf('tripGrade'));
    })
    it('should add a new trip', function(){
        newTrip.click();
        tripAdder.click();
        tripName.sendKeys('Test Trip');
        tripGrade.sendKeys('7');
        saveTrip.click();
        browser.wait(EC.urlContains('/trips'), 5000);
        expect(element.all(by.css('mat-card')).getText()).toContain('Test Trip');
    })
});
