
$( document ).ready(function() {  // Runs when the document is ready

  // // using jQuery
  // // https://docs.djangoproject.com/en/1.10/ref/csrf/
  // function getCookie(name) {
  //   var cookieValue = null;
  //   if (document.cookie && document.cookie !== '') {
  //       var cookies = document.cookie.split(';');
  //       for (var i = 0; i < cookies.length; i++) {
  //           var cookie = jQuery.trim(cookies[i]);
  //           // Does this cookie string begin with the name we want?
  //           if (cookie.substring(0, name.length + 1) === (name + '=')) {
  //               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
  //               break;
  //           }
  //       }
  //   }
  //   return cookieValue;
  // }

  // var csrftoken = getCookie('csrftoken');

  // function csrfSafeMethod(method) {
  //   // these HTTP methods do not require CSRF protection
  //   return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  // }

  // $.ajaxSetup({
  //     beforeSend: function(xhr, settings) {
  //         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
  //             xhr.setRequestHeader("X-CSRFToken", csrftoken);
  //         }
  //     }
  // });

  console.log("hi?");




 $('.create-comment-form').hide(); //Initially form wil be hidden.

    $("#add_comment_id").click(function(e) {

        $("#create-comment-form").show();
        e.preventDefault();
    });


$("#create-comment-form").on('submit', function(event) {
    event.preventDefault();

    $('#create-comment-form').hide(); //Initially form wil be hidden.

    console.log("??????? r u working")


    $.post("/grumblr-private/create-comment")
      .done(function(data) {
            console.log("??????? working")

          getUpdates();
      });

});

}); // End of $(document).ready
