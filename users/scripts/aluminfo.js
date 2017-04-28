$(function() {
  $('.delete_internship').click(function(event){
    //don't do the normal behavior of the onclick event
    event.preventDefault();

    // show a popup
    $('#deleteInternship').modal();

    //grab a href of popup and reset it's href to the right one
    var link = $(this).attr('href');
    console.log(link);

    $('#real_delete').attr('href', link);



  });//click

  $('.delete_job').click(function(event){
    //don't do the normal behavior of the onclick event
    event.preventDefault();

    // show a popup
    $('#deleteJob').modal();

    //grab a href of popup and reset it's href to the right one
    var link = $(this).attr('href');
    console.log(link);

    $('#real_delete').attr('href', link);



  });//click

  $('.delete_offer').click(function(event){
    //don't do the normal behavior of the onclick event
    event.preventDefault();

    // show a popup
    $('#deleteOffer').modal();

    //grab a href of popup and reset it's href to the right one
    var link = $(this).attr('href');
    console.log(link);

    $('#real_delete').attr('href', link);



  });//click
});
