 var firebaseConfig = {
    apiKey: "AIzaSyCVmT0l828BSUpMkOumuiTaMcZ6ioI88nE",
    authDomain: "cs411collegeadvising.firebaseapp.com",
    databaseURL: "https://cs411collegeadvising.firebaseio.com",
    projectId: "cs411collegeadvising",
    storageBucket: "cs411collegeadvising.appspot.com",
    messagingSenderId: "795505184538",
    appId: "1:795505184538:web:940b94324a1410064a26a3",
    measurementId: "G-5XPWG51587"
 };

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();



//Sign up
firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
  // Handle Errors here.
  var errorCode = error.code;
  var errorMessage = error.message;
  // ...
});

document.getElementById("login_button").addEventListener("click", function(){
    var email = document.getElementById("login_email").innerText;
    console.log(email);
    var password = document.getElementById("login_password").innerText;
    console.log(password);
    //Sign in
    firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
    // Handle Errors here.
    var errorCode = error.code;
    var errorMessage = error.message;
});
});