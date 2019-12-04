

$(document).ready(function() {

  $('#searchSchoolsBtn').on('click', function() {
    stateCode = $('#stateInput').val();
    $.get( "search=0&inoutstate=0&state=" + stateCode + "&tuition=0&enrollment=0&degree=0&gender=0", function( data ) {
      $( "#searchResults" ).html( data );
      console.log("loaded schools");
    });
  });

});

