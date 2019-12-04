

$(document).ready(function() {
  
  $('#searchSchoolsBtn').on('click', function() {
    

    var url = "search=0";

    inOutState = $('#inOutInput').val();
    url += "&inoutstate=" + inOutState;

    stateCode = $('#stateInput').val();
    url += "&state=" + stateCode;

    tuitionCode = $('#tuitionInput').val();
    url += "&tuition=" + tuitionCode;

    enrollmentCode = $('#sizeInput').val();
    url += "&enrollment=" + enrollmentCode;

    degreeCode = $('#degreeInput').val();
    url += "&degree=" + degreeCode;

    genderCode = $('#genderInput').val();
    url += "&gender=" + genderCode;

    $.get( url, function( data ) {
      $( "#searchResults" ).html( data );
      console.log("loaded schools");
    });
  });

});

