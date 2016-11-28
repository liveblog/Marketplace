
angular.module("marketPlace", [])
    .constant("producersUrl", "http://localhost:5000/producers")
    .controller("marketPlaceCtrl", function($scope, $http, producersUrl) {

        $scope.data = {};

        $http.get(producersUrl)
            .success(function (data) {
            $scope.data.producers = data._items;
        })
        .error(function (error) {
            $scope.data.error = error;
        });
    });