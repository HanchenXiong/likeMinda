var app = angular.module('SemanticSearchApp', []);


app.controller('SemanticSearchController', ['$scope', '$log', '$http',
    function($scope, $log, $http, userTextInput) {
        // Controller variables
        $scope.userTextInput = userTextInput;
 
        /**
            this function queries the endpoint /api/search/
            to get a list of tweets retrieved with the user input
            gets a json response as a result
        **/   
        $scope.searchAndRefresh = function() {
            // create a dictionary for the requests parameters
            var url = "http://localhost:2222/api/search";

            // fire the API request
            $http({
                method: "GET",
                url: url,
                //data: {"sentence": $scope.userTextInput}
            }).then(function successCallback(response) {
                // this callback will be called asynchronously
                // when the response is available
                $log.log(response);
                $scope.tweetIDs = response.data;
            }, function errorCallback(error) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
                $log.log(error);
            });
        }

        $scope.setValue = function(value) {
            $scope.userTextInput = value;
        }
    }
]);
