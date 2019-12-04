

$(document).ready(function() {
  
  $('#searchSchools').on('click', function() {
    var url = "search=0";

    var inOutState = $('#inOutInput').val();
    url += "&inoutstate=" + inOutState;

    var stateCode = $('#stateInput').val();
    url += "&state=" + stateCode;

    var tuitionCode = $('#tuitionInput').val();
    url += "&tuition=" + tuitionCode;

    var enrollmentCode = $('#sizeInput').val();
    url += "&enrollment=" + enrollmentCode;

    var degreeCode = $('#degreeInput').val();
    url += "&degree=" + degreeCode;

    var genderCode = $('#genderInput').val();
    url += "&gender=" + genderCode;

    $.get( url, function( data ) {
      $( "#searchResults" ).html( data );
      console.log("loaded schools");
    });
  });

  $('#searchSafety').on('click', function() {
    var url = "search=1";

    var inOutState = $('#inOutInput').val();
    url += "&inoutstate=" + inOutState;

    var stateCode = $('#stateInput').val();
    url += "&state=" + stateCode;

    var tuitionCode = $('#tuitionInput').val();
    url += "&tuition=" + tuitionCode;

    var enrollmentCode = $('#sizeInput').val();
    url += "&enrollment=" + enrollmentCode;

    var degreeCode = $('#degreeInput').val();
    url += "&degree=" + degreeCode;

    var genderCode = $('#genderInput').val();
    url += "&gender=" + genderCode;

    $.get( url, function( data ) {
      $( "#searchResults" ).html( data );
      console.log("loaded schools");
    });
  });

  $('#searchMatch').on('click', function() {
    var url = "search=2";

    var inOutState = $('#inOutInput').val();
    url += "&inoutstate=" + inOutState;

    var stateCode = $('#stateInput').val();
    url += "&state=" + stateCode;

    var tuitionCode = $('#tuitionInput').val();
    url += "&tuition=" + tuitionCode;

    var enrollmentCode = $('#sizeInput').val();
    url += "&enrollment=" + enrollmentCode;

    var degreeCode = $('#degreeInput').val();
    url += "&degree=" + degreeCode;

    var genderCode = $('#genderInput').val();
    url += "&gender=" + genderCode;

    $.get( url, function( data ) {
      $( "#searchResults" ).html( data );
      console.log("loaded schools");
    });
  });

  $('#searchReach').on('click', function() {
    var url = "search=3";

    var inOutState = $('#inOutInput').val();
    url += "&inoutstate=" + inOutState;

    var stateCode = $('#stateInput').val();
    url += "&state=" + stateCode;

    var tuitionCode = $('#tuitionInput').val();
    url += "&tuition=" + tuitionCode;

    var enrollmentCode = $('#sizeInput').val();
    url += "&enrollment=" + enrollmentCode;

    var degreeCode = $('#degreeInput').val();
    url += "&degree=" + degreeCode;

    var genderCode = $('#genderInput').val();
    url += "&gender=" + genderCode;

    $.get( url, function( data ) {
      $( "#searchResults" ).html( data );
      console.log("loaded schools");
    });
  });

});

