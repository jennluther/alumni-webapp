$(function() {
  $('.delete_link').click(function(event){
    //don't do the normal behavior of the onclick event
    event.preventDefault();

    // show a popup
    $('#deleteModal').modal();

    //grab a href of popup and reset it's href to the right one
    var link = $(this).attr('href');
    console.log(link);

    $('#real_delete').attr('href', link);



  });//click
});
