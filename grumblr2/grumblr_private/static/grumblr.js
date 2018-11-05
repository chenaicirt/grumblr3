



$( document ).ready(function() {  // Runs when the document is ready
  var newpost = false; 

  // using jQuery
  // https://docs.djangoproject.com/en/1.10/ref/csrf/
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }


  setInterval(function() {

    var url = "/grumblr-private/check-new-post";

    $.ajax({
           url: url,
           success: function(data) {
             $(newPosts).append(data  );
           }
    });

  }, 5000);




  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });


 $(".triggerSubmission").on("click", function(){
    var textareaList = document.getElementsByTagName('textarea')
    text = ""; 
    for(var i = 0; i < textareaList.length; i++){
       if (textareaList[i].id) {
        if (textareaList[i].value) {
        var urlToSend = 'post/comment/' + textareaList[i].id;
                // do ajax things

         $.ajax({
           url: urlToSend,
           data: { 'text': textareaList[i].value },
           type: 'post',
           cache: false,
           success: function (data) {
            var postid = (data['post_id']);
            // var postid = obj[0]['fields']['post']; 
            var commentSelector = "#allComments" + postid;

            var additionalComment=" <div class='date'>" + data['created_date']+ "</div> <strong>" + data['author'] + "</strong> <p> " + data['text']+ "</p>";

            $(commentSelector).append(additionalComment  );

           }
        });


        }
       }
    }

   }); 




}); // End of $(document).ready
