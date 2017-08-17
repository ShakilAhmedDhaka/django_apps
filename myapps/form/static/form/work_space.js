$(document).ready(function () {

//alert('just checking');


window.fbAsyncInit = function() {
	alert('fbAsyncInit');
    FB.init({
      appId            : '657378241131010',
      autoLogAppEvents : true,
      xfbml            : true,
      version          : 'v2.10'
    });
    FB.AppEvents.logPageView();
    
	FB.getLoginStatus(function(response) {
	  if (response.status === 'connected') {
	  	console.log('connected');
	    // the user is logged in and has authenticated your
	    // app, and response.authResponse supplies
	    // the user's ID, a valid access token, a signed
	    // request, and the time the access token 
	    // and signed request each expire
	    var uid = response.authResponse.userID;
	    var accessToken = response.authResponse.accessToken;
	    //console.log(accessToken);


	    // for accessing a facebook page and collecting posts details
	 //    FB.api(
		//   '/fcbarcelona',
		//   'GET',
		//   {"fields":"posts{created_time,message,comments}"},
		//   function(response) {
		//       console.log(response.posts.data[0]['created_time']);
		//   }
		// );


		//for user information
		FB.api(
		  '/me/',
		  'GET',
		  {"fields":"birthday"},
		  function(response) {
		      console.log(response.birthday);
		      var str = $('#birthdate').text();
		      $('#birthdate').html(str + response.birthday);
		  }
		);

	  } else if (response.status === 'not_authorized') {
	  	console.log('not authorized');
	    // the user is logged in to Facebook, 
	    // but has not authenticated your app
	  } else {
	  	console.log('not logged');
	    // the user isn't logged in to Facebook.
	  }
	 });

  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "//connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));



});