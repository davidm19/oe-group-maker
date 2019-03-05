describe('OE new trip function', function(){
    beforeEach(function(){
        browser.get('http://localhost:4200/');
    })

    var tripPage = element.all(by.buttonText("Trips"));
    var EC = protractor.ExpectedConditions;
    var tripAdder = element.all(by.css('i'));
    var tripCard = element.all(by.css('mat-card-content'))
    var tripName = element(by.css("input[class = 'mat-input-element mat-form-field-autofill-control cdk-text-field-autofill-monitored']"));
    var tripGrade = element(by.css("input[list = 'trip_grade']"));
    var saveTrip = element(by.css("button[class = 'mat-raised-button mat-primary']"));
    var deleteTrip = element.all(by.buttonText("Delete"));
    var addStudents = element(by.css("button[class = 'mat-raised-button mat-accent']"));
    var viewStudents = element(by.css("button[class = 'mat-raised-button mat-primary']"));
    var submitStudents = element(by.css("button[class = 'mat-raised-button mat-primary']"));


    it('should have a url', function(){
        browser.get('http://localhost:4200/');
        expect(browser.getCurrentUrl()).toBe('http://localhost:4200/');
    })
    it('should show new trips page', function(){
        tripPage.click();
        expect(browser.getCurrentUrl()).toBe('http://localhost:4200/trips');
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
        //     var numbah = tripCard.count();
        //     deleteTrip.click();
        //     expect(tripCard.count()).toBe(numbah - 1);
        // })
    //TODO: Add all students to a trip through checkboxes.
    it('should add students to a trip with checkboxes', function(){
        tripPage.click();
        addStudents.click();
        submitStudents.click();
        tripPage.click();
        viewStudents.click();
        expect(element.all(by.css('app-trip-detail')).getText()).toContain('Test Trip\nGrade: 7\nMichael Huang\nMia Dimson\nDavid Malone\nRyan Hom');

    })
    //TODO: Add some students to a trip through checkboxes.
    it('should add selected students to a trip through checkboxes', function(){
        tripPage.click();
        addStudents.click();
        element(by.css("input[ng-reflect-name='0']")).click();
        element(by.css("input[ng-reflect-name='2']")).click();
        submitStudents.click();
        tripPage.click();
        viewStudents.click();
        expect(element.all(by.css('app-trip-detail')).getText()).toContain('Test Trip\nGrade: 7\nMia Dimson\nRyan Hom');
    })
    //TODO: Return error when students checked are zero.
    it('should return an error when no students selected', function(){
        var EC = protractor.ExpectedConditions;
        tripPage.click();
        addStudents.click();
        element.all(by.css("input")).click();
        submitStudents.click();
        browser.wait(EC.alertIsPresent(), 5000);
    })
    //TODO: Assign grade to a trip.
    //TODO: 3 checkboxes need to be added before students can submit preferences.
});
