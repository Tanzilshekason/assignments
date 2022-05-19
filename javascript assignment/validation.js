

function validation() {

    validationFlag = true;
    
    // for first name validation
    var firstName = document.getElementById("firstname").value;
    if(firstName == ""){
        document.getElementById("firstname-error").style.display = "block";
        document.getElementById("firstname-error").innerHTML = "**Enter your first name";
        validationFlag = false;

    }
    else {
        pattern_firstname=/^[a-zA-Z]+$/;
        if(!pattern_firstname.test(firstName)){
            document.getElementById("firstname-error").style.display = "block";
            document.getElementById("firstname-error").innerHTML = "firstname cannot be numbers";
            validationFlag = false;
        }
        if(pattern_firstname.test(firstName)){
            document.getElementById("firstname-error").style.display = "none";
            document.getElementById("firstname-error").innerHTML = "";
            validationFlag = false;
        }

    }


    // for last name validation
    var lastname = document.getElementById("lastname").value;
    if (lastname == ""){
        document.getElementById("lastname-error").style.display = "block";
        document.getElementById("lastname-error").innerHTML = "**Enter your last name";
        validationFlag = false;

    }
    else {
        pattern_lastname=/^[a-zA-Z]+$/;
        if(!pattern_lastname.test(lastname)){
            document.getElementById("lastname-error").style.display = "block";
            document.getElementById("lastname-error").innerHTML = "lastname cannot be numbers";
            validationFlag = false;
        }
        if(pattern_lastname.test(lastname)){
            document.getElementById("lastname-error").style.display = "none";
            document.getElementById("lastname-error").innerHTML = "";
            validationFlag = false;
        }

    }

    // for phone number validation
    var phone = document.getElementById("phone").value;
    if (phone == ""){
        document.getElementById("phone-error").style.display = "block";
        document.getElementById("phone-error").innerHTML = " **Number cannot be blank ";
        validationFlag = false;

    }else if(phone.length != 10){
        document.getElementById("phone-error").style.display = "block";
        document.getElementById("phone-error").innerHTML = "**Enter valid phone number";
        validationFlag = false;

    }else if (isNaN(phone)) {
        document.getElementById("phone-error").style.display = "block";
        document.getElementById("phone-error").innerHTML = "**Enter only number";
        validationFlag = false;

    }else{
        document.getElementById("phone-error").style.display = "none";
        document.getElementById("phone-error").innerHTML = "";
    }

    
    var phoneNumberOffice = document.getElementById("phone-number-office").value;
    // office number (only number no other char) validation;
    if (isNaN(phoneNumberOffice)) {
        document.getElementById("phone-number-office-error").style.display= "block";
        document.getElementById("phone-number-office-error").innerHTML= "**Enter only number";
        validationFlag = false;

    }else{
        document.getElementById("phone-number-office-error").style.display= "none";
        document.getElementById("phone-number-office-error").innerHTML= "";
    }
    
    var email = document.getElementById("email").value;
    // email id (empty or not) validation
    if (email == ""){
        document.getElementById("email-error").style.display= "block";
        document.getElementById("email-error").innerHTML= "**Email cannot be blank";
        validationFlag = false;

    }else{
        document.getElementById("email-error").style.display= "none";
        document.getElementById("email-error").innerHTML= "";
    }
    var regEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (!regEmail.test(email)){
        document.getElementById("email-error").style.display= "block";
        document.getElementById("email-error").innerHTML= "**Email is not valid";
        validationFlag = false;

    }else{
        document.getElementById("email-error").style.display= "none";
        document.getElementById("email-error").innerHTML= "";
    }
    
    
    var password = document.getElementById("password").value;
    // password validation
    if (password == "") {
        document.getElementById("password-error").innerHTML= "**password cannot be blank";
        validationFlag = false;

    }else{
        document.getElementById("password-error").style.display= "none";
        document.getElementById("password-error").innerHTML= "";
    }

    // alphanumeric validation;
    var regPassword = /^\w{8,12}$/;
    if (!regPassword.test(password)){
        document.getElementById("password-error").style.display= "block";
        document.getElementById("password-error").innerHTML= "**Password should be between 8-12 characters";
        validationFlag = false;

    }else{
        document.getElementById("password-error").style.display= "none";
        document.getElementById("password-error").innerHTML= "";
    }

    var confirmPassword = document.getElementById("confirm-password").value;
    // match password
    if (confirmPassword != password ) {
        document.getElementById("confirm-password-error").style.display= "block";
        document.getElementById("confirm-password-error").innerHTML= "**password don't match";
        validationFlag = false;

    }else{
        document.getElementById("confirm-password-error").style.display= "none";
        document.getElementById("confirm-password-error").innerHTML= "";
    }

    // DOB validation
    var  day= document.getElementById("birth-day").value;
    var  month= document.getElementById("birth-month").value;
    var   year= document.getElementById("birth-year").value;

    if (day == "day"){
        document.getElementById("date-error").style.display= "block";
        document.getElementById("date-error").innerHTML= "**Select proper date format";
        validationFlag = false;

    }else if (month == "month"){
        document.getElementById("date-error").style.display= "block";
        document.getElementById("date-error").innerHTML= "**Select proper date format";
        validationFlag = false;

    }else if(year == "year" ){
        document.getElementById("date-error").style.display= "block";
        document.getElementById("date-error").innerHTML= "*Select proper date format";
        validationFlag = false;
    }else{
        document.getElementById("date-error").style.display= "none";
        document.getElementById("date-error").innerHTML= "";
    }

    // gender validation
    gender = document.getElementsByName("rdb-gender");
    if (!(gender[0].checked || gender[1].checked)) {
        document.getElementById("gender-error").style.display = "block";
        document.getElementById("gender-error").innerHTML = "**Select atleast 1 value";
        validationFlag = false;

    }else{
        document.getElementById("gender-error").style.display = "none";
        document.getElementById("gender-error").innerHTML = "";

    }
    
    // interest validation
    var checkboxActivity = document.querySelectorAll('input[name="chkbx-activity"]:checked').length;
    if (checkboxActivity < 1){
        document.getElementById("interest-error").style.display = "block";
        document.getElementById("interest-error").innerHTML = "**select atleast 1 value";
        validationFlag = false;

    }else{
        document.getElementById("interest-error").style.display = "none";
        document.getElementById("interest-error").innerHTML = "";
    }

    // textbox validation
    var text = document.getElementById("about").value;
    if (text == "" ){
        document.getElementById("about-error").style.display = "block";
        document.getElementById("about-error").innerHTML = " **Enter the text ";
        validationFlag = false;

    }else{
        document.getElementById("about-error").style.display = "none";
        document.getElementById("about-error").innerHTML = "";
    }
    return validationFlag;  
};


window.onload = function(){
    var years = document.getElementById("birth-year");

    var currentYear = (new Date()).getFullYear();

    for (var year = 1998; year <= currentYear; year++) {
        var option = document.createElement("option");
        option.innerHTML = year;
        option.value = year;
        years.appendChild(option);
    }
};


function calculateAge(){

    let  day= document.getElementById("birth-day").value;
    let  month= document.getElementById("birth-month").value;
    let  year= document.getElementById("birth-year").value;
    
    document.getElementById("day-29").style.display = "block";
    document.getElementById("day-30").style.display = "block";
    document.getElementById("day-31").style.display = "block";
    if(month == "4"){
        document.getElementById("day-31").style.display = "none";
    };
    if(month == "6" ){
        document.getElementById("day-31").style.display = "none";
    };
    if(month == "9" ){
        document.getElementById("day-31").style.display = "none";
    };
    if(month == "11"){
        document.getElementById("day-31").style.display = "none";
    };

    if(month == "2" && (year % 4 == 0)){
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
