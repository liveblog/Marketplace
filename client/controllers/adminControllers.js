
angular.module("marketPlaceAdmin")
    .constant("authUrl", "http://localhost:5500/users/login")
    .controller("authCtrl", function($scope, $http, $location, authUrl) {

        $scope.authenticate = function (user, pass) {
            //$location.path("/main");
            $http.post(authUrl, {
            }, {
                withCredentials: true
            }).success(function (data) {
                $location.path("/main");
            }).error(function (error) {
                $scope.authenticationError = error;
            });
        }
    });