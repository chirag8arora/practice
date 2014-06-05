'use strict';

// Declare app level module which depends on filters, and services

angular.module('myApp', [
    'ngRoute',
    'myApp.controllers'
]).config(function($routeProvider) {
    $routeProvider.
    // home page without login
    when('/', {
        templateUrl: 'partials/home',
        controller: 'HomeCtrl'
    }).
    otherwise({
        redirectTo: '/'
    });
});
