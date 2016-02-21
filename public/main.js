var ref = new Firebase("https://flickering-torch-8936.firebaseio.com/")
var app = angular.module("myApp", ["firebase"]);

app.controller("MainController", function ($scope, $firebaseAuth, $firebaseArray, $firebaseObject) {
  $scope.process = function() {
  	$scope.limit = 5

    ref.push({"go": true})
    $scope.suggestionsText = "Based on your purchasing history, and past stock performance, we recommend the following stocks:"

    $scope.list = $firebaseArray(ref.child("recommendations"))

    // $scope.suggestions = ref.get("recommendations")
  }
})



// $scope.authObj = $firebaseAuth(ref);

//   $scope.authObj.$onAuth(function(authData) {
//     if (authData) {
//       console.log("Logged in as:", authData.uid);
//       $scope.user = authData;
//       ref.child("users").child($scope.user.uid).set(authData.twitter.cachedUserProfile)
//       $scope.votedForMe = $firebaseObject(ref.child("votes").child($scope.user.uid))

//       $scope.votedForMe.$watch(function (votes) {
//         console.log("latest votes", $scope.votedForMe)
//         angular.forEach($scope.votedForMe, function (vote, id) {
//           console.log(vote)

//           $scope.matchedVotes[id] = $firebaseObject(ref.child("votes").child(id).child($scope.user.uid))
//         })
//       })
//     } else {
//       console.log("Logged out");
//       $scope.user = {};
//     }
//   });
//   $scope.matchedVotes = {};
//   $scope.user = {}
//   $scope.users = $firebaseArray(ref.child("users"))

//   $scope.login = function () {
//     $scope.authObj.$authWithOAuthPopup("twitter");
//   }

//   $scope.isGood = function (user) {
//     console.log("I like", user)
//     ref.child("votes").child(user.$id).child($scope.user.uid).set(true)
//   }

//   $scope.needsImprovement = function (user) {
//     console.log("nah bro nah", user)
//     ref.child("votes").child(user.$id).child($scope.user.uid).set(false)
//   }