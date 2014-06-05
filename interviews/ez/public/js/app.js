'use strict';

// Declare app level module which depends on filters, and services

angular.module('myApp', [
    'ngRoute',
    'myApp.controllers'
]).config(function($routeProvider) {
    $routeProvider.
    // home page without login
    when('/question1', {
        templateUrl: 'partials/question1',
        controller: 'Question1'
    }).
    when('/question2', {
        templateUrl: 'partials/question2',
        controller: 'Question2'
    }).
    when('/question3', {
        templateUrl: 'partials/question3',
        controller: 'Question3'
    }).
    otherwise({
        redirectTo: '/question1'
    });
});
