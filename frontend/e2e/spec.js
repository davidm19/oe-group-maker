describe('OE new trip function', function(){
    beforeEach(function(){
        browser.get('http://localhost:4200/');
    })

    var tripPage = element.all(by.css('button'));
    var EC = protractor.ExpectedConditions;
    var tripAdder = element.all(by.css('i'));
    var tripCard = element.all(by.css('mat-card-content'))
    var tripName = element(by.css("input[class = 'mat-input-element mat-form-field-autofill-control cdk-text-field-autofill-monitored']"));
    var tripGrade = element(by.css("input[list = 'trip_grade']"));
    var saveTrip = element(by.css("button[class = 'mat-raised-button mat-primary']"));
    var deleteTrip = element.all(by.css("button[class = 'mat-button mat-warn']"));
    var addStudents = element(by.css("button[class = 'mat-raised-button mat-accent']"));
    // var numCards = tripCard.count();
    // var numCardsLess = numCards - 1;

    it('should have a title', function(){
        browser.get('http://localhost:4200/');
        expect(browser.getCurrentUrl()).toBe('http://localhost:4200/');
    })
    it('should show new trip functions', function(){
        tripPage.click();
        expect(browser.getCurrentUrl()).toBe('http://localhost:4200/trips');
        // expect(EC.presenceOf('tripGrade'));
    })
    it('should add a new trip', function(){
        tripPage.click();
        tripAdder.click();
        tripName.sendKeys('Test Trip');
        tripGrade.sendKeys('7');
        saveTrip.click();
        browser.wait(EC.urlContains('/trips'), 5000);
        expect(element.all(by.css('mat-card')).getText()).toContain('Test Trip\n7\nView Trip\nAdd Students\nDelete');
    })
    //TODO: Delete Trips (nonessential)
        // it('should delete a trip', function(){
        //     deleteTrip.click();
        //     expect(tripCard.count()).toBe(numCards - 1);
        // })
    //TODO: Add students to a trip through checkboxes.
    it('should add students to a trip with checkboxes', function(){
        tripPage.click();
        addStudents.click();
    })
    //TODO: 3 checkboxes need to be added before students can submit preferences.

});
