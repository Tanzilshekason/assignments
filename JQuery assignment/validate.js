$(document).ready(function(){

    // Firstname validation
    $("#firstname-error").hide();
    let firstNameError = true;
    $("#firstname").keyup(function(){
        validateFirstName();    
    });
    function validateFirstName(){
        let firstNameValue = $("#firstname").val();

        if (firstNameValue.length == ''){
            $("#firstname-error").show();
            $('#firstname-error').html("**First name cannot be empty");
            $("#firstname-error").focus();
            firstNameError = false;   
            return false;
        }else {
            pattern_firstname=/^[a-zA-Z]+$/;
            if(!pattern_firstname.test(firstNameValue)){
                $("#firstname-error").show();
                $("#firstname-error").html("Firstname cannot be number");
                return false;
            }
            if(pattern_firstname.test(firstNameValue)){
                $("#firstname-error").show();
                $("#firstname-error").html("");
                return false;
            }

        }
        
        
    };


    // Lastname validation
    $("#lastname-error").hide();
    let lastNameError = true;
    $("#lastname").keyup(function(){
        validateLastName();    
    });

    function validateLastName(){
        let lastNameValue = $("#lastname").val();

        if (lastNameValue.length == ''){
            $("#lastname-error").show();
            $('#lastname-error').html("**Lastname cannot be empty");
            $("#lastname-error").focus();
            lastNameError = false;   
            return false;
        }else {
            pattern_lastname=/^[a-zA-Z]+$/;
            if(!pattern_lastname.test(lastNameValue)){
                $("#lastname-error").show();
                $("#lastname-error").html("lastname cannot be number");
                return false;
            }
            if(pattern_lastname.test(lastNameValue)){
                $("#lastname-error").show();
                $("#lastname-error").html("");
                return false;
            }

        }
    };


    // Phone number validation
    $("#phone-error").hide();
    let phoneNumberError = true;
    $("#phone").keyup(function(){
        validatePhoneNumber();    
    });

    function validatePhoneNumber(){
        let phoneNumberValue = $("#phone").val();

        if (phoneNumberValue.length == ''){
            $("#phone-error").show();
            $('#phone-error').html("**Number cannot be empty.");
            $("#phone-error").focus();
            phoneNumberError = false;   
            return false;

        }else if(phoneNumberValue.length != 10){
            $("#phone-error").show();
            $('#phone-error').html("**Enter valid phone number.");
            $("#phone-error").focus();
            phoneNumberError = false;   
            return false;

        }else if(isNaN(phoneNumberValue)){
            $("#phone-error").show();
            $('#phone-error').html("**Enter only number.");
            $("#phone-error").focus();
            phoneNumberError = false;   
            return false;

        }else{
            $("#phone-error").hide();
        };
    };


    // Office Phone number validation
    $("#phone-number-office-error").hide();
    let officePhoneNumberError = true;
    $("#phone-number-office").keyup(function(){
        validateOfficePhoneNumber();    
    });

    function validateOfficePhoneNumber(){
        let officePhoneNumberValue = $("#phone-number-office").val();
        var regNumber = /^[0-9]{0,10}$/
        if((isNaN(officePhoneNumberValue)) || (!regNumber.test(officePhoneNumberValue))){
            $("#phone-number-office-error").show();
            $('#phone-number-office-error').html("**Enter only numbers");
            $("#phone-number-office-error").focus();
            officePhoneNumberError = false;   
            return false;

        }else if(officePhoneNumberValue.length == null){
            $("#phone-number-office-error").hide();
        }else{
            $("#sphone-number-office-error").hide();
        };
    };


    // Email Validation
    $("#email-error").hide();
    let emailError = true;
    $("#email").keyup(function(){
        validateEmail();    
    });

    function validateEmail(){
        let emailValue = $("#email").val();
        let regEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

        if (emailValue.length == ''){
            $("#email-error").show();
            $('#email-error').html("**Email cannot be blank");
            $("#email-error").focus();
            emailError = false;   
            return false;

        }else if(!(regEmail.test(emailValue))){
            $("#email-error").show();
            $('#email-error').html("**Email is not valid");
            $("#email-error").focus();
            emailError = false;   
            return false;

        }else{
            $("#email-error").hide();
        }
    };


    // Password validation
    $("#password-error").hide();
    let passwordError = true;
    $("#password").keyup(function(){
        validatePassword();    
    });

    function validatePassword(){
        var passwordValue = $("#password").val();
        let regPassword = /^\w{8,12}$/;

        if (passwordValue.length == ''){
            $("#password-error").show();
            $('#password-error').html("**Password cannot be blank");
            $("#password-error").focus();
            passwordError = false;   
            return false;

        }else if(!(regPassword.test(passwordValue))){
            $("#password-error").show();
            $('#password-error').html("**Password is not valid");
            $("#password-error").focus();
            passwordError = false;   
            return false;

        }else{
            $("#password-error").hide();
        }
    };


    // Confirm Password validation
    $("#confirm-password-error").hide();
    let confirmPasswordError = true;
    $("#confirm-password").keyup(function(){
        validateConfirmPassword();    
    });


    function validateConfirmPassword(){
        let confirmPasswordValue = $("#confirm-password").val();
        var passwordValue = $("#password").val();

        if (confirmPasswordValue != passwordValue){
            $("#confirm-password-error").show();
            $('#confirm-password-error').html("**Passwords do not match.");
            $("#confirm-password-error").focus();
            confirmPasswordError = false;   
            return false;

        }else{
            $("#confirm-password-error").hide();
        }
    };


    // Month Validation
    $("#date-error").hide();
    var dateError = true;
    $("#birth-month").click(function(){
        validateMonth();    
    });

    function validateMonth(){
        var birthMonthValue = $("#birth-month").val();

        if (birthMonthValue  == 'month'){
            $("#date-error").show();
            $('#date-error').html("**Please select proper date format.");
            $("#date-error").focus();
            dateError = false;   
            return false;
        }else{
            $("#date-error").hide();
        }
    };


    // Day Validation
    $("#date-error").hide();
    var dateError = true;
    $("#birth-day").click(function(){
        validateDay();    
    });

    function validateDay(){
        var birthDayValue = $("#birth-day").val();

        if (birthDayValue  == 'day'){
            $("#date-error").show();
            $('#date-error').html("**Please select proper date format.");
            $("#date-error").focus();
            dateError = false;   
            return false;
        }else{
            $("#date-error").hide();
        }
    };


    // Year Validation
    $("#date-error").hide();
    var dateError = true;
    $("#birth-year").click(function(){
        validateYear();    
    });

    function validateYear(){
        var birthYearValue = $("#birth-year").val();

        if (birthYearValue  == 'year'){
            $("#date-error").show();
            $('#date-error').html("**Please select proper date format.");
            $("#date-error").focus();
            dateError = false;   
            return false;
        }else{
            $("#date-error").hide();
        }
    };

    // Gender Validation
    $("#gender-error").hide();
    let genderError = true;
    $("#btn-submit").click(function(){
        validateGender();    
    });

    function validateGender(){
        var genderValue = $("input[name = 'rdb-gender']:checked").val();

        if (genderValue == null){
            $("#gender-error").show();
            $('#gender-error').html("**Select your gender.");
            genderError = false;   
            return false;

        }else{
            $("#gender-error").hide();
        }
    };
    

    // Interest Validation
    $("#interest-error").hide();
    let interestError = true;
    $("#btn-submit").click(function(){
        validateInterest();    
    });

    function validateInterest(){
        var interestValue = $("input[name = 'chkbx-activity']:checked").val();

        if (interestValue == null){
            $("#interest-error").show();
            $('#interest-error').html("**Select atleast 1 activity.");
            interestError = false;   
            return false;

        }else{
            $("#interest-error").hide();
        }
    };


    // About us Validation
    $("#about-error").hide();
    let aboutYouError = true;
    $("#about").keyup(function(){
        validateAboutYou();    
    });

    function validateAboutYou(){
        let aboutYouValue = $("#about").val();

        if (aboutYouValue.length == ''){
            $("#about-error").show();
            $("#about-error").html("**Enter some text. ");
            $("#about-error").focus();
            aboutYouError = false;   
            return false;
        }else{
            $("#about-error").hide();
        };
    };


   // Submit button
   $('#btn-submit').click(function(){
    firstNameError == true;
    lastNameError == true;
    phoneNumberError = true;
    officePhoneNumberError = true;
    emailError = true;
    passwordError = true;
    confirmPasswordError = true;
    genderError = true;
    interestError = true;
    aboutYouError = true;
    dateError = true;

    validateFirstName();
    validateLastName();
    validatePhoneNumber();
    validateOfficePhoneNumber();
    validateEmail();
    validatePassword();
    validateConfirmPassword();
    validateGender();
    validateMonth();
    validateDay();
    validateYear();
    validateInterest();
    validateAboutYou();
    
    if((firstNameError == true) && (lastNameError == true) 
        && (phoneNumberError = true) && (officePhoneNumberError = true) 
        && (emailError = true) && ( passwordError = true) 
        && (confirmPasswordError = true) && (dateError = true)
        && (genderError = true) && (interestError = true) 
        && (aboutYouError = true)){
            return true;    
    }else{
        return false;
    }
    
});
});





window.onload = function () {
    var years = document.getElementById("birth-year");
    var currentYear = (new Date()).getFullYear();
    for (var year = 1998; year <= currentYear; year++) {
        var option = document.createElement("option");
        option.innerHTML = year;
        option.value = year;
        years.appendChild(option);
    }
};

// Age validation
function calculateAge(){
    let day= document.getElementById("birth-day").value;
    let month= document.getElementById("birth-month").value;
    let year= document.getElementById("birth-year").value;
        
    document.getElementById("day-29").style.display = "block";
    document.getElementById("day-30").style.display = "block";
    document.getElementById("day-31").style.display = "block";
    
    var monthsWith30Days = ["4", "6", "9", "11"];
    if(monthsWith30Days.includes(month)){
        document.getElementById("day-31").style.display = "none";
    };

    if(month == "2" && (year % 4 == 0)){
        // if(year % 4 == 0){
            document.getElementById("day-30").style.display = "none";
            document.getElementById("day-31").style.display = "none";
    }else if(month == "2" && (year % 4 != 0)){
            document.getElementById("day-29").style.display = "none";
            document.getElementById("day-30").style.display = "none";
            document.getElementById("day-31").style.display = "none";
    };

    

    if( day != "day" && month != "month" && year != "year" ){
        var stringDate = month + "/" + day + "/" + year 
        var timestamp = Date.parse(stringDate);
        var dateObject = new Date(timestamp);

        var currentYear = new Date().getFullYear();
        var birthYear = dateObject.getFullYear();
        var age = currentYear - birthYear;
        document.getElementById("age").value = age;
    }
};

// Submit message for the page
var count = 1;

function showMessage() {
  if (!(count++ % 3))
    alert("The page is submitted"); 
}

