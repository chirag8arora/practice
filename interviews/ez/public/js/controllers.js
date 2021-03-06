'use strict';
var controllers = angular.module('myApp.controllers', []);
controllers.controller('Question1', function($scope, $http) {
    // d3 variables
    var margin = {
            top: 80,
            right: 40,
            bottom: 20,
            left: 40
        },
        width = $('.q1').width() - margin.left - margin.right,
        height = 300;

    // create a svg for bar chart
    var svg = d3.select('.q1').append('svg')
        .attr('width', width + margin.left + margin.right)
        .attr('height', height + margin.top + margin.bottom)
        .append('g')
        .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

    // transform 0-27 to a-z and ?
    function intToChar(i) {
        if (i == 26) return '?';
        return String.fromCharCode(97 + i);
    }

    // to get the container's width for responsive chart
    $scope.getElementDimensions = function() {
        return $('.q1').width();
    };

    // bind resize with bar chart re-render
    // so resize the browser, the char will re-render and fit in
    $scope.$watch($scope.getElementDimensions, function(newValue) {
        d3.select('.q1 svg').attr('width', newValue);
        $scope.render();
    }, true);
    $(window).bind('resize', function() {
        $scope.$apply();
    });

    // render the bar chart using d3, basicly creates rectangles
    $scope.render = function() {
        // init dataset and remove previous items before render
        var dataset = $scope.dataset;
        svg.selectAll('*').remove();
        // responsive width
        var width = $('.q1').width() - margin.left - margin.right;
        // edge case
        if (!dataset) return;

        // setup x, y ranges, a-z and 0 to max(dataset)
        var x = d3.scale.ordinal()
            .rangeRoundBands([0, width], 0.1)
            .domain(dataset.map(function(d, i) {
                return intToChar(i);
            }));
        var y = d3.scale.linear()
            .range([height, 0])
            .domain([0, d3.max(dataset, function(d) {
                return d;
            }) + 2]);

        // setup xAxis and yAxis
        var xAxis = d3.svg.axis()
            .scale(x)
            .orient('bottom');
        var yAxis = d3.svg.axis()
            .scale(y)
            .orient('left');


        // add title and helpinfo to svg
        svg.append('text')
            .attr('x', (width / 2))
            .attr('y', 0 - (margin.top / 2))
            .attr('text-anchor', 'middle')
            .style('font-size', '24px')
            .text('Static of ' + $scope.userSearchKey);
        svg.append('text')
            .attr('x', (width / 2))
            .attr('y', 0 - (margin.top / 4))
            .attr('text-anchor', 'middle')
            .text('Mouse on bars to see details');

        // add x y axis to svg
        svg.append('g')
            .attr('class', 'x axis')
            .attr('transform', 'translate(0,' + height + ')')
            .call(xAxis);
        svg.append('g')
            .attr('class', 'y axis')
            .call(yAxis)
            .append('text')
            .attr('transform', 'rotate(-90)')
            .attr('y', 6)
            .attr('dy', '.71em')
            .style('text-anchor', 'end')
            .text('Count');

        //add the rectangles
        svg.selectAll('.bar')
            .data(dataset)
            .enter()
            .append('rect')
            .attr('class', 'bar')
            .attr('x', function(d, i) {
                return x(intToChar(i));
            })
            .attr('y', function(d) {
                return y(d);
            })
            .attr('width', x.rangeBand())
            .attr('height', function(d) {
                return height - y(d);
            })
            .append('title')
            .text(function(d, i) {
                // here is the tooltip, using title attr of .bar
                return intToChar(i) + ' occurs: ' + d + ' times';
            });
    };
    $scope.search = function(userSearchKey) {
        // set default
        $scope.userSearchKey = userSearchKey || 'barack';
        // show loading
        $('.spinner').show();
        // call the api, using jsonp, JSON_CALLBACK the default callback
        var url = 'https://api.angel.co/1/search?query=' + $scope.userSearchKey + '&type=User&callback=JSON_CALLBACK';
        $http({
            method: 'JSONP',
            url: url
        }).success(function(data) {
            // init an int[27] to count characters
            var dataset = Array.apply(null, new Array(27)).map(Number.prototype.valueOf, 0);
            data.slice(0, Math.min(data.length, 5)).forEach(function(user) {
                // slice [0:5] to do the statistic
                for (var i = 0; i < user.name.length; i++) {
                    // for loop each name
                    var charCode = user.name.charCodeAt(i);
                    if (charCode <= 122 && charCode >= 97) {
                        // a-z
                        dataset[charCode - 97] += 1;
                    } else if (charCode <= 90 && charCode >= 65) {
                        // A-Z
                        dataset[charCode - 65] += 1;
                    } else {
                        // Others
                        dataset[26] += 1;
                    }
                }
            });
            // call the render function
            $scope.dataset = dataset;
            $scope.render();
            // hide the loading animation
            $('.spinner').hide();
        }).error(function() {
            // hide the loading animation
            $('.spinner').hide();
        });
    };
}).controller('Question2', function($scope) {
    $scope.get_missing_letters = function(sentence) {
        // set a default
        sentence = sentence || '';
        $scope.missing = '';

        // an int[26] to count characters
        var dataset = Array.apply(null, new Array(26)).map(Number.prototype.valueOf, 0);
        for (var i = 0; i < sentence.length; i++) {
            var charCode = sentence.charCodeAt(i);
            if (charCode <= 122 && charCode >= 97) { // a-z
                dataset[charCode - 97] += 1;
            } else if (charCode <= 90 && charCode >= 65) { // A-Z
                dataset[charCode - 65] += 1;
            }
        }
        // iterate int[26] array, 0 means missing char
        dataset.forEach(function(d, i) {
            if (d === 0) {
                // add this to missing buffer
                // here use an array, then join should be better
                $scope.missing += String.fromCharCode(97 + i);
            }
        });
    };
}).controller('Question3', function($scope) {
    $scope.result = [];
    $scope.errs = [];
    $scope.go = function(step, initial) {
        // clear previous errs and result;
        $scope.errs = [];
        $scope.result = [];

        // set default parameters
        step = step || 1;
        initial = initial || 'R....';

        // validate the input
        var reg = /^\d+$/;
        if (!reg.test(step)) {
            $scope.errs.push('The step must be integer');
        }
        reg = /^[.LR]+$/;
        if (!reg.test(initial)) {
            $scope.errs.push('The initial state can only have ".", "L", "R"');
        }
        if ($scope.errs.length > 0) return;

        // initial state for counters of left and right
        // for example ..LRR... => state = {left: [2], right:[3,4]}
        var state = {
            left: [],
            right: []
        };
        // define move functions
        var move_left = function(l, i) {
            state.left[i] = l - parseInt(step);
            // out of boundry, set to null
            if (state.left[i] < 0) state.left[i] = null;
        };
        var move_right = function(r, i) {
            state.right[i] = parseInt(r) + parseInt(step);
            // out of boundry, set to null
            if (state.right[i] >= initial.length) state.right[i] = null;
        };

        for (var i = 0; i < initial.length; i++) {
            if (initial.charAt(i) == 'L') {
                state.left.push(i); // add the index to state.left
            } else if (initial.charAt(i) == 'R') {
                state.right.push(i); // add the index to state.left
            }
        }

        // start moving particles
        var counter = 0;
        while (true) {
            // initial a result buffer and empty_flag
            var current_state = '';
            var empty_flag = true;
            // dump the state to a result string, '..LR..' -> '..XX..'
            for (i = 0; i < initial.length; i++) {
                if (state.left.indexOf(i) >= 0 || state.right.indexOf(i) >= 0) {
                    // position i is in either left or right array
                    // the graph is not empty
                    // and assign a X to this position
                    empty_flag = false;
                    current_state += 'x';
                } else {
                    // position i is neither in left nor in right
                    // assign a . to this position
                    current_state += '.';
                }
            }
            current_state += ' ' + counter;
            counter++;
            // put this current state to the result array
            $scope.result.push(current_state);
            // if empty_flag is true, means no particle in the graph, should break
            if (empty_flag) break;

            // move the particles for next time inteval
            state.left.forEach(move_left);
            state.right.forEach(move_right);
        }
    };
}).controller('navCtrl', ['$scope', '$location',
    function($scope, $location) {
        $scope.navClass = function(page) {
            var currentRoute = $location.path().substring(1) || 'question1';
            return page === currentRoute ? 'active' : '';
        };
    }
]);
