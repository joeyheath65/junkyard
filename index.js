function ping() {
    // The custom URL
    var URL = $("http://192.168.0.1").val();
    var settings = {
      cache: false,
      dataType: "jsonp",
      async: true,
      crossDomain: true,
      url: URL,
      method: "GET",
    // For response
      statusCode: {
        200: function (response) {
          console.log(" is up!");
        },
        400: function (response) {
          console.log(" is down!");
        },
        0: function (response) {
          console.log(" is down!");
        },
      },
    };
    // Sends the request and observes the response
    $.ajax(settings).done(function (response) {
      console.log(response);
    });
  }